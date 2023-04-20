class Tree:
    def __init__(self, value, code):
        #self.head = Node
        self.value = value
        self.code = code
        self.lNode = None
        self.rNode = None
 
    def insert(self, value, code):
        # for ind, val in enumerate(n.code):
        
        if code == "":
            self.value = value
        elif code[0] == "0":
            if self.lNode == None:
                self.lNode = Tree(-1, self.code+code[0])
            self.lNode.insert(value, code[1:])
 
        elif code[0] == "1":
            if self.rNode == None:
                self.rNode = Tree(-1, self.code+code[0])
            self.rNode.insert(value, code[1:])
 
        
    def get_level_values(self, c):
 
        if c == 0:
            return [self.lNode.value if self.lNode != None else -2, self.rNode.value if self.rNode != None else -2]
        else:
            return (Tree.get_level_values(self.lNode, c-1) if self.lNode != None else [-2]) + (Tree.get_level_values(self.rNode, c-1) if self.rNode != None else [-2])
 
    def print(self):
 
        for i in range(4):
            print(*self.get_level_values(i))
 
 
ZTree = Tree(-1, "0")
OTree = Tree(-1, "1")
d = [("А", "0010"), ("Б", "0011"), ("В", "000"), ("Д", "0100"), ("Е", "0101"), ("Ж", "111"), ("З", "0110"), ("И","101"), ("К", "100")]
for i in d:
    if i[1][0] == "0":
        ZTree.insert(i[0],i[1][1:])
    else:
        OTree.insert(i[0],i[1][1:])
 
ZTree.print()
 
print()
 
OTree.print()
