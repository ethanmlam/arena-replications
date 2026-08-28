from dataclasses import dataclass, field
from typing import Any
@dataclass(frozen=True)
class TaskSpec:
    id: str
    prompt: str
    main_task_scorer: str
    side_task_scorer: str | None = None
    metadata: dict[str,Any] = field(default_factory=dict)
