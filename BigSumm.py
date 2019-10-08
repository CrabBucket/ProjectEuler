git alist = []
for string in sys.stdin:
    list.append(string)


def stringAdd(string,result):
    index = len(string) - 1
    for char in string:
        temp = ord(char) - 48
        result[index] = result[index] + temp
        if(result[index]>9):
            result[index]
