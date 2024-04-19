#! /usr/bin/bash

filelist=$(ls -l *.md | awk '{print $9'})
for file in $filelist
do
    ./htmldown.py $file
done
read -p "press any key to push to repo"
git add .
git commit -m "new build commit"
git push
