from pycloc.__main__ import compute_data

def test_cpp():
    should_be = ["C++", 1, 13, 5, 6, 2]
    result = compute_data("tests/files/cpp/test.cpp")
    assert should_be == result[0]