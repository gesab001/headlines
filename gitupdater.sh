#!/usr/bin/env bash
cd /var/www/html/headlines/
sudo /usr/bin/git pull
sudo /usr/bin/git add .
sudo /usr/bin/git commit -m "updated xml"
sudo /usr/bin/git push --all
