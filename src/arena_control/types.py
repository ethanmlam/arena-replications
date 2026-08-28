from dataclasses import dataclass, field
from typing import Any, Literal

Role = Literal["system", "user", "assistant", "tool"]

@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any]

@dataclass
class Message:
    role: Role
    content: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)
    tool_call_id: str | None = None

@dataclass
class ToolResult:
    call_id: str
    name: str
    content: str
    is_error: bool = False

@dataclass
class Trajectory:
    task_id: str
    mode: Literal["honest", "attack"]
    messages: list[Message]
    task_success: bool = False
    side_task_success: bool = False
    monitor_score: float | None = None
