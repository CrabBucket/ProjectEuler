list = []
import sys
def stringAdd(string,result):


    for i in range(len(string))[::-1]:

        temp = ord(string[i]) - 48

        result[i] = result[i] + temp
        if(result[i]>9 and i>0):
            result[i] = result[i] - 10
            result[i-1] += 1




    return result
for i in range(57):
    list.append(0)

for string in sys.stdin:
    if(string[0]=='#'):
        break
    string = "000000" + string
    print(string)
    list = stringAdd(string,list)


for x in list[4:14]:
    print(x,end='')