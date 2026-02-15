---
name: changelog
description: Automatically generates and updates a CHANGELOG.md based on conventional commits.
---

# 📜 Changelog Generator Skill

This skill helps maintain a clean and automated `CHANGELOG.md` file by parsing your Git commit history. It works best with repositories following the **Conventional Commits** standard.

## 🚀 Features

- **Automatic Grouping**: Categorizes changes into Features, Bug Fixes, Documentation, etc.
- **Incremental Updates**: Can detect new commits since the last version.
- **Conventional Commit Support**: Uses types like `feat`, `fix`, `docs`, and `refactor`.

## 🛠️ Usage

### Generate/Update Changelog
Run the following script to scan the commit history and update the `CHANGELOG.md` in the root of the repository:

```bash
python3 .agents/skills/changelog/scripts/update_changelog.py
```

## 📐 Formatting Rules

The generator follows these conventions:
- **Features (feat)**: Listed under a "Features" header.
- **Bug Fixes (fix)**: Listed under a "Bug Fixes" header.
- **Other changes**: Grouped by their commit type.
- **Breaking Changes**: Highlighted at the top of the version section.

---
*Follow the [commiter](file:///home/monlow99/skill-sambles/.agents/skills/commiter/SKILL.md) guidelines to ensure the best results.*
