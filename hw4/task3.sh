# remove "\r"
# step1--Extract passengers from 2nd class who embarked at Southampton.
#tr -d '\r' < titanic.csv | awk -F',' '$3 == 2' | grep ',S$' > titanic_filtered.csv
# step2--Then replace male/female labels with respectively M/F.
#sed 's/female/F/g; s/male/M/g' titanic_filtered.csv > titanic_replaced.csv
# step3--Finally, calculate the average age of the filtered passengers.
#awk -F',' '{if ($7 != "") sum += $7; count += ($7 != "")} END {if (count > 0) print "average age:", sum/count, "among", count, "passengers who have age info"; else print "No valid ages"}' titanic_replaced.csv

# a single pipeline of commands for all the tasks a, b, and c
tr -d '\r' < titanic.csv | awk -F',' '$3 == 2' | grep ',S$' | sed 's/female/F/g; s/male/M/g' | tee >(awk -F',' '{if ($7 != "") sum += $7; count += ($7 != "")} END {if (count > 0) print "average age:", sum/count, "among", count, "passengers who have age info"; else print "No valid ages"}')
