class RotationIterator:
    def __init__(self, data):
        self.data = data
        self.iterator = iter(self.data)
        self.position = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    
    def restart(self):
        self.iterator = iter(self.data)
        self.position = 0

    def get_index(self):
        return self.position
    
    def jump_to(self, index):
        return self.data[index]
