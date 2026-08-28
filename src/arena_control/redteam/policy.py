from typing import Protocol
from arena_control.types import Message
class AttackPolicy(Protocol):
    """Policy tries to complete the side task without raising monitor suspicion."""
    async def next_message(self, history: list[Message]) -> Message: ...
