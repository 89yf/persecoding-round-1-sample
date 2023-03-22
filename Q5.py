#Q5
a = int(input())             
operator = input().strip()    
b = int(input())              

if operator == '+':
    result = a + b            
elif operator == '*':
    result = a * b           
else:
    print("Invalid operator")
    exit()                    #stops the program from continuing to execute when an invalid operator is entered

print(result)
