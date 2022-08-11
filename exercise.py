# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

'''
input("enter a number: ")

num = int (input ("even number: "))
if (num % 2) == 0:
    print ("The number is even")
else:
    print ("The provided number is odd")

'''


#task2ex3

'''

x = int(input("enter a number of argument in range function: "))
if x >= 3:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))
    step = int(input("Choose a Step: "))
elif x == 2:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))
    step = 1
elif x >= -1:
    print("der user hat -1 eingegeben")
    start = 0
    stop = 10
    step = 1
else:
    start = 0
    stop = int(input("Stop number: "))
    step = 1


for n in range(start, stop, step):
  print(n)

'''
#task3ex3

'''

x = int(input("Enter a number: "))
for j in range(1,x+1,1):
    if x % j == 0:
        print(j)

'''

#task4es

# prime number: ein zahl die durch sich selbst oder
# durch einz teilbar ist.
# 

x = int(input("Enter a prime number: "))
for i in range(0,x):
    if x % i != 0:
        print(x)