from pathlib import Path
import yaml
from yt_systems.validate import validate_system


def test_validation_accepts_valid_manifest(tmp_path: Path):
    d = tmp_path / 'sys'; d.mkdir()
    manifest = {
      'id':'x','name':'X','category':'content','source':{'type':'youtube','url':'https://youtube.com/x'},
      'reconstruction_status':'RECONSTRUCTED','inputs':[],'outputs':['post'],'tools':['n8n'],
      'steps':[{'id':'s1','name':'Trigger','action':'receive webhook','tool':'n8n','provenance':'EXACT','evidence':[{'source_url':'https://youtube.com/x','timestamp':'00:01:00','provenance':'EXACT','note':''}]}]
    }
    (d/'system.yaml').write_text(yaml.safe_dump(manifest), encoding='utf-8')
    assert validate_system(d) == []


def test_validation_rejects_step_without_evidence(tmp_path: Path):
    d = tmp_path / 'sys'; d.mkdir()
    manifest = {
      'id':'x','name':'X','category':'content','source':{'type':'youtube','url':'u'},
      'reconstruction_status':'DRAFT','inputs':[],'outputs':[],'tools':[],
      'steps':[{'id':'s1','name':'Bad','action':'do','provenance':'EXACT','evidence':[]}]
    }
    (d/'system.yaml').write_text(yaml.safe_dump(manifest), encoding='utf-8')
    errors = validate_system(d)
    assert errors
    assert any('evidence' in e for e in errors)
