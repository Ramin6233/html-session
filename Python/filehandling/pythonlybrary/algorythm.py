def fun1(n):
    return n*(n+1)/2           #4x(4+1)/2=4x5/2=20/2=10
print(fun1(4))



def fun2(n):
    sum=0
    for i in range(1,n+1):     #1+2+3+4=10
        sum+=i
    return sum
print (fun2(4))


def fun3(n):
    sum=0
    for i in range(1,n+1):
        for i in range(1,i+1):   #1+(1+1)+(1+1+1)+(1+1+1+1)=1+2+3+4=10
            sum+=i

        return sum
    
    print(fun3(4))


    #Acitivity-2 #Iteration if number will be 1 for any point

    def fun4(n):
        sum=0
        for i in range(1,n+1):
            sum+=1
        return sum
    print(fun4(5))
