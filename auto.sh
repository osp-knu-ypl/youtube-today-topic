#!/bin/bash

#echo "data now : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H)(h)"
vardate=" $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H)(h)"
echo $vardate

python3 ./data_processing/crawler.py KR
python3 ./data_processing/crawler.py US

