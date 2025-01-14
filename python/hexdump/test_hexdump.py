from python.hexdump.main import hexdump
from pytest import raises


def test_empty():
    assert hexdump(b"") == "<empty>"
    assert hexdump(b"", 0, 0) == "<empty>"


def test_short_string():
    assert (
        hexdump(b"42") == "0000 | 34 32                                            | 42"
    )
    assert (
        hexdump(b"42 a b")
        == "0000 | 34 32 20 61 20 62                                | 42 a b"
    )


def test_long_string():
    assert (
        hexdump(b"42" * 10)
        == "0000 | 34 32 34 32 34 32 34 32 34 32 34 32 34 32 34 32  | 4242424242424242\n0010 | 34 32 34 32                                      | 4242"
    )


def test_null_bytes():
    with raises(TypeError, match="object of type 'NoneType' has no len()"):
        hexdump(None)


def test_addr():
    assert (
        hexdump(b"42", addr=1, num=0)
        == "0001 | 34 32                                            | 42"
    )
    assert (
        hexdump(b"42", addr=10, num=0)
        == "000a | 34 32                                            | 42"
    )


def test_num_under_16():
    assert (
        hexdump(b"42", num=1)
        == "0000 | 34 32                                            | 42"
    )
    assert (
        hexdump(b"42", num=0)
        == "0000 | 34 32                                            | 42"
    )
    assert (
        hexdump(b"42", num=10)
        == "0000 | 34 32                                            | 42"
    )


def test_num_over_16():
    assert (
        hexdump(b"42", num=100)
        == """0000 | 34 32                                            | 42
0010 |                                                  | 
0020 |                                                  | 
0030 |                                                  | 
0040 |                                                  | 
0050 |                                                  | 
0060 |                                                  | """
    )


def test_negative_num():
    assert hexdump(b"42", num=-1) == ""
    assert hexdump(b"42", num=-10) == ""
    assert hexdump(b"42", num=-100) == ""
