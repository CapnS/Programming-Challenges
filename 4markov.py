import random
import requests

r = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
words = r.text.split("\n")
markov = random.sample(words, 10)
chain = " ".join(markov)
print(chain)