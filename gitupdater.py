#!/usr/bin/python3
import git

repo = git.Repo("/var/www/html/headlines")
assert not repo.bare
