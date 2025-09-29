from pathlib import Path
import subprocess


def get_active_branch_name(wd=".")->str|None:
    """Return active branch name."""
    head_dir = Path(wd) / ".git" / "HEAD"
    with head_dir.open("r") as f: content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]
    return None


def get_git_commit_hash()->str|None:
    """Return git commit hash."""
    try:
        # Run git command in the notebooks directory
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd="..",  # Move up from folder to the repo root
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return None  # Not a git repository or error occurred
