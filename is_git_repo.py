#!/usr/bin/env python3

# Imports
import os
import sys
import git
import subprocess

# Vars
workdir = sys.argv[-1]  # dir to work in (scan)

# Funcs

"""
from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(self.rorepo.working_tree_dir)
assert not repo.bare
"""


def is_git_repo(path="."):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


def is_git_directory(path="."):
    return (
        subprocess.call(
            ["git", "-C", path, "status"],
            stderr=subprocess.STDOUT,
            stdout=open(os.devnull, "w"),
        )
        == 0
    )


# Seems to be the best option (most reliable + gives the root of the project)
def get_git_root(path="."):
    """
    `None` if path is not in git repo, `{repo root dir path}` if it is."""
    if (
        subprocess.call(
            ["git", "branch"],
            stderr=subprocess.STDOUT,
            stdout=open(os.devnull, "w"),
            cwd=path,
        )
        != 0
    ):
        return None
    else:
        root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], cwd=path
        )
        return root.decode("utf-8").replace(
            "\n", ""
        )  # str(root).replace("b'", "").replace("\\n'", "")


# Check if any path has been given:
if len(sys.argv) == 1:
    sys.exit("You need to give path to dir!!!")

repo = get_git_root(workdir)
if repo is None:
    print("Couldn't find git repository here / in path!!!")  # <- print the path?
    # exit()
else:
    print(f"Found git repo at: {repo}")

print()

print("Is git repo:")
print(is_git_repo(workdir))
print(is_git_directory(workdir))
print(get_git_root(workdir))
