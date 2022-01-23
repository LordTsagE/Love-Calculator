# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_1 = name1.lower()
name_2 = name2.lower()
compatibility = 0
a = name_1.count("t")
b = name_1.count("r")
c = name_1.count("u")
d = name_1.count("e")
a1 = name_2.count("t")
b1 = name_2.count("r")
c1 = name_2.count("u")
d1 = name_2.count("e")
compatibility = a+b+c+d+a1+b1+c1+d1

compatibility2 = 0
a2 = name_1.count("l")
b2 = name_1.count("o")
c2 = name_1.count("v")
d2 = name_1.count("e")
a3 = name_2.count("l")
b3 = name_2.count("o")
c3 = name_2.count("v")
d3 = name_2.count("e")
compatibility2 = a2+b2+c2+d2+a3+b3+c3+d3

cp1 = str(compatibility)
cp2 = str(compatibility2)
compat = (cp1 + cp2)
compat_n = int(compat)
if compat_n <= 10 or compat_n >= 90:
  print(f"Your score is {compat_n}, you go together like coke and mentos.")
elif compat_n <= 50 and compat_n >= 40:
  print(f"Your score is {compat_n}, you are alright together.")
else:
  print(f"Your score is {compat_n}.")