from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("message", 0) == "egassem"

    assert encrypt_message("message", 3) == "egas_sem"

    assert encrypt_message("message", 2) == "ssemeg_am"

    assert encrypt_message("message", 4) == "mseg_essa"

    with pytest.raises(TypeError):
        encrypt_message("message", "key")
