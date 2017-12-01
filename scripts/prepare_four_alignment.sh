#!/bin/bash

TRAINING_CORPUS="../data/all_features_included.dev"
GOLD_LEXICON="../data/all_features_included.all"
CONFIG="../starter/config.ini"
TIME=20000

# change training time
sed -i "/maxtime=/ c maxtime=$TIME" $CONFIG

RES_PATH="../experiments_res/"
MODEL=("FAS" "ref-comp" "word-comp" "no-comp")
ELEMENTS=${#MODEL[@]}

for (( i=0;i<$ELEMENTS;i++)); do
	echo ${MODEL[${i}]}
	sed -i "/alignment-method=/ c alignment-method=${i}" $CONFIG
	cat $CONFIG | grep alignment-method=
	OUTPUT_DIR="$RES_PATH${MODEL[${i}]}"
	/usr/bin/python ../starter/main.py -c $TRAINING_CORPUS -l $GOLD_LEXICON -o $OUTPUT_DIR -C $CONFIG
	/usr/bin/python plot_freq.py $OUTPUT_DIR

done
# plot_graphs.py requires SEABORN package 
/usr/bin/python plot_graphs.py $RES_PATH $TIME
