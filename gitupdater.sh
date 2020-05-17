#!/usr/bin/env bash
cd /var/www/html/headlines/
/usr/bin/git pull
/usr/bin/git add .
/usr/bin/git commit -m "updated xml"
/usr/bin/git push --all
