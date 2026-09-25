"""Synthetic input tests ONLY; no shipped game data or C# API verification."""
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile


SPEC = importlib.util.spec_from_file_location(
    "inspect_mission_content", Path(__file__).resolve().parents[1] / "tools/inspect_mission_content.py"
)
finder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(finder)


def archive_bytes(entries):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as archive:
        for name, content in entries:
            archive.writestr(name, content)
    stream.seek(0)
    return stream


class EvidenceFinderTests(unittest.TestCase):
    def test_short_discriminator_and_observed_values(self):
        effect = {"$t": "CreateMissionEffect", "DefinitionRef": {"$content": "synthetic-only"},
                  "SpawnRuleOverride": False}
        result = finder.find_effects({"asset": [effect]})[0]
        self.assertEqual(result["pointer"], "/asset/0")
        self.assertEqual(json.loads(result["field_value_displays"]["DefinitionRef"]), effect["DefinitionRef"])
        self.assertEqual(result["field_value_displays"]["SpawnRuleOverride"], "false")
        self.assertEqual(result["fields_not_present"], [])

    def test_full_discriminator_and_missing_fields_are_not_defaulted(self):
        result = finder.find_effects({"$type": "Xenonauts.Strategy.Data.EntityEffects.CreateMissionEffect"})[0]
        self.assertEqual(result["pointer"], "")
        self.assertEqual(result["field_value_displays"], {})
        self.assertEqual(result["fields_not_present"], ["DefinitionRef", "SpawnRuleOverride"])

    def test_descriptions_similar_names_and_unverified_aliases_are_not_matches(self):
        self.assertEqual(finder.find_effects([
            {"text": "CreateMissionEffect"}, {"$t": "CreateActivityEffect"},
            {"$t": "CreateMissionEf"}, {"$type": "Other.CreateMissionEffect"},
            {"$t": None},
        ]), [])

    def test_both_type_keys_are_retained_without_emulating_engine_precedence(self):
        result = finder.find_effects({"$t": "Unknown", "$type": "CreateMissionEffect"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["discriminators"], {"$t": "Unknown", "$type": "CreateMissionEffect"})

    def test_json_pointer_escaping(self):
        result = finder.find_effects({"a/b~c": [{"$t": "CreateMissionEffect"}]})
        self.assertEqual(result[0]["pointer"], "/a~1b~0c/0")

    def test_bom_hash_and_candidate_filename(self):
        raw = b'\xef\xbb\xbf{"$t":"CreateMissionEffect"}'
        archive = archive_bytes([("nested/source.JSON", raw),
                                 ("unknown/root/capture_resources^uoo1.json", "{}")])
        result = finder.scan_archive(archive)
        self.assertEqual(result["status"], "MATCHES_FOUND")
        self.assertEqual(result["json_entries_parsed"], 2)
        self.assertEqual(result["matches"][0]["sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(result["reference_candidates"][0]["entry"], "unknown/root/capture_resources^uoo1.json")

    def test_parse_failure_is_partial_not_absence_of_game_api(self):
        result = finder.scan_archive(archive_bytes([("broken.json", "{bad}"),
                                                     ("ok.json", '{"$t":"CreateMissionEffect"}')]))
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(len(result["matches"]), 1)
        self.assertEqual(result["issues"][0]["reason"], "JSONDecodeError")

    def test_no_matches_is_explicit(self):
        result = finder.scan_archive(archive_bytes([("ordinary.json", "{}"), ("unused.dll", "ignored")]))
        self.assertEqual(result["status"], "NO_MATCHES")
        self.assertEqual(result["json_entries_seen"], 1)

    def test_entry_and_total_read_limits_are_reported(self):
        with patch.object(finder, "MAX_ENTRY_BYTES", 1):
            result = finder.scan_archive(archive_bytes([("large.json", "{}")]))
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["json_entries_parsed"], 0)
        with patch.object(finder, "MAX_TOTAL_BYTES", 2):
            result = finder.scan_archive(archive_bytes([("a.json", "{}"), ("b.json", "{}")]))
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["json_entries_parsed"], 1)

    def test_duplicate_zip_entries_are_not_silently_chosen(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            archive = archive_bytes([("same.json", "{}"), ("same.json", '{"$t":"CreateMissionEffect"}')])
        result = finder.scan_archive(archive)
        self.assertEqual(result["status"], "PARTIAL")
        self.assertEqual(result["json_entries_parsed"], 0)
        self.assertEqual(len(result["issues"]), 1)

    def test_nonfinite_observation_remains_a_display_string(self):
        archive = archive_bytes([("example.json", '{"$t":"CreateMissionEffect","SpawnRuleOverride":Infinity}')])
        result = finder.scan_archive(archive)
        self.assertEqual(result["matches"][0]["field_value_displays"]["SpawnRuleOverride"], "Infinity")
        json.dumps(result, allow_nan=False)

    def test_cli_exit_codes_and_input_is_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.zip"
            for content, expected in [('{"$t":"CreateMissionEffect"}', 0), ("{}", 1), ("{bad}", 2)]:
                before = archive_bytes([("source.json", content)]).getvalue()
                path.write_bytes(before)
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(finder.main([str(path)]), expected)
                self.assertEqual(path.read_bytes(), before)
            path.write_bytes(b"not a zip")
            with redirect_stderr(io.StringIO()):
                self.assertEqual(finder.main([str(path)]), 2)


if __name__ == "__main__":
    unittest.main()
