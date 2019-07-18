#!/usr/bin/env bash

for folder in info/*/; do
    echo $folder
    #outFolder="info/${filename:4:50}"
    #outFolder=${outFolder::-4}
    lstFile="$folder/lst"
    vecFile="$folder/positives.vec"

    opencv_createsamples -info $lstFile -num 800 -w 35 -h 50 -vec $vecFile
done