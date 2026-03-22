import pytest

from core.environment.environment import load_env_value, get_aws_access_key_id, get_openapi_key


def test_load_env_value_returns_value(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("MY_KEY=my_value\n")

    assert load_env_value("MY_KEY", str(env_file)) == "my_value"


def test_load_env_value_raises_when_key_missing(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("OTHER_KEY=other\n")

    with pytest.raises(KeyError, match="MISSING_KEY"):
        load_env_value("MISSING_KEY", str(env_file))


def test_load_env_value_raises_when_file_missing():
    with pytest.raises(Exception):
        load_env_value("ANY_KEY", "/nonexistent/.env")


def test_aws_secret_access_key_returns_secret_str(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("AWS_SECRET_ACCESS_KEY=secret123\n")
    monkeypatch.chdir(tmp_path)

    result = get_aws_access_key_id()

    assert result.get_secret_value() == "secret123"


def test_get_aws_access_key_id_returns_secret_str(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("AWS_ACCESS_KEY_ID=keyid456\n")
    monkeypatch.chdir(tmp_path)

    result = get_aws_access_key_id()

    assert result.get_secret_value() == "keyid456"


def test_get_openapi_key_returns_secret_str(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("OPEN_API_KEY=openkey789\n")
    monkeypatch.chdir(tmp_path)

    result = get_openapi_key()

    assert result.get_secret_value() == "openkey789"
