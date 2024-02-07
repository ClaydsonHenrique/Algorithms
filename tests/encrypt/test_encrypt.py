from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("message", 0) == "egassem"

    assert encrypt_message("message", 3) == "sem_egas"

    assert encrypt_message("message", 2) == "egass_em"

    assert encrypt_message("message", 4) == "ega_ssem"

    with pytest.raises(TypeError):
        encrypt_message("message", "keyError")
