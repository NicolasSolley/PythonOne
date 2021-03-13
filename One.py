character_name = "Nick"
character_age = 21

print("Hello, " + character_name + ". You are " + str(character_age) + " years old.")

character_name = "NICK"
print(character_name.isupper())  # isupper checks to see if the string is all uppercase
print(len(character_name))  # len means length
print(character_name[0])  # brackets can be used to find a specific character at specific index

character_name = "Nick"
print(character_name.index("i"))  # .index finds the specific index for a character in a string
print(character_name.replace("Nick", "Solley"))
print()
print(3 + 4.5)
print(3 * (4 + 3))  # Python follows order of operations
print()
print("Two integers addition calculator")
num1 = input("Enter first integer: ")
num2 = input("Enter second integer: ")
result = (int(num1) + int(num2))
print("Sum: " + str(result))
print()


def sayHello(user):  # Functions
    print("Hello, " + user)  # Function interior must all be indented


sayHello("Mike")

isMale = True
isTall = False

if isMale and isTall:
    print("Is male is true")
else:
    print("Is male is false")


def maxInt(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


num1 = input("Num1: ")
num2 = input("Num2: ")
num3 = input("Num3: ")

print(maxInt(num1, num2, num3))
