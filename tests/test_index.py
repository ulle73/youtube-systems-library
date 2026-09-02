from pathlib import Path
import json, yaml
from yt_systems.index import build_index, search_index


def _write_system(root: Path, slug: str, name: str, category: str, tools, outputs):
    d = root / slug; d.mkdir(parents=True)
    manifest = {
      'id':slug,'name':name,'category':category,'source':{'type':'youtube','url':'https://youtube.com/'+slug},
      'reconstruction_status':'RECONSTRUCTED','inputs':[],'outputs':outputs,'tools':tools,'steps':[]
    }
    (d/'system.yaml').write_text(yaml.safe_dump(manifest), encoding='utf-8')


def test_index_and_search_find_by_tool_and_output(tmp_path: Path):
    root = tmp_path/'systems'; root.mkdir()
    _write_system(root,'content-a','Content Engine','content',['n8n','Claude'],['linkedin','newsletter'])
    _write_system(root,'seo-a','SEO Engine','seo',['Python'],['pages'])
    index_path = tmp_path/'index.json'
    records = build_index(root,index_path)
    assert len(records) == 2
    results = search_index(index_path,'n8n linkedin')
    assert results[0]['id'] == 'content-a'
