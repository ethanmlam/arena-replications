from arena_control.analysis.metrics import compute_metrics
from arena_control.types import Trajectory
def row(mode,score,task=True,side=False): return Trajectory("t",mode,[],task,side,score)
def test_control_metrics():
    m=compute_metrics([row("honest",.1),row("honest",.9),row("attack",.8,side=True),row("attack",.2,side=True)],.5)
    assert m.catch_rate==.5; assert m.false_positive_rate==.5; assert m.attack_success_rate==1
