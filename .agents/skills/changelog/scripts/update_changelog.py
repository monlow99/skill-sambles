import subprocess
import os
import re
from datetime import datetime

def get_git_commits():
    try:
        # Get all commits in the format: hash|type|scope|subject
        # Using %s for the subject which usually contains the conventional commit format
        result = subprocess.run(
            ['git', 'log', '--pretty=format:%H|%s'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.split('\n')
    except subprocess.CalledProcessError:
        return []

def parse_commits(commits):
    categories = {
        'feat': '✨ Features',
        'fix': '🐛 Bug Fixes',
        'docs': '📝 Documentation',
        'style': '🎨 Style',
        'refactor': '♻️ Refactor',
        'perf': '⚡️ Performance',
        'test': '✅ Test',
        'build': '🏗️ Build',
        'ci': '💚 CI',
        'chore': '🔨 Chore',
        'revert': '⏪ Reverts'
    }
    
    parsed = {cat: [] for cat in categories.values()}
    other = []

    # Regex for conventional commits: type(scope): subject or type: subject
    commit_pattern = re.compile(r'^(\w+)(?:\(([^)]+)\))?!?: (.+)$')

    for line in commits:
        if not line:
            continue
        parts = line.split('|', 1)
        if len(parts) < 2:
            continue
        
        hash_val = parts[0][:7]
        message = parts[1]
        
        match = commit_pattern.match(message)
        if match:
            ctype, scope, subject = match.groups()
            category_name = categories.get(ctype, 'Other')
            
            scope_prefix = f"**{scope}**: " if scope else ""
            entry = f"- {scope_prefix}{subject} ([{hash_val}])"
            
            if category_name in parsed:
                parsed[category_name].append(entry)
            else:
                other.append(entry)
        else:
            other.append(f"- {message} ([{hash_val}])")

    return parsed, other

def generate_markdown(parsed, other):
    lines = [f"# CHANGELOG\n", f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
    
    for category, items in parsed.items():
        if items:
            lines.append(f"## {category}")
            lines.extend(items)
            lines.append("")
            
    if other:
        lines.append("## ❓ Others")
        lines.extend(other)
        lines.append("")
        
    return "\n".join(lines)

def main():
    repo_root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
    if not repo_root:
        print("Error: Not a git repository.")
        return

    commits = get_git_commits()
    parsed, other = parse_commits(commits)
    markdown = generate_markdown(parsed, other)
    
    changelog_path = os.path.join(repo_root, 'CHANGELOG.md')
    with open(changelog_path, 'w') as f:
        f.write(markdown)
    
    print(f"Changelog updated at {changelog_path}")

if __name__ == "__main__":
    main()
