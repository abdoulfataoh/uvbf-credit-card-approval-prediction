#!/bin/bash
echo "enter google drive id for data backup: "
read
dvc remote modify gdrive url gdrive://$REPLY