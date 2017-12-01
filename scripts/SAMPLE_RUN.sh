l#!/bin/bash

TRAINING_CORPUS="../data/all_features_included.dev"
GOLD_LEXICON="../data/all_features_included.all"
OUTPUT_DIR="../test_FAS/"

/usr/bin/python main.py -c "$TRAINING_CORPUS" -l "$GOLD_LEXICON" -o "$OUTPUT_DIR" -C ../config.ini
