#Week 1 Homework Question 2 
#Author : Rishi Mehta (370655416)

#Script
amount = int(input("What amount do you want?"))
quarters = amount // 25 
amount = amount % 25
dimes = amount // 10 
amount = amount % 10
nickels = amount // 5
amount = amount % 5
pennies = amount


#To print, we use 
print("Quarters: " + str (quarters))
print("Dimes: " + str (dimes))
print("Nickels: " + str (nickels))
print("Pennies: " + str (pennies))

