"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    '''Returns random words from a dictionary
    
    >>> WordFinder = WordFinder("words2.txt")
    6 words read

    >>> WordFinder.random() in ["#Veggies", "kale", "#Fruits", "parsnips", "apple", "mango"]
    True
    '''
    
    def __init__(self,path):
        '''Initiating variables and printing # of items in a file'''
        file = open(path)
        self.path = path
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")
        
    def __repr__(self):
        '''Represents the object that has been created'''
        return f"WordFinder = ('{self.path}')"
        
    def parse(self,file):
        '''Used to parse the file to a list of words'''
        return[w.strip() for w in file]
        
    def random(self):
        '''Returns a random word from file'''
        return choice(self.words)
    
    
class RandomWordFinder(WordFinder):
    '''Returns words without empyt spaces and that don't start "#"'''
    def parse(self, file):
        return [w.strip() for w in file if w.strip() and not w.startswith("#")]
    
    def __repr__(self):
        '''Represents the object that has been created'''
        return f"RandomWordFinder = ('{self.path}')"
    
    
