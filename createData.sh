#!/usr/bin/env bash

for folder in info/*/; do
    echo $folder
    vecFile="${folder}positives.vec"
    dataFolder=${folder:5:${#folder}}
    dataFolder="data/$dataFolder"

    if [ ! -d $dataFolder ]; then
        mkdir -p $dataFolder;
    fi

    opencv_traincascade -data $dataFolder -vec $vecFile -bg bg.txt -numPos 700 -numNeg 350 -numStages 15 -w 35 -h 50
done