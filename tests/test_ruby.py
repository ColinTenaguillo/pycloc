from pycloc.__main__ import compute_data

def test_easy_ruby():
    should_be = ["RUBY", 1, 7, 1, 4, 2]
    result = compute_data("tests/files/ruby/easy.rb")
    print(result[0], should_be)
    assert should_be == result[0]
