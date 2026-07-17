from pathlib import Path

from py_lib_policy import Violation
from py_lib_testkit import run_async
from ternforge_python_consumer_r2 import answer, runtime_preview


def test_answer() -> None:
    assert answer() == 42


def test_split_tooling_dependencies() -> None:
    async def sample() -> int:
        return answer()

    assert runtime_preview("consumer") == "consumer"
    assert Violation(Path("sample.py"), "example").render(Path.cwd()).endswith("sample.py: example")
    assert run_async(sample()) == 42
