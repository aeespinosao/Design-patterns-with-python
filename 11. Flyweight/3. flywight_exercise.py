"""
Flyweight Coding Exercise
You are given a class called Sentence , which takes a string such as 'hello world'. You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in the sentence.
Typical use would be something like:
sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD
"""

class Sentence:
    
    class WordToken:
        def __init__(self, capitalize = False):
            self.capitalize = capitalize
    
    def __init__(self, plain_text):
        self.words = plain_text.split()
        self.tokens = {}
        
    def __getitem__(self, index):
        wt = self.WordToken()
        self.tokens[index] = wt
        return self.tokens[index]
        
    def __str__(self):
        return ' '.join([
            word.upper() if i in self.tokens and self.tokens[i].capitalize else word 
            for i, word in enumerate(self.words)
        ])