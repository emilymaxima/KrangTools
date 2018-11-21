#!/bin/sh
for file in $(ls -p | grep -v / | head -15000)
do
mv $file </dir/foo>
done
