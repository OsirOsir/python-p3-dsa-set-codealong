class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        
        for i in enumerable:
            self.dictionary[i] = True
            
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self
    
    def __str__(self):
        elements = ','.join(map(str, self.dictionary.keys()))
        return f'MySet: {{{elements}}}'
    