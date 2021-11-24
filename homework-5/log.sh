#!/bin/bash

{
    echo "Общее количество запросов:" 
    wc -l access.log | awk '{print $1}'
    echo

    echo "Общее количество запросов по типам:" 
    cat access.log | awk 'length($6)<=15 {print $6}' | cut -c 2- | sort | uniq -c 
    echo

    echo "Топ 10 самых частых запросов:"
    cat access.log | awk '{print $7}' | sort | uniq -c | sort -n -r | head -n 10
    echo

    echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:"
    cat access.log | awk '{print $9 " " $10 " " $1 " " $7}' | grep "^4" | sort -nk2 -r | head -n 5
    echo

    echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:"
    cat access.log | awk '{print $9 " " $1}' | grep "^5" | sort -nk1 -r | uniq -c | sort -nk1 -r | head -n 5
    echo

} >res_sh.txt 