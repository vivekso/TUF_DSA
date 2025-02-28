class largetsElement:
    def __init__(self, arr):
        self.arr =  arr

    def largetsElementInArray(self):
        large = float('-inf')
        for i in self.arr:
            if i > large:
                large = i
        return large
    
arra = [1,3,4,5,6,78,12,12,34,9]
obj = largetsElement(arra)
print(obj.largetsElementInArray())