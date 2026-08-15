import pytest

from src.decorators import log, write_log


def test_log(capsys):
    write_log("", "test_message")
    captured = capsys.readouterr()
    output = captured.out
    assert output == "test_message\n"


@log("")
def wrong():
    raise ValueError("error")


def test_log_error(capsys):
    with pytest.raises(ValueError, match="error"):
        wrong()
    captured = capsys.readouterr()
    output = captured.out
    assert "start" in output
    assert "end" in output
    assert "error" in output
