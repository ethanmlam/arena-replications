import json
from dataclasses import asdict
from pathlib import Path
from arena_control.types import Trajectory
def write_trajectories(rows:list[Trajectory],path:str|Path)->Path:
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w") as f:
        for row in rows: f.write(json.dumps(asdict(row),sort_keys=True)+"\n")
    return path
