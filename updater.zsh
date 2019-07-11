#!/bin/zsh

while true; do
    git add data/fine.dat
    git add data/backup.dat
    git commit -m "updated data"

    git push

    sleep 1800;
done;

