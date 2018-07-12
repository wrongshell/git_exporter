#!/usr/bin/env python

from git import Repo

r = Repo()
repo_branches = r.branches

print(repo_branches)

for branch in repo_branches:
    print(branch)
