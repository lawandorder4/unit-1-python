# the error in the code ws that their wasnt no space "" so the code thinks its nothing so it wouldnt do nothing and jsut say its 0
text = "Hello, world, my name is"
count = 0

for char in text:
    #by adding a space in "" you are definging what you want to be counted that way the code knows what to count instead of nothing
    if char == " ":
       count += 1

print(count)


print("give me a number")
num = int(input())

for num in range(1, num):
    if num % 2 <= 0:
        print(num, "is even.")
    else:
        
        print(num, "is odd.")