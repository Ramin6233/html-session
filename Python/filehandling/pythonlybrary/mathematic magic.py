number= 200

print("number is : ",number)
digits=len(str(number))
print("digits is : ", digits)
result=0
temp=number
while temp>0:
    digit=temp%10
    result+-=digit**digits
    temp//=10
if number==result:
    print("number is armstrong")
else:
    print("number is not armstrong")

    