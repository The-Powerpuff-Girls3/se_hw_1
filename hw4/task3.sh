# remove "\r"
tr -d '\r' < titanic.csv > titanic_cleaned.csv
# step1--Extract passengers from 2nd class who embarked at Southampton.
awk -F',' '$3 == 2' titanic_cleaned.csv | grep ',S$' > titanic_filtered.csv
# step2--Then replace male/female labels with respectively M/F.
sed 's/female/F/g; s/male/M/g' titanic_filtered.csv > titanic_replaced.csv
# step3--Finally, calculate the average age of the filtered passengers.
awk -F',' '{if ($7 != "") sum += $7; count += ($7 != "")} END {if (count > 0) print "average age:", sum/count, "among", count, "passengers who have age info"; else print "No valid ages"}' titanic_replaced.csv
