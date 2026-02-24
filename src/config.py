import os
from dataclasses import dataclass
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from streamlit.errors import StreamlitSecretNotFoundError


@dataclass
class AppConfig:
    agent_id: str | None
    env_file: Path | None


def read_secret_agent_id() -> str | None:
    try:
        value = st.secrets.get("AGENT_ID")
    except StreamlitSecretNotFoundError:
        return None

    if not value:
        return None
    return str(value).strip() or None


def find_env_file(env_path: Path | None = None) -> Path | None:
    project_root = Path(__file__).resolve().parent.parent
    candidates: list[Path] = []

    if env_path is not None:
        given = Path(env_path)
        if given.is_absolute():
            candidates.append(given)
        else:
            candidates.append(Path.cwd() / given)
            candidates.append(project_root / given)

    candidates.extend(
        [
            project_root / ".env",
            Path.cwd() / ".env",
        ]
    )

    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if resolved.exists() and resolved.is_file():
            return resolved

    return None


def load_config(env_path: Path | None = None) -> AppConfig:
    resolved_env_file = find_env_file(env_path)

    if resolved_env_file:
        load_dotenv(dotenv_path=resolved_env_file, override=False)
    else:
        load_dotenv(override=False)

    secret_agent_id = read_secret_agent_id()
    env_agent_id = os.getenv("AGENT_ID")
    agent_id = (secret_agent_id or env_agent_id or "").strip() or None

    return AppConfig(agent_id=agent_id, env_file=resolved_env_file)
