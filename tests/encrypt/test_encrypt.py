import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    with pytest.raises(TypeError):
        encrypt_message("message", "key")

    with pytest.raises(TypeError):
        encrypt_message(123, 4)

    assert encrypt_message("message", 0) == "egassem"

    assert encrypt_message("message", 7) == "egassem"

    assert encrypt_message("message", 3) == "ssemeg_am"

    assert encrypt_message("message", 4) == "mseg_essa"

    assert encrypt_message("hello_world", 6) == "dlo_worlh_el"

    assert encrypt_message("hello_world", 5) == "o_dlohl_wrld"
