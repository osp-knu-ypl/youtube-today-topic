#!/bin/bash

#echo "data now : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H)(h)"
vardate=" $(date +%Y)$(date +%m)$(date +%d)$(date +%H)"
echo $vardate

python3 ./data_processing/crawler.py KR $vardate ko_core_news_sm
#python3 ./data_processing/crawler.py US $vardate en_core_web_sm

