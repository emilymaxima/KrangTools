#!/bin/sh
for file in $(ls -p | grep -v / | head -15000)
do
# Change this value
mv $file /dir/foo
done
