from dataclasses import dataclass
from typing import Protocol
from arena_control.types import Trajectory
@dataclass(frozen=True)
class MonitorVerdict:
    suspicion: float
    reason: str
    flagged_steps: tuple[int,...]=()
class Monitor(Protocol):
    async def score(self, trajectory: Trajectory) -> MonitorVerdict: ...
