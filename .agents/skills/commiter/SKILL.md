---
name: commiter
description: Commits changes to the repository in a structured way
---

# 📝 Committer Skill Guide

This skill ensures that all changes to the repository follow the **Conventional Commits** standard, maintaining a clean and machine-readable history.

## 📐 Commit Format

Every commit must follow this structure:

```text
<type>(<scope>): <subject>

[optional body]

[optional footer(s)]
```

### 1. Title (Subject Line)
- **Limit**: Exactly **50 characters** or less.
- **Style**: Imperative, present tense (e.g., "add feature" instead of "added feature" or "adds feature").
- **Format**: `type(scope): description`
- **Constraint**: Do not capitalize the first letter and do not end with a period.

### 2. Commit Types
Each commit type is represented by a specific emoji to improve visual scanning:

| Emoji | Type | Description |
| :--- | :--- | :--- |
| ✨ | `feat` | A new feature for the user, not a new feature for build scripts |
| 🐛 | `fix` | A bug fix for the user, not a fix to a build script |
| 📝 | `docs` | Changes to the documentation |
| 🎨 | `style` | Formatting, missing semi-colons, etc; no production code change |
| ♻️ | `refactor` | Refactoring production code, e.g. renaming a variable |
| ⚡️ | `perf` | Code change that improves performance |
| ✅ | `test` | Adding missing tests, refactoring tests; no production code change |
| 🏗️ | `build` | Changes that affect the build system or external dependencies |
| 💚 | `ci` | Changes to our CI configuration files and scripts |
| 🔨 | `chore` | Other changes that don't modify src or test files |
| ⏪ | `revert` | Reverts a previous commit |

### 3. Detailed Description (Body)
The body is **required** when the change is non-trivial. It should provide a clear contrast between the old and new behavior.
- Use the body to explain the **WHY** behind the change.
- Use bullet points for multiple changes.
- Separate the body from the title with a blank line.

### 4. Breaking Changes
For any breaking change, you must:
1. Add a `!` after the type/scope (e.g., `feat(api)!: break user login`).
2. Include a `BREAKING CHANGE:` footer with a description of the change and migration instructions.

---

## 💡 Examples

### Good Commit ✅
```text
feat(auth): add google oauth2 provider

Implement the Google OAuth2 flow to allow users to sign in 
using their Google accounts. This replaces the legacy 
custom provider which was deprecated last month.

- Add passport-google-oauth20 dependency
- Implement AuthController.googleLogin
- Update security config to allow oauth callbacks
```

### Bad Commit ❌
```text
Fixing the bug where the user could not login after logout.  # Too long, past tense, ends with period
```

---
*Follow these rules strictly to maintain repository integrity.*