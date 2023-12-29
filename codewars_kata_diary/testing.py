from typing import Callable


def test_func(inputs: list, expected: list, func: Callable):
    """Function to test a function with multiple test cases

    Note: Yes I could have used pytest or unittest, but I want to keep this
    repo simple.

    Args:
        inputs (list): List of inputs to test the function
        expected (list): List of expected outputs
        func (callable): Function to test
    """
    assert len(inputs) == len(
        expected
    ), "Length of inputs and expected should be equal"

    print(f"Testing function {func.__name__}", end="\n\n")
    num_passed = 0
    for i, (inp, out) in enumerate(zip(inputs, expected)):
        print(f"Test Case #{i + 1}")
        print("Input: ", inp)
        print("Expected Output: ", out)
        if isinstance(inp, tuple):
            res = func(*inp)
        else:
            res = func(inp)
        print("Actual Output: ", res)
        if res == out:
            print("[Passed]", end="\n\n")
            num_passed += 1
        else:
            print("[Failed]", end="\n\n")

    print(f"{num_passed}/{len(inputs)} test cases passed")
