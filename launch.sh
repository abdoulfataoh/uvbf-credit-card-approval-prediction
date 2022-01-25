#!/bin/bash
# swtich in git tag
echo "choose model for training (1/2):"
echo "enter 1 for logistic-regression"
echo "enter 2 for random-forest "
echo -n "your answer: "
read

# choose tag
case $REPLY in
1) echo "switching on logistic-regression model"
   git checkout logistic-regression-experiment
   TAG="logistic-regression-experiement" ;;
2) echo "switching on random-forest model"
   git checkout random-forest-experiment
   TAG="random-forest-experiment" ;;
*) echo "exited"; exit
esac

# clear screen
clear

# verbose
echo "switched on $TAG ....done"

# google drive info
echo -n "enter google drive id for data backup: "
read
dvc remote modify gdrive url gdrive://$REPLY

# launch 
dvc repro
dvc push