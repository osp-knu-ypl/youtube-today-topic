#!/bin/bash

while :
do
	# echo "data now : $(date +%Y)-$(date +%m)-$(date +%d) $(date +%H)(h)"
	vardate="$(date +%Y)$(date +%m)$(date +%d)$(date +%H)"
	echo $vardate

	# support language pack countrycode / time / language pack

	python3 ./data_processing/crawler.py KR $vardate KR
	#python3 ./data_processing/crawler.py US $vardate en_core_web_sm
	#python3 ./data_processing/crawler.py ES $vardate es_core_news_sm
	#python3 ./data_processing/crawler.py FR $vardate fr_core_news_sm
	#python3 ./data_processing/crawler.py DE $vardate de_core_news_sm
	#python3 ./data_processing/crawler.py RU $vardate ru_core_news_sm
	#python3 ./data_processing/crawler.py IT $vardate it_core_news_sm
	#python3 ./data_processing/crawler.py GR $vardate el_core_news_sm
	#python3 ./data_processing/crawler.py CN $vardate zh_core_news_sm

	sleep 43200
done
