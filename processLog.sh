#!/bin/bash

file=$RANDOM"_log"

cp log.txt $file

echo "]" >> $file

cat $file |python -mjson.tool |less
rm $file
