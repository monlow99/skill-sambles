# 🧠 Project Knowledge & Architecture Patterns

This document captures the key architectural decisions, technology stacks, and patterns discovered during the development of this repository. It serves as a reference for future projects within this workspace.

## 🛠️ Technology Stack & Environment

- **Node.js**: v18.19.1 (LTS)
- **Package Manager**: npm v9.2.0
- **Frontend Framework**: React v19.2.0
- **Build Tool**: Vite v5.4.11 (Fixed for Node 18 compatibility)
- **Styling**: Vanilla CSS (Modern CSS properties: variables, radial-gradients, backdrop-filters).

## 📐 Design Patterns

### 1. Glassmorphism Design System
Used in **LuminaNotes** to create a premium feel:
- **Backgrounds**: Deep `slate-950` (`#020617`) with subtle radial gradients for depth.
- **Glass Effect**: `backdrop-filter: blur(12px)` combined with semi-transparent borders and backgrounds.
- **Typography**: `Outfit` (Google Fonts) for a modern, tech-focused aesthetic.

### 2. Skill-Driven Development
The repository follows a strict modular structure where "Skills" extend the agent's capabilities:
- **Location**: `.agents/skills/[skill-name]/`
- **Structure**: `SKILL.md` (Docs), `scripts/` (Logic), `resources/` (Assets).
- **Installed Skills**:
    - `commiter`: Enforces Conventional Commits.
    - `skill-creator`: Bootstraps new skills.
    - `changelog`: Automates `CHANGELOG.md` generation.
    - `frontend-design`: UI/UX design assistant.
    - `vercel-react-best-practices`: Performance guidelines.

### 3. Git Automation
- **Changelog Hook**: A `post-commit` hook is installed via `.agents/skills/changelog/scripts/setup_hooks.py`.
- **Formatting**: `type(scope): message` format is required for all commits to maintain the automated changelog.

## 🚀 Environment Compatibility Notes

### Vite & Node 18
When creating new apps in this environment, **avoid Vite v6+**. 
Always downgrade to **Vite v5** and `@vitejs/plugin-react` v4 in `package.json` to avoid "EBADENGINE" errors.

```bash
# Correct versions for Node 18
npm install vite@5 @vitejs/plugin-react@4
```

## 📂 Key Files
- [README.md](file:///home/monlow99/skill-sambles/README.md): Main overview.
- [CHANGELOG.md](file:///home/monlow99/skill-sambles/CHANGELOG.md): History of all changes.
- [notes-app/](file:///home/monlow99/skill-sambles/notes-app/): Reference React implementation.
