#! /usr/bin/env bash

filelist=$(ls -l content/*.md | awk '{print $9'})
for file in $filelist
do
    python htmldown.py $file -v
done

python rss_build.py

git add .
git commit -m "new build commit"
echo "files comitted -> git push to publish"
# git push
