import asyncio
import pytest
from arena_control.agent.loop import MaxTurnsError, run_agent_loop
from arena_control.types import Message, ToolCall

async def test_returns_when_model_stops_calling_tools():
    async def model(messages,schemas): return Message(role="assistant",content="done")
    out=await run_agent_loop(model,[Message(role="user",content="go")],[],{})
    assert out[-1].content=="done"

async def test_dispatches_parallel_calls_and_preserves_ids():
    calls=[]
    async def add(x,y): calls.append((x,y)); await asyncio.sleep(.01); return x+y
    responses=iter([Message(role="assistant",tool_calls=[ToolCall("a","add",{"x":1,"y":2}),ToolCall("b","add",{"x":4,"y":5})]),Message(role="assistant",content="done")])
    async def model(messages,schemas): return next(responses)
    out=await run_agent_loop(model,[Message(role="user",content="go")],[{"name":"add"}],{"add":add})
    results=[m for m in out if m.role=="tool"]
    assert {m.tool_call_id for m in results}=={"a","b"}; assert {m.content for m in results}=={"3","9"}

async def test_tool_error_becomes_result_not_crash():
    def explode(): raise ValueError("boom")
    responses=iter([Message(role="assistant",tool_calls=[ToolCall("x","explode",{})]),Message(role="assistant",content="recovered")])
    async def model(messages,schemas): return next(responses)
    out=await run_agent_loop(model,[Message(role="user",content="go")],[],{"explode":explode})
    assert out[-2].role=="tool" and "boom" in out[-2].content

async def test_max_turn_cap():
    async def model(messages,schemas): return Message(role="assistant",tool_calls=[ToolCall("x","noop",{})])
    with pytest.raises(MaxTurnsError): await run_agent_loop(model,[],[],{"noop":lambda:None},max_turns=2)
