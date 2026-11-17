"""Former name of ``microcosm_pipeline.py``, kept for one release; runs it unchanged."""

# compat: populace alias, remove after 0.2.0
import runpy
from pathlib import Path

runpy.run_path(
    str(Path(__file__).with_name("microcosm_pipeline.py")), run_name="__main__"
)
