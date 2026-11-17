---
name: basecamp-test
description: Run basecamp unit tests
---

# Intent
Run the project's unit tests and give insights on the results especially the missed parts.

# Step-by-Step Instructions
1. Turn on virtual environment venv_basecamp by running `scripts/activate_venv.ps1`
2. Set the path to the project's home directory by running `scripts/cd_basecamp.ps1`
3. Execute unit tests by running `pytest --cov=. --cov-report=term-missing --cov-branch --cov-config=.coveragerc`
4. Give insights to the results and add suggested unit tests for the missed coverage

# Guardrails & Rules
- Never modify files
