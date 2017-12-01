#!/bin/bash

TRAINING_CORPUS="../data/all_features_included.dev"
GOLD_LEXICON="../data/all_features_included.all"
OUTPUT_DIR="../test/"
CONFIG="../starter/config.ini"

/usr/bin/python ../starter/main.py -c $TRAINING_CORPUS -l $GOLD_LEXICON -o $OUTPUT_DIR -C $CONFIG
