from pathlib import Path
from arena_control.sandbox.runner import DockerSandbox,SandboxPolicy
def test_secure_defaults(tmp_path:Path):
    p=SandboxPolicy("python:3.12-slim"); assert p.network is False; assert p.read_only_root is True; assert p.timeout_seconds<=30
