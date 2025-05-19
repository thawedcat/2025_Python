import math
num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
add = num_1 + num_2
sub = num_1 - num_2
div = num_1 / num_2
mod = num_1 % num_2
mul = num_1 * num_2

print("addition :", add, "\n",
        "subtraction: ", sub , "\n",
        "multiplication: ", mul , "\n",
        "Modulus: ", mod, "\n",
        "Division: " , div, "\n")

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

print(num_1, num_2)
root_add = math.sqrt(num_1) + math.sqrt(num_2)
power = math.pow(num_1,num_2)
added_and_log = math.log10(num_1+num_2)

print("Suqure root and added :", root_add, "\n", "Number 1 powered by number 2 :", power, "\n", "Additional of 2 numbers and the based 10 logrithms of the sum :", added_and_log, "\n")

