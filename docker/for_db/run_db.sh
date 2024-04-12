#!/bin/bash

# 0. 설정값 가져오기
source ../../.env 


# 1. 기존 데이터 디렉토리가 호스트에 있는지 확인 (3단계에서 활용)
host_data_dir=$PROJECT_PATH/db/data_directory/$DB_CONTAINER

is_continuity=false
if [ -d "$host_data_dir" ]; then
    is_continuity=true
fi

echo " ---- 이전 데이터를 이어가나요? : $is_continuity"


# 2. 컨테이너 생성
docker run \
    --name $DB_CONTAINER \
    --hostname $DB_CONTAINER \
    -e POSTGRES_PASSWORD=$POSTGRES_PWD \
    -e TZ=Asia/Seoul \
    -p $DB_PORT:5432 \
    -v $host_data_dir:/var/lib/postgresql/data \
    -v $PROJECT_PATH/db/backup:/backup \
    -v $PROJECT_PATH/db/schema:/schema \
    -d \
    postgres 

sleep 10   # PC 성능이 좋으면 시간 줄여도 됨 (서버가 생성될 시간 확보)


# 3. 새롭게 생성되는 경우 유저와 DB 생성
if [ "$is_continuity" = false ]; then
    docker exec -i $DB_CONTAINER psql -U postgres \
        -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PWD';" \
        -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
fi


# 4. 버전 복원 지정
read -p " ---- 버전 복원 안 함(0), 스키마만 복원(1), 데이터 복원(2)를 선택하세요 : " choice

if [ "$choice" -ge 1  ]; then
    echo " ---- $CUR_SCHEMA 버전으로 스키마 복원중 ..."
    docker exec -it $DB_CONTAINER psql -U $DB_USER -d $DB_NAME -f schema/$CUR_SCHEMA
fi

if [ "$choice" -ge 2  ]; then
    echo " ---- $CUR_DUMP 버전으로 데이터 복원중 ..."
    docker exec -it $DB_CONTAINER pg_restore -U $DB_USER -d $DB_NAME backup/$CUR_DUMP
fi