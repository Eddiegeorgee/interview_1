numbers=[5,11,13,55,84,32,100,65,97,95,64,87,30,21,502]

# Even = int(numbers % 2) ==0
# Odd = int(numbers % 2) != 0

even=[]
odd=[]

for num in numbers:
    if num % 2 ==0:
        even.append(num)
    
    else:
        odd.append(num)

print(even)
print(odd)



