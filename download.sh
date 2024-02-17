#!/bin/bash
if [ ! -d Apple ]; then
    curl -O https://cdn.intra.42.fr/document/document/17060/leaves.zip
    unzip leaves.zip
    mv images Apple
    rm leaves.zip
fi
