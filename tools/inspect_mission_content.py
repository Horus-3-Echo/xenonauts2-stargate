"""Read-only XSG-004A evidence finder; NOT a game-data validator or launcher.

Input is the user's actual moddable_content.zip, never a guessed install path.
Output is diagnostic JSON on stdout. No extraction, patching, or runtime imports.
Only documented CreateMissionEffect discriminators are recognized. Other aliases,
comments, and other engine-specific JSON extensions are not inferred.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import PurePosixPath
import sys
import zipfile


EFFECT_TYPES = frozenset({
    "CreateMissionEffect",
    "Xenonauts.Strategy.Data.EntityEffects.CreateMissionEffect",
})
OBSERVED_FIELDS = ("DefinitionRef", "SpawnRuleOverride")
REFERENCE_BASENAME = "capture_resources^uoo1.json"
MAX_ENTRY_BYTES = 16 * 1024 * 1024
MAX_TOTAL_BYTES = 512 * 1024 * 1024


def pointer_token(value):
    return str(value).replace("~", "~0").replace("/", "~1")


def find_effects(document):
    """Return observations, not a schema or a claim that the effect is valid."""
    found = []
    pending = [("", document)]
    while pending:
        pointer, node = pending.pop()
        if isinstance(node, dict):
            discriminators = {
                key: node[key] for key in ("$t", "$type")
                if isinstance(node.get(key), str)
            }
            if any(value in EFFECT_TYPES for value in discriminators.values()):
                # String displays also preserve Python json's Infinity/NaN support
                # without putting non-finite numeric values in our output schema.
                found.append({
                    "pointer": pointer,
                    "discriminators": discriminators,
                    "observed_field_names": sorted(node),
                    "field_value_displays": {
                        key: json.dumps(node[key], ensure_ascii=False, sort_keys=True)
                        for key in OBSERVED_FIELDS if key in node
                    },
                    "fields_not_present": [key for key in OBSERVED_FIELDS if key not in node],
                })
            for key, value in reversed(list(node.items())):
                pending.append((pointer + "/" + pointer_token(key), value))
        elif isinstance(node, list):
            for index in range(len(node) - 1, -1, -1):
                pending.append((pointer + "/" + str(index), node[index]))
    return found


def scan_archive(source):
    """Scan ZIP bytes read-only. Accept a filename or binary file-like object."""
    report = {
        "purpose": "XSG-004A content observations, not runtime validation",
        "json_entries_seen": 0,
        "json_entries_parsed": 0,
        "matches": [],
        "reference_candidates": [],
        "issues": [],
    }
    total = 0
    with zipfile.ZipFile(source, "r") as archive:
        entries = sorted(
            (entry for entry in archive.infolist()
             if not entry.is_dir() and entry.filename.lower().endswith(".json")),
            key=lambda entry: entry.filename,
        )
        counts = Counter(entry.filename for entry in entries)
        reported_duplicates = set()
        report["json_entries_seen"] = len(entries)
        for entry in entries:
            name = entry.filename
            if counts[name] > 1:
                if name not in reported_duplicates:
                    report["issues"].append({"entry": name, "reason": "duplicate ZIP member name; skipped"})
                    reported_duplicates.add(name)
                continue
            if entry.file_size > MAX_ENTRY_BYTES:
                report["issues"].append({"entry": name, "reason": "entry exceeds read limit; skipped"})
                continue
            if total + entry.file_size > MAX_TOTAL_BYTES:
                report["issues"].append({"entry": name, "reason": "total read limit reached; remaining entries skipped"})
                break
            total += entry.file_size
            try:
                raw = archive.read(entry)
                digest = hashlib.sha256(raw).hexdigest()
                if PurePosixPath(name).name == REFERENCE_BASENAME:
                    report["reference_candidates"].append({"entry": name, "sha256": digest})
                document = json.loads(raw.decode("utf-8-sig"))
                matches = find_effects(document)
            except (ValueError, RecursionError, OSError, RuntimeError, zipfile.BadZipFile) as error:
                report["issues"].append({"entry": name, "reason": type(error).__name__})
                continue
            report["json_entries_parsed"] += 1
            for match in matches:
                report["matches"].append({"entry": name, "sha256": digest, **match})
    report["status"] = (
        "PARTIAL" if report["issues"] else
        "MATCHES_FOUND" if report["matches"] else "NO_MATCHES"
    )
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="Actual moddable_content.zip path (read-only)")
    args = parser.parse_args(argv)
    try:
        report = scan_archive(args.archive)
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as error:
        print("Unable to inspect content archive: " + type(error).__name__, file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False))
    if report["issues"]:
        return 2
    return 0 if report["matches"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
