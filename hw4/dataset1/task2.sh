#!/bin/bash

grep -l "sample" file* | xargs grep -o "CSC510" | uniq -c | grep -E '^[ ]*([3-9]|[0-9]{2,}) ' | cut -d: -f1 | \
sort | gawk '{print $2}' | xargs ls -l | sort -k5,5nr | gawk '{print $9}' | \
sed 's/file_/filtered_/'