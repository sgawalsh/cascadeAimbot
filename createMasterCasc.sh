#!/usr/bin/env bash

if [ ! -d data/master ]; then
    mkdir -p data/master;
fi

opencv_traincascade -data data/master/ -vec info/masterVec.vec -bg bg.txt -numPos 2000 -numNeg 1000 -numStages 20 -w 35 -h 50