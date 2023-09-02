import random
a = ["rock","paper","scissor"]
b = None
c = random.choice(a)

while b not in a:
    b= input("select among [rock , paper , scissor]: \n")
user = print(f"you choose {b}")
computer = print(f"computer choose {c}")

if b == c:
    print("tie ! ")
elif b == "rock" and c == "scissor":
    print("you wins!! ")
elif b == "paper" and c == "rock":
    print("you wins!! ")
elif b == "scissor" and c == "paper":
    print("you wins!! ")
else:
    print("you loss !!")
    
print("Thank you for playing the game")
