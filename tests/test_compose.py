from yt_systems.compose import compare_systems, compose_candidate


def test_compare_systems_reports_shared_and_unique_tools():
    systems = [
        {'id':'a','tools':['n8n','Claude'],'outputs':['linkedin']},
        {'id':'b','tools':['n8n','OpenAI'],'outputs':['newsletter']},
    ]
    comparison = compare_systems(systems)
    assert comparison['shared_tools'] == ['n8n']
    assert comparison['unique_tools']['a'] == ['Claude']


def test_compose_candidate_preserves_component_source_provenance():
    systems = [
        {'id':'a','name':'A','source':{'url':'u1'},'steps':[{'id':'research','name':'Research','action':'find topics','provenance':'EXACT','evidence':[{'source_url':'u1','provenance':'EXACT'}]}]},
        {'id':'b','name':'B','source':{'url':'u2'},'steps':[{'id':'publish','name':'Publish','action':'publish post','provenance':'RECONSTRUCTED','evidence':[{'source_url':'u2','provenance':'RECONSTRUCTED'}]}]},
    ]
    result = compose_candidate('canonical-content','Canonical Content',systems,[('a','research'),('b','publish')])
    assert result['steps'][0]['derived_from']['system_id'] == 'a'
    assert result['steps'][1]['derived_from']['system_id'] == 'b'
