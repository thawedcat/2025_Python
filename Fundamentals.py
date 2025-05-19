name = input("Enter the name: ")
age = int(input("Enter the age: "))
is_married = (input("Is he or she married? : "))
is_married = is_married.lower

if is_married == "yes":
    is_married = True
else :
    is_married = False

if is_married is True : 
    phrase = (name.capitalize() + " is " + str(age) + " years old and is married")
    print("length in character \n: "+ str(len(phrase)))
    print(phrase)
elif is_married is False : 
    phrase = (name.capitalize() + " is " + str(age) + " years old and is single")
    print("length in character \n: "+ str(len(phrase)))
    print(phrase)
else:
    print("unexpected error.")

