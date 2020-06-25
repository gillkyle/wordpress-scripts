#!/bin/bash

# run by opening the WP shell from Local "Open Site Shell" and run with
# $ ./../../../../../kyle/Github/wordpress-scripts/shell/authors.sh

basePath="./../../../../../kyle/Github/wordpress-scripts/shell"

echo "Running import-posts script..."
echo
echo "Saving list of users to authors.txt to be able to reference IDs during post import"
wp user list > "${basePath}/authors.txt"

numAuthors=$(< "$basePath"/authors.txt wc -l)
echo "Saved ${numAuthors} authors successfully"

# # ID/0	user_login/1	display_name/2	user_email/3	user_registered/4	roles/5
# tail -n +2 "$basePath/authors.txt" | while read line; do
#   # echo ${line}
#   # echo ${linearray[1]}

#   # split the row text by space and save each column value into a new array
#   linearray=($line)
# done

# get author from text file for author ID 
authorName=AllanPooley
echo $authorName

authorId=$(awk -v author="$authorName" '{ if($2 == author) { print $1 } }' "$basePath/authors.txt")
echo $authorId