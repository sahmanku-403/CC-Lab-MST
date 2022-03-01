#Huffman Encoder and decoder
#implement trees

#=====ENCODER=====
#input string
#use dictionary
#sort in ascending order of frequency-1
#use first two elements to make a tree-2
#remove the first 2 elements and put this tree-1
#repeat 1 to 3 until size = 1
#use string to print encoding

#=====DECODER=====
#use encoded string and trees to decode
from collections import OrderedDict
class Node:
    def __init__(this, data=""):
        this.left = None
        this.right = None
        this.data = data
string = input("Enter string to encode: ")

#use dictionary
def encode(string):
    dict = {}
    k = 1
    for i in string:
        if i in dict:
            dict[i]= dict[i]+1
        else:
            dict[i] = 1
    while(len(dict)!=1):
        dict = OrderedDict(sorted(dict.items(), key = lambda x:x[1], reverse= True))
        item1 = dict.popitem()
        item2 = dict.popitem()
        node = Node(k)
        node.left = item1[0]
        node.right= item2[0]
        dict[node] = item1[1]+item2[1]
        k = k+1
    return node


code = ""
root = encode(string)
code_dict= {}
print("=======Encoding======")
def printcode(node, code=""):
    if isinstance(node, str):
        print(f'{node}= {code}',end="\n")
        code_dict[node] = code #why is this not giving error like code??
    else:
        if node.left:
            printcode(node.left, code+'0')
            
        if node.right:
            printcode(node.right, code+'1')
            

printcode(root, code)
output = ""
for i in string:
    output = output+code_dict[i]
print(f'encoded string: {output}')
print(f'length: {len(output)}')
print("======Decoding======")
def decode(output, node):
    root = node
    for i in output:
        if i is '0':
            node= node.left
        else:
            node = node.right
        if isinstance(node, str):
            print(node, end="")
            node = root
decode(output, root)
    
    
