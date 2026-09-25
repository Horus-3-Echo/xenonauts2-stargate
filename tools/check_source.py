"""Check source packaging only. Does not compile C# or start Xenonauts 2."""
from pathlib import Path
import json
import uuid
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'mod/manifest.json').read_text(encoding='utf-8'))
assert manifest['version'] == '0.0.4'
assert manifest['$type'] == 'Common.Content.DataStructures.VersionedAsset'
assert manifest['asset']['$type'] == 'Common.Content.DataStructures.ContentPackManifest'
uuid.UUID(manifest['asset']['UID'])
project = ET.parse(root / 'src/StargateX2/StargateX2.csproj').getroot()
refs = [x.attrib['Include'] for x in project.findall('.//Reference')]
assert len(refs) == len(set(refs)), 'Duplicate assembly reference name'
assert all(x.findtext('Private') == 'false' for x in project.findall('.//Reference'))
assert project.findtext('.//AssemblyName') == 'StargateX2'
ET.parse(root / 'GamePaths.props.example')
for name in ['README.md', 'AGENTS.md', 'BUILD.md', 'STATUS.md', 'BACKLOG.md',
             'DECISIONS.md', 'docs/BRIEF.md', 'src/StargateX2/StargateModLifecycle.cs']:
    assert (root / name).is_file(), name
json.loads((root / 'environment.example.json').read_text(encoding='utf-8'))
print('PASS T00: XSG manifest, XML, assembly references and source structure')
print('NOT_RUN T01-T04: no compiler, game libraries or game runtime')
