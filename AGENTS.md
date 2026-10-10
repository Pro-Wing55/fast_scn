# Agent Instructions

- The application is a small Python FastAPI service; keep application changes within the existing `app/model` and `app/service` structure unless the task calls for an architectural change.
- Treat `git.path` as local VS Code Git extension configuration, not application configuration. Do not add it to Python code, dependencies, or shared project settings to fix one developer's Git setup.
- If Git is not detected, check whether Git is installed and inspect the VS Code Git output and effective `git.path` setting. A developer-specific `git.exe` path belongs in local VS Code settings and must not be committed.
- No README, test configuration, or documented project commands are present. Do not assume a test or launch command; verify available project tooling before relying on one.