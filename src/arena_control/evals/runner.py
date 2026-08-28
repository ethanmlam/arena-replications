from collections.abc import Awaitable, Callable, Sequence
from arena_control.evals.spec import TaskSpec
from arena_control.types import Trajectory

async def run_eval(
    tasks: Sequence[TaskSpec],
    modes: Sequence[str],
    seeds: Sequence[int],
    run_one: Callable[[TaskSpec,str,int],Awaitable[Trajectory]],
    *, max_concurrency: int = 8,
) -> list[Trajectory]:
    """Ethan TODO later: run task × mode × seed with bounded concurrency and stable ordering."""
    raise NotImplementedError("Ethan TODO: implement eval matrix runner")
