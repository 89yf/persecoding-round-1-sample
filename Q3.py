#Q3

word = input()
result = word

while len(result) <= 30:       #while loop continues to execute the code repeatedly as long as the condition is true
    result += word             #word += word is the same as word = word + word

print(result)  


    #OR

    
word = input().strip()

while len(word) <= 30:
    word += word

print(word[:30])                #prints the 30 characters of the word
