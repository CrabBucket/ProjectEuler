class Node:
    def __eq__(self,node):
        if self.x==node.x and self.y==self.y:
            return True
        return False
    def __hash__(self):
        return hash((str(self.x)+" "+str(self.y)))
    def __str__():
        return str(x) + " " + str(y)
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.connections = []
width = int(input())
height = width
nodes = []
count = 0
sum = 0
for y in range(0,height+1):
    row = []
    for x in range(0,width+1):
        row.append(Node(x,y))
    nodes.append(row)

for x in range(width+1):
    for y in range(height+1):
        if y==1 and x == 0:
            continue
        if(x<width):
            nodes[y][x].connections.append(nodes[y][x+1])
        if(y<height):
            nodes[y][x].connections.append(nodes[y+1][x])
dict = {}
def traverse(node):
    global dict
    if str(node.x)+" "+str(node.y) in dict:
        return dict[str(node.x)+" "+str(node.y)]

    if node.y==height and node.x==height:
        dict[str(node.x)+" "+str(node.y)] = 1
        return 1
    if len(node.connections) > 1:
        temp = traverse(node.connections[0]) + traverse(node.connections[1])
    elif len(node.connections) == 1:
        temp = traverse(node.connections[0])
    else:
        return 0
    dict[str(node.x)+" "+str(node.y)] = temp
    return temp


print(2*traverse(nodes[0][0]))





