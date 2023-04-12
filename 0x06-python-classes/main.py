

class square:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def tell(self):
        print("hello {} your are {} year old".format(self.name,self.name))