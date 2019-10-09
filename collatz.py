dict = {}
def collatz(int):
 if int == 1:
     return 1

 if int in dict:
     return dict[int]
 if int%2 == 0:

     temp = 1 + collatz(int/2)
     dict[int] = temp
     return temp
 else:
     temp = 1 + collatz(3*int+1)
     dict[int] = temp
     return temp
num = -1
for i in range(1,int(input())):
    temp = collatz(i)
    if(temp>biggest):
        biggest = temp
        num = i

print(num)