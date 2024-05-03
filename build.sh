#! /usr/bin/bash

filelist=$(ls -l *.md | awk '{print $9'})
for file in $filelist
do
    ./htmldown.py $file
done

./rss_build.py

read -p "press any key to push to repo"
git add .
git commit -m "new build commit"
read -p "RSS FEED UPDATES: files comitted -> git push manually"
# git push
