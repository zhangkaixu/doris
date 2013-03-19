all: jump.txt

corpus=sina.news.txt
wordlist=high_freq.words


#count character unigrams
unigram.txt: ${corpus}
	./doris/unigram.py < ${corpus} > unigram.txt

jump.txt: unigram.txt
	./doris/word/jump.py --words ${wordlist} \
		--input ${corpus} --characters unigram.txt --output jump.txt

#count context
