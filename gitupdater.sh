#!/usr/bin/env bash
cd /var/www/html/headlines/ 
git pull 
git add . 
git commit -m "updated xml" 
git push --all
