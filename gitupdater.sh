#!/usr/bin/env bash
cd /var/www/html/headlines/ 
sudo git pull 
sudo git add . 
sudo  git commit -m "updated xml" 
sudo  git push --all
