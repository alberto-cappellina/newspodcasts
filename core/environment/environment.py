from dotenv import dotenv_values
from pydantic import SecretStr

def get_hf_token() -> str:
    key = load_env_value('HF_TOKEN')
    return key


def get_openapi_key():
    key = load_env_value('OPEN_API_KEY')
    return SecretStr(key)


def load_env_value(key: str, env_path: str = ".env") -> str:
    values = dotenv_values(env_path)
    if key not in values:
        raise KeyError(f"Key '{key}' not found in {env_path}")
    return values[key]