# input('hello , what is your name?')
print("hello, welcome to UII network")

name =input("what is your name ?\n")
print("hello "+ name + ", thank you so much for your coming in taday.\n\n\n")

menu =" Black Coffee, Espresso, Latte, Cappucino"

print(name + ", what would you like from our menu today? "
             "here is what we are serving \n " + menu)


Order =input()

price = 8

quantity =input("how many coffers would you like ?\n")

total =price * int(quantity)

print(total)
print("Thank you , your total is: $ " + str(total))

print("Sounds Great " + name + ", we'll have " + quantity + " "
      + Order+ " ready for you in a moment.")

