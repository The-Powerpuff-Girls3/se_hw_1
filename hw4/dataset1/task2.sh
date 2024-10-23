#!/bin/bash

grep -l "sample" file* | xargs grep -o "CSC510" | uniq -c | grep -E '^[ ]*([3-9]|[0-9]{2,}) ' | cut -d: -f1 | \
gawk '{print $1, $2}' | xargs -I {} sh -c 'count=$(echo "{}" | awk "{print \$1}"); file=$(echo "{}" | awk "{print \$2}"); size=$(stat -c%s "$file"); echo "$count $file $size"' | sort -k1,1nr -k3,3n | gawk '{print $2}' | \
sed 's/file_/filtered_/'