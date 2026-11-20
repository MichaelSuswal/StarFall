"""Run the tools self-tests without pytest: python3 tests/tools/run.py"""
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import test_tools  # noqa: E402

failed = 0
names = [n for n in dir(test_tools) if n.startswith("test_")]
for n in names:
    try:
        getattr(test_tools, n)()
        print(f"ok    {n}")
    except Exception:
        failed += 1
        print(f"FAIL  {n}")
        traceback.print_exc()
print(f"{len(names) - failed} passed, {failed} failed")
sys.exit(1 if failed else 0)
