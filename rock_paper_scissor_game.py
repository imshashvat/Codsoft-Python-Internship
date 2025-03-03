import random
print("--------------------------------------------")
print("********************************************")
print("    》》》ROCK PAPER SCISSOR GAME《《《")
print("********************************************")
print("--------------------------------------------\n")
users_choice = input("Please choose between 'Rock' or 'Paper' or 'Scissor': ")
print(f"User's choice: {users_choice}")
options = ("Rock", "Paper" , "Scissor")
computers_choice = random.choice(options)
print(f"Computer's choice: {computers_choice}")
if users_choice == "Rock":
    if computers_choice == "Rock" :
            print("Match is Draw")
    elif computers_choice=="Paper":
        print("Oh!..You Lost.") 
    elif computers_choice=="Scissor":
        print("WOW!..You WON.")    
elif users_choice=="Paper":
    if computers_choice =="Rock" :
        print("WOW!..You WON.")   
    elif computers_choice=="Paper":
        print("This Match is DRAW!.") 
    elif computers_choice=="Scissor":
        print("Oh!..You Lost.") 
elif users_choice=="Scissor":
    if computers_choice =="Rock" :
        print("Oh!...You Lost.")   
    elif computers_choice=="Paper":
        print("WOW!...You WON.") 
    elif computers_choice=="Scissor":
        print("This Match is DRAW.")
else:
    print("Sorry!...Wrong Input.")    
print("Thanks for playing our game.")        
         