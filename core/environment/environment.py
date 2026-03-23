from dotenv import dotenv_values
from pydantic import SecretStr


def get_aws_secret_access_key() -> SecretStr:
    key = load_env_value('AWS_SECRET_ACCESS_KEY')
    return SecretStr(key)


def get_aws_access_key_id() -> SecretStr:
    key = load_env_value('AWS_ACCESS_KEY_ID')
    return SecretStr(key)


def get_openapi_key() -> SecretStr:
    key = load_env_value('OPEN_API_KEY')
    return SecretStr(key)


def load_env_value(key: str, env_path: str = ".env") -> str:
    values = dotenv_values(env_path)
    if key not in values:
        raise KeyError(f"Key '{key}' not found in {env_path}")
    return values[key]
