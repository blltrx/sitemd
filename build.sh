#! /usr/bin/bash

filelist=$(ls -l content/*.md | awk '{print $9'})
for file in $filelist
do
    ./htmldown.py $file
done

./rss_build.py

git add .
git commit -m "new build commit"
echo "files comitted -> git push to publish"
# git push
