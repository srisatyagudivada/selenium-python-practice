print(list(range(5,10)))

print(list(range(10)))

#print only odd numbers from 1 to 10
print(list(range(1,10,2))) #2 indicates the increment 1, 1+2, 3+2 like that

#print only even numbers
print(list(range(0,10,2))) # 10 is ending point and it will not be printed
#print 1 to 10 in descending order
print(list(range(10,1,-1)))

print(list(range(-10,-5)))

print(list(range(-10,-5,2)))

#looping statements--while loop, for loop

#while loop--initialization, incrementation, condition

i=1#initialization
while i<=10: #condition
    print(i)
    i=i+1  # incrementation
    print("Done!!!")


# print 1 to 10 in descending order

i=10
while i>=1:
    print(i)
    i=i-1


# for loop : we can use range function where we can specify the starting point
# and ending point

#print 1 to 10 using for loop

for i in range(1,11):
    print(i)

# print 1 to 10 in decending order using for loop
for i in range(10,0,-1):
     print(i)

#print even numbers between1 to 20
for i in range(0, 21, 2):
    print(i)
#print odd numbers between1 to 20
for i in range(1, 20, 2):
    print(i)

#jumping statements-break & continue

for i in range(1,10):
    if i==5: # terminate the loop if it is 5
        break
    print(i)  # this will print 1.....9
print("program exited!!")


#continue

for i in range(1,10):
    if i==5:
     continue
    print(i)



