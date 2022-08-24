# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

"""


input("enter a number: ")


num = int (input ("even number: "))


if (num % 2) == 0:
    print ("The number is even")


else:
    print ("The provided number is odd")



"""


#task2ex3

"""

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

"""
#task3ex3

"""

x = int(input("Enter a number: "))


for j in range(1,x+1,1):
    if x % j == 0:
        print(j)

"""

#task4ex3

# prime number: ein zahl die durch sich selbst oder
#            durch einz teilbar ist.


"""


x = int(input("Enter a prime number: "))
s = True


for i in range(2,x):
    if x % i == 0:
        s = False


if s == True:
    print(x, "is a prime number")


else:
    print(x, "is not a prime number")


"""

#task5ex3

"""

for i in range(100):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

"""

#Task6ex3



from curses import def_shell_mode


for i in range(1000, 2001):

    if i % 7 == 0 and i % 5 != 0:
        print(i) 

text = "Berlin is a world city of culture, politics, media and science."
kj def_shell_mode ds 
d sd sd
 ds 
 sd
  