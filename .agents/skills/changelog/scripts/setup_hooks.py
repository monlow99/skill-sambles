import os
import subprocess
import stat

def install_hook():
    repo_root = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
    if not repo_root:
        print("Error: Not a git repository.")
        return

    hooks_dir = os.path.join(repo_root, '.git', 'hooks')
    post_commit_path = os.path.join(hooks_dir, 'post-commit')

    hook_content = f"""#!/bin/bash
# Automatically update CHANGELOG.md after a commit
# To avoid infinite loop, we check the commit message or use a flag

# Run the update script
python3 {repo_root}/.agents/skills/changelog/scripts/update_changelog.py

# Note: Amending here would trigger post-commit again. 
# A cleaner way is to stage it for the NEXT commit or use a specific workflow.
# For now, we just ensure the file is updated on disk.
"""

    with open(post_commit_path, 'w') as f:
        f.write(hook_content)

    # Make it executable
    st = os.stat(post_commit_path)
    os.chmod(post_commit_path, st.st_mode | stat.S_IEXEC)

    print(f"Post-commit hook installed at {post_commit_path}")

if __name__ == "__main__":
    install_hook()
