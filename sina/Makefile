all: jump.txt

corpus=sina.news.txt
wordlist=high_freq.words

#count character unigrams
unigram.txt: ${corpus}
	./doris/unigram.py < ${corpus} > $@

jump.txt: unigram.txt
	./doris/word/jump.py --words ${wordlist} \
		--input ${corpus} --characters unigram.txt --output $@

#count context

jump21.txt : jump.txt
	./doris/word/jump21.py --words ${wordlist} --input ${corpus} --characters unigram.txt --output $@ --historyfile jump.txt --dl 1 --dr 0

jump12.txt : jump.txt
	./doris/word/jump21.py --words ${wordlist} --input ${corpus} --characters unigram.txt --output $@ --historyfile jump.txt --dl 0 --dr 1

jump22.txt : jump21.txt
	./doris/word/jump21.py --words ${wordlist} --input ${corpus} --characters unigram.txt --output $@ --historyfile jump21.txt --dl 0 --dr 1

jump13.txt : jump12.txt
	./doris/word/jump21.py --words ${wordlist} --input ${corpus} --characters unigram.txt --output $@ --historyfile jump12.txt --dl 0 --dr 1

jump31.txt : jump.txt
	./doris/word/jump21.py --words ${wordlist} --input ${corpus} --characters unigram.txt --output $@ --historyfile jump21.txt --dl 1 --dr 0
