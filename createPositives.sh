#!/usr/bin/env bash

for filename in pos/*.jpg; do
    echo $filename
    outFolder="info/${filename:4:${#filename}}"
    outFolder=${outFolder::-4}
    lstFile="$outFolder/lst"

    opencv_createsamples -img $filename -bg bg.txt -info $lstFile -pngoutput $outFolder -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1500 -h 50 -w 35
done