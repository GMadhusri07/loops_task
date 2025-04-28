#  1.take input number from user and print the factors of that number
number=int(input("enter a number :"))
print("the factors of",number,"are :")
for i in range(1, number + 1 ,1): 
    if number % i==0:  
        print(i)
        
# output :
# enter a number :33
# the factors of 33 are :
# 1
# 3
# 11
# 33

# ---------------------------------------------------------------------------------------------------------------------
# 2.print the tables from 1-5 with multiplying of even numbers

for i in range (1,6,1):
  print ("the table number is", i )
  for j in range(2,21,2):
    print(i, "X", j, "=", i*j)

# # OUTPUT :
# the table number is 1
# 1 X 2 = 2
# 1 X 4 = 4
# 1 X 6 = 6
# 1 X 8 = 8
# 1 X 10 = 10
# 1 X 12 = 12
# 1 X 14 = 14
# 1 X 16 = 16
# 1 X 18 = 18
# 1 X 20 = 20
# the table number is 2
# 2 X 2 = 4
# 2 X 4 = 8
# 2 X 6 = 12
# 2 X 8 = 16
# 2 X 10 = 20
# 2 X 12 = 24
# 2 X 14 = 28
# 2 X 16 = 32
# 2 X 18 = 36
# 2 X 20 = 40
# the table number is 3
# 3 X 2 = 6
# 3 X 4 = 12
# 3 X 6 = 18
# 3 X 8 = 24
# 3 X 10 = 30
# 3 X 12 = 36
# 3 X 14 = 42
# 3 X 16 = 48
# 3 X 18 = 54
# 3 X 20 = 60
# the table number is 4
# 4 X 2 = 8
# 4 X 4 = 16
# 4 X 6 = 24
# 4 X 8 = 32
# 4 X 10 = 40
# 4 X 12 = 48
# 4 X 14 = 56
# 4 X 16 = 64
# 4 X 18 = 72
# 4 X 20 = 80
# the table number is 5
# 5 X 2 = 10
# 5 X 4 = 20
# 5 X 6 = 30
# 5 X 8 = 40
# 5 X 10 = 50
# 5 X 12 = 60
# 5 X 14 = 70
# 5 X 16 = 80
# 5 X 18 = 90
# 5 X 20 = 100
