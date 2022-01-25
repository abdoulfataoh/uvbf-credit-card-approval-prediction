#!/bin/bash
# script to auto swtich in git tag
echo "choose model for training (1/2):"
echo "enter 1 for logistic-regression"
echo "enter 2 for random-forest "
echo -n "your answer: "
read
echo "" 
case $REPLY in
1) echo "switching on logistic-regression model"
   git checkout logistic-regression-experiment ;;
2) echo "switching on random-forest model"
   git checkout random-forest-experiment ;;
*) echo "exited"; exit
esac