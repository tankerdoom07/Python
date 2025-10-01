n= int(input("enter number : "))

fact = 1
for i in range(1, n+1):
    fact*=i

print(" factorial : " , fact)
def cal_sum(a , b):
    sum = a + b
    print (sum)
    return sum
cal_sum(20, 10)
