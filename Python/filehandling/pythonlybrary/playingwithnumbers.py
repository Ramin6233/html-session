number= int(input("enterr a number : "))
original_num=0
while number>0:
    digit=number%10
    reverse_num=reverse_num*10+digit
    number//=10
if original_num ==reverse_num:
    print("number is palindrome")
    print("reverse number is : ", reverse_num)
    print("original number is : ", original_num)
else:
    print("number is not palindrome")






    largest_num= int(input("enter a largest number : "))
    smallest_num= int(input("enter a smallest number : "))
    while (smallest_num):
        numberStore=smallest_num
        smallest_num=largest_num%smallest_num
        largest_num=numberStore
    print("GCD is : ", largest_num)
    print("HCF is : ", largest_num)



