"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start=0):
        '''Makes a new generator starting at input start value'''
        self.next = start
        self.start = self.next
        
    def __repr__(self):
        '''Representation'''
        return f'Start serial = {self.start}'
        
    def generate(self):
        '''Return next generated number'''
        self.next += 1
        return self.next -1

    def reset(self):
        '''Resets to original start'''
        self.next = self.start
