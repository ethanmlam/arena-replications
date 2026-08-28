from collections.abc import Awaitable, Callable, Mapping, Sequence
from typing import Any
from arena_control.types import Message, ToolResult

ModelFn = Callable[[Sequence[Message], Sequence[dict[str, Any]]], Awaitable[Message]]
ToolFn = Callable[..., Any]

async def run_agent_loop(
    model: ModelFn,
    messages: list[Message],
    tool_schemas: list[dict[str, Any]],
    tools: Mapping[str, ToolFn],
    *,
    max_turns: int = 20,
) -> list[Message]:
    """Run an agent until it returns text or reaches max_turns.

    Ethan TODO, in this order:
    1. Call `model` with the full message history and JSON tool schemas.
    2. Append each assistant response verbatim.
    3. If it has no tool calls, return the trajectory.
    4. Validate tool name and arguments, dispatch every call, and catch errors.
    5. Support parallel calls with asyncio.gather while preserving call IDs.
    6. Append one `role="tool"` message per result, matched by tool_call_id.
    7. Raise MaxTurnsError after max_turns rather than spinning forever.

    Tests are the executable specification. Do not use LangChain.
    """
    raise NotImplementedError("Ethan TODO: implement the agent tool-calling loop")

class MaxTurnsError(RuntimeError):
    pass
