import importlib
import sys

import pytest

from l0_paper import microcosm_smoke
from l0_paper.microcosm_smoke import make_toy_frame, make_toy_targets, run_l0_smoke


def test_toy_targets_compile_against_microcosm_frame():
    frame, truths = make_toy_frame(seed=1, n=30)
    targets = make_toy_targets(truths)

    assert frame.n("household") == 30
    assert len(targets) == 3


def test_l0_smoke_uses_microcosm_budget_control():
    summary = run_l0_smoke(seed=0, n=120, target_records=60, epochs=120)

    assert summary.final_loss < summary.initial_loss
    assert summary.n_nonzero < summary.n_records
    assert summary.l0_lambda > 0


def test_legacy_smoke_module_warns_and_reexports():
    # compat: populace alias, remove after 0.2.0
    legacy_name = "l0_paper.populace_smoke"
    sys.modules.pop(legacy_name, None)
    with pytest.warns(DeprecationWarning, match="microcosm_smoke"):
        legacy = importlib.import_module(legacy_name)

    assert len(legacy.__all__) == 4
    for name in legacy.__all__:
        assert getattr(legacy, name) is getattr(microcosm_smoke, name)
