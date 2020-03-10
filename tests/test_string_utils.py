from spirit.utils.string_utils import non_key_sensitive_match


def test_non_key_sensitive_match():
    assert non_key_sensitive_match("hello", "Hello")
