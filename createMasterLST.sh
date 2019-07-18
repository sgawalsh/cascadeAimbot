#!/usr/bin/env bash

if [[ ! -e /info/lst ]]; then
    mkdir -p /info
    touch /info/lst
fi

> info/lst

for folder in info/*/; do
    echo $folder
    lstFile="${folder}lst"
    echo $lstFile
    number=${folder:5:${#folder}}
    echo $number

    cat $lstFile | while read line
    do
        echo "${number}$line" >> info/lst
    done
done