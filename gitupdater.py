#!/usr/bin/python
import git

repo = git.Repo("/var/www/html/headlines")
assert not repo.bare

git = repo.git
git.pull()
git.add(".")
git.commit("-m", "updated xml")
