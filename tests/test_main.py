from src import main

def test_main_runs():
    expected_value = 42 
    result = main.some_function()  
    assert result == expected_value
