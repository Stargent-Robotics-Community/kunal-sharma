num1 = int(input("Enter 1st integer:"))
num2 = int(input("Enter 2nd integer:"))
num3 = int(input("Enter 3rd integer:"))
num4 = int(input("Enter 4th integer:"))
num5 = int(input("Enter 5th integer:"))


integers= [num1, num2, num3, num4, num5]
i = 0
sum=0
while i<5:
    sum=sum+integers[i]
    i=i+1
print(sum) 