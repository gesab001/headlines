#!/usr/bin/python
import git

repo = git.Repo("/var/www/html/headlines")
assert not repo.bare

git = repo.git
git.pull()
git.add(".")
repo.commit('updated xml')
