#!/bin/bash
basePath="./../../../../../kyle/Github/wordpress-scripts"

tail -n +2 "$basePath/posts.csv" | while IFS=, read -r fields_slug fields_excerpt; do
  echo $fields_slug
  echo $fields_excerpt
  # linearray=($line)
  # echo ${linearray[1]}

done