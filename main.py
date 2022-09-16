# Gift Recommendation Program

print("Looking for a perfect Gift? We got you.")
account = input("Would you like to get started with building an account first? Yes/No :")

def verify_password(Password1, Password2):
    while True:
        if Password1 == Password2:
            print("Your password is correct")    # If the password entered both times is same then it is correct.
            break
        else:    # If the password entered both times is not same then it is incorrect.
            break
    return Password2
while account == "Yes":
    username = input("Enter a username:")
    Password1 = input("Enter your password:")    # User enters password
    Password2 = input("Enter your password again:")
    password = verify_password(Password1,Password2)
    if Password1 != Password2:
        print("Password is incorrect")
    else:
        break
else:
    print("Let's get started.")

gender=input("Is the receiver of the gift Male or Female?")
from functions import personalityType
print(personalityType())

from functions import TypeOfOccasion
print(TypeOfOccasion())

print("\n")
print("Types of Hobby")
print("1: Sports/Exercise, Traveling and Volunteering")
print("2: Traveling, Video-games and Going Out(Nightlife)")
print("3: Reading, Art and Music")
print("4: Cooking, Music and Writing")
choice = int(input("Choose a Hobby Type 1-4: "))

from functions import hobbyChoice
print(hobbyChoice(choice))
hobby = hobbyChoice(choice)
print("\n")
from functions import recommendation
print("The gift we recommend is", recommendation(gender,choice))
print("\n")

if gender == "Male":
    like = input("Are you satisfied with this gift? Yes/No: ")
    if like != "Yes":
        print("Here is another gift we chose", recommendation(gender,choice))
    else:
        print("Thank you for choosing us to find the perfect gift.")
else:
    like = input("Are you satisfied with this gift? Yes/No: ")
    if like != "Yes":
        print("Here is another gift we chose", recommendation(gender,choice))
    else:
        print("Thank you for choosing us to find the perfect gift.")


