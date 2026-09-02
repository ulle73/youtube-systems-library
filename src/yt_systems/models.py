from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum


class Provenance(str, Enum):
    EXACT = "EXACT"
    RECONSTRUCTED = "RECONSTRUCTED"
    INFERRED = "INFERRED"


@dataclass(frozen=True)
class EvidenceRef:
    source_url: str
    timestamp: str | None
    provenance: Provenance
    note: str = ""

    def to_dict(self) -> dict[str, str | None]:
        data = asdict(self)
        data["provenance"] = self.provenance.value
        return data
