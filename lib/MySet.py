class MySet:

    def __init__(self, enumarable = []):
        self.dictionary = {}
        for value in enumarable:
            self.dictionary[value] = True

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

    def __str__(self):
       dictionary_str = ','.join(map(str, sorted(self.dictionary)))
       return f'MySet: {{{dictionary_str}}}'
