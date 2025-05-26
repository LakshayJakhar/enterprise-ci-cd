import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import main


def test_main_runs():
    expected_value = 42
    result = main.some_function()
    assert result == expected_value
