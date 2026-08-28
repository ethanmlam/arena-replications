# ARENA replications: a small AI-control harness

A from-scratch, testable implementation of the core loop behind AI-control experiments:

- an agent that can call tools without LangChain;
- isolated code execution;
- a parallel eval harness;
- a monitor that scores full trajectories;
- a red-team policy trying to finish a side task without being flagged;
- measured catch rate, false-positive rate, attack success, and honest usefulness.

This is informed by [ControlArena](https://control-arena.aisi.org.uk/), but it does not import ControlArena. The point is to understand and implement the plumbing before comparing against the reference library.

## Authorship and status

The scaffolding, interfaces, configs, serialization, metrics, and tests are prepared. Ethan writes the core implementations. Start with the agent loop:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
pytest tests/test_agent_loop.py -q
```

The failing tests in `tests/test_agent_loop.py` are the spec. Implement `src/arena_control/agent/loop.py` until they pass. It must parse calls, dispatch tools, preserve call IDs, catch errors, support parallel calls, append results, and enforce a max-turn cap.

## Roadmap

- [ ] Agent tool-calling loop from scratch
- [ ] Docker sandbox with no network, read-only root, explicit mounts, timeout, CPU/memory caps, and bounded output
- [ ] Task x mode x seed eval runner with bounded concurrency
- [ ] Honest and attack policies for one small code-sabotage setting
- [ ] Trajectory monitor with a numeric suspicion score and reasons
- [ ] Red-team pass that tries to evade the monitor
- [ ] Pre-register threshold, then report catch rate and false-positive rate
- [ ] Compare the small implementation with ControlArena/Inspect after the from-scratch version works

## Sources

- [ControlArena documentation](https://control-arena.aisi.org.uk/)
- [Neolithic founding MTS role](https://neolithic.org/careers/founding-member-of-technical-staff)
- [Inspect AI](https://inspect.aisi.org.uk/)

## Safety boundary

Use toy tasks and disposable containers only. Do not run untrusted agent commands on the host, expose credentials, or give the sandbox network access.
