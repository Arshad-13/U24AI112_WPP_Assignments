class decode:
    def __init__(self, message):
        self.message = message
        self.mapping = {str(i): chr(64+i) for i in range(1, 27)}
        self.combination = []
        
    def combinations(self, msg):
        temp1 = [i for i in msg]
        temp2 = []
        for i in range(len(temp1)):
            j = i + 1
            if(j > len(temp1)-1): return temp2
            z,y,x = temp1[j], temp1[i], temp1[i] + temp1[j]
            temp1[i] = x
            temp1.pop(j)
            temp2.append(temp1)
            print(temp2)
            temp1.insert(j, z)
            temp1[i] = y
        return temp2
    
    def display(self):
        pass
        v = self.combinations(self.message)
        print(v)
        
msg = "1112"
obj1 = decode(msg)
obj1.combinations(msg)
# obj1.display()
