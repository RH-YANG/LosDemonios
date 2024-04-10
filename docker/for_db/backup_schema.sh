#!/bin/bash

source ../../.env 

current_date=$(date +"%y%m%d")

docker exec -it $DB_CONTAINER pg_dump -s -c -U $DB_USER -d $DB_NAME -f schema/$current_date.sql

echo "설정파일의 CUR_SCHEMA를 $current_date.sql으로 변경 하세요"