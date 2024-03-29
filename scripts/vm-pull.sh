#!/bin/bash
# Script by Adrian, if you're wondering

# To be executed in parent directory
if ! test -f "LICENSE"; then
    echo "License file not found in current directory. Canceling."
    exit
fi

rsync -aP --exclude={'data','__pycache__','.*'} eml4u@eml4u-experiment.cs.upb.de:/home/eml4u/EML4U/notebooks/ExplainingDriftTextEmbeddings/* ./
