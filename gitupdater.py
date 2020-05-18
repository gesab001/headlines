#!/usr/bin/python
import git

repo = git.Repo("/var/www/html/headlines")
assert not repo.bare

git = repo.git
git.add(".")
git.commit("updated xml")
