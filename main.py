import random as r

arr_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l']
arr_sign  = ['%','#','*','@','!']
size_pass = int(input("ENTER SIZE OF PASSWORD : "))
pass_str = ""
for i in range(size_pass):
   
    pass_str+=arr_alpha[r.randint(0,5)]+arr_sign[r.randint(0,4)]

print(f"PassWord is : {pass_str}")
