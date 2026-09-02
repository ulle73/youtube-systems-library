from yt_systems.models import EvidenceRef, Provenance


def test_provenance_has_three_allowed_values():
    assert [p.value for p in Provenance] == ["EXACT", "RECONSTRUCTED", "INFERRED"]


def test_evidence_ref_serializes_source_trace():
    ref = EvidenceRef(
        source_url="https://youtube.com/watch?v=abc",
        timestamp="00:03:12",
        provenance=Provenance.EXACT,
        note="Prompt visible on screen",
    )
    assert ref.to_dict() == {
        "source_url": "https://youtube.com/watch?v=abc",
        "timestamp": "00:03:12",
        "provenance": "EXACT",
        "note": "Prompt visible on screen",
    }
