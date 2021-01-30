from typing import Dict
from dataclasses import dataclass, field

@dataclass
class Config:
    base_elo: int = field(default=1000)
    points_per_match: int = field(default=1)
    k_factor: int = field(default=32)

    period: Dict[str, float] = field(default_factory=dict)

    trigger_threshold: int = field(default=10)
