import random
import re
class Markov(object):

    def __init__(self, read_file):
        self.cache = {}
        self.read_file = read_file
        self.words = self.getWordList()
        self.word_size = len(self.words)
        self.database()

    # def file_to_words(self):
    #     self.read_file.seek(0)
    #     data = self.read_file.read()
    #     words = data.split()
    #     return words

    def getWordList(self):
        wordlist = [word.lower() for word in re.findall(r"[\w']+", self.read_file.read())]
        return wordlist 

    def triples(self):
        
        if len(self.words) < 6:
            return

        for i in range(len(self.words)-5):
            yield (self.words[i], self.words[i+1], self.words[i+2],  self.words[i+3],  self.words[i+4], self.words[i+5])

    def database(self):
        for w1, w2, w3, w4, w5, w6 in self.triples():
            key = (w1, w2, w3, w4, w5)
            if key in self.cache:
                self.cache[key].append(w6)
            else:
                self.cache[key] = [w6]

    def generate_markov(self, size=25):
        seed = random.randint(0, self.word_size-6)
        seed_word, next_word, nexer_word, nexest_word, nexestest_word = self.words[seed], self.words[seed+1], self.words[seed+2], self.words[seed+3], self.words[seed+4]
        w1, w2, w3, w4, w5 = seed_word, next_word, nexer_word, nexest_word, nexestest_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2, w3, w4, w5 = w2, w3, w4, w5, random.choice(self.cache[(w1, w2, w3, w4, w5)])
        gen_words.append(w5)
        return ' '.join(gen_words)

if __name__ == "__main__":
    content = open("bible.txt", 'r')

    markov = Markov(content)
    print(markov.generate_markov())
    with  open("cache.txt", 'w') as cache_out:
        cache_out.write(str(markov.cache))