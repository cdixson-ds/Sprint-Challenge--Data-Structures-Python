
class RingBuffer():
    def __init__(self, capacity):
        self.data = []
        self.capacity =capacity

    def append(self, x):
        if len(self.data) == self.capacity:
            self.current=0
            self.data[self.current] = x
            self.current=(self.current+1)%self.capacity
            self.__class__=bufferfull
        else:
            self.data.append(x)

    def get(self):
        if self.data is None:
            return []
        else:
            return self.data

class bufferfull:
    def append(self,x):
            if len(self.data)<self.capacity:
                    self.data.insert(self.current, x)
            else:
                    self.data[self.current]=x
            self.current=(self.current+1)%self.capacity

    def remove(self,x):
            if self.data:
                    if self.current>len(self.data):
                            self.current=0
                    self.data.pop(self.current)

    def get(self):
        if self.data is None:
            return []
        else:
            return self.data

# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']
