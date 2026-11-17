# compat: populace alias, remove after 0.2.0
"""Deprecated alias for :mod:`l0_paper.microcosm_smoke`.

Import from ``l0_paper.microcosm_smoke`` instead; this module goes in the next
release.
"""

import warnings

from l0_paper.microcosm_smoke import (  # compat: populace alias, remove after 0.2.0
    SmokeCalibration,
    make_toy_frame,
    make_toy_targets,
    run_l0_smoke,
)

__all__ = ["SmokeCalibration", "make_toy_frame", "make_toy_targets", "run_l0_smoke"]

warnings.warn(  # compat: populace alias, remove after 0.2.0
    "l0_paper.populace_smoke is now l0_paper.microcosm_smoke; "
    "the old name goes in the next release",
    DeprecationWarning,
    stacklevel=2,
)
