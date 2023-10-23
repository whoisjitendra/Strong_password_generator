# import random module to choose the random characters
import random

# all type characters are present here
Character_for_password="qazwsxedcrfvtgbyhnujmiklpoZXCVBNMLKJHGFDSAPOIUYTREWQ1234567890!@#$%^&*()~`?/.,\|"

# create a while loop 
while(True):
    Length_of_the_password=int(input("Enter the Length of the password->"))
    # create the empty string
    Store_the_password=""  
    for p in range(0,Length_of_the_password):
        
        Password_character=random.choice(Character_for_password)
        Store_the_password=Store_the_password+Password_character
    print("Password is generate:", Store_the_password)
    
    Repeat=input("Do you Continue this operation?(y/n):")        
    Output=Repeat.lower()
    if Repeat!="y":
        break
        
        
        