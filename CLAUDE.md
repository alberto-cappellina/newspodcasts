# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`newspodcasts` — a LangGraph + LangChain pipeline that fetches Gmail newsletters and converts them to a podcast.

## Environment

A virtual environment is at `.venv/`. Activate it before running Python commands:

```bash
source .venv/bin/activate
```

## Commands

```bash
# Install dependencies (editable)
pip install -e .

# Run the pipeline (triggers OAuth2 browser flow on first run)
python newspodcasts.py
```

Place `credentials.json` (downloaded from Google Cloud Console) in the project root before the first run. The OAuth2 token is cached in `token.json` after consent.
