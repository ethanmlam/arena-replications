from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class SandboxPolicy:
    image: str
    timeout_seconds: int = 30
    memory_mb: int = 512
    cpus: float = 1.0
    network: bool = False
    read_only_root: bool = True

@dataclass
class ExecutionResult:
    exit_code: int | None
    stdout: str
    stderr: str
    timed_out: bool = False

class DockerSandbox:
    """Execute untrusted commands with explicit isolation and resource limits."""
    def __init__(self, policy: SandboxPolicy, workdir: Path): self.policy=policy; self.workdir=workdir
    def run(self, argv: list[str]) -> ExecutionResult:
        """Ethan TODO later: no shell=True; cap output; enforce timeout, CPU, memory, network, mounts."""
        raise NotImplementedError("Ethan TODO: implement sandboxed execution")
