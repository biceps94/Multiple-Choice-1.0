import time  #Adds "time" library in order to delay response

# CV information & Stuff to pull that'll be used in game
bio = {
    'name': 'Slobodan',
    'age': '25',
    'location': 'Zemun',
    'phone': '062 8371 375',
    'e-mail': 's.cvjeticanin94@gmail.com'
}

technical = {
    'SQL': 'Basic',
    'Python': 'Basic',
    'QA': 'Intermediate',
    'English': 'Fluent'
}

profile = ("Unfortunately experienced as a CSS agent.\nI'm looking to trade my soul for a QA testing job position")


KNinfo = ("Kuehne + Nagel / Belgrade / May - November (2018) ")
FBMinfo = ("First Beat Media  / Belgrade / (2017) September - May (2018)")
SINCRinfo = ("Quick mentions:  Sitel & NCR - 8 months of combined work experience ")


def bioinfo():
    print("Name:", bio['name'])
    time.sleep(1)
    print("Age:", bio['age'])
    time.sleep(1)
    print("Location:", bio['location'])
    time.sleep(1)
    print("Phone:", bio['phone'])
    time.sleep(1)
    print("E-mail:", bio['e-mail'])

def techinfo():
    print("My SQL knowledge is:", technical['SQL'],"\t\nI'm comfortable working with existing databases")
    time.sleep(1)
    print("My Python knowledge is:", technical['Python'], "\nI'm comfortable with making shitty multiple choice games")
    time.sleep(1)
    print("But like... I'd totally love to learn more")
    time.sleep(1)
    print("My knowledge of QA is:", technical['QA'], "\nI'm totally k, with writing/preforming test cases")
    time.sleep(1)
    print("My english language is:", technical['English'], "\nI am a god")



# --------------------------------------------------------------------------------------------------------------------



# Type of choice laid out for user

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

yes = ["Y", "y", "yes","yep","Yes"]
no = ["N", "n", "no", "No"]

required_ABC = ("\n Use only A, B, or C \n") # Restricts user by asking for a valid input
required_YN = ("\n Use only Yes/No \n") # Restricts user by asking for a valid input


# Plan:
# CV1 - 1 Choice // Done
# CV2 - 2 My CV Multiple Info // Done
# CV3 - Loop that breaks [virus]


instructions = """

Please select a choice when asked by typing in the following either one of listed letters:
\t* A
\t* B
\t* C
\t* Y/yes
\t* N/no

"""

# This is the function for a main menu

def main_menu():
    print("This is a simple python choice based game")
    time.sleep(2)
    print("It's been designed to show my amazing but totally basic knowledge of Python")
    time.sleep(2.5)
    print("It's also been designed to show you how your job as HR employee sucks")
    time.sleep(2.5)
    print("Lets start")
    time.sleep(1.5)
    print(f"Instructions on how to play the game: \t{instructions}")





# This is the function for introduction of the game.
time.sleep(1)
def start():
    print("You awake from sleeping at your desk")
    print("Your goal for the day is to find the perfect slave for a job at your company")
    time.sleep(2)
    print("Woah! An E-mail has just arrived")
    print(".... Oh great - Your co-worker just forwarded you 3 CVs \n They need you to review/select a candidate for interview")
    print("I guess it's time to choose one")
    print(""" A. CV1
B. CV2
C. CV3 """)
    choice = input(">> ")
    if choice in answer_A:
        option_cv1()
    elif choice in answer_B:
        option_cv2()
    elif choice in answer_C:
        option_cv3()
    else:
        print(required_ABC)
        start()


# This is the function for first choice in INTRODUCTION of the game
def option_cv1():
    print("You pick the first CV up for a review")
    print("However... \nYou immediately regret your decision")
    print("Why? - I don't know \n I'm actually just trying to get you to cv2 or cv3")
    print("Lets speed this up")
    print("""A. CV2
B. CV3""")
    choice = input(">> ")
    if choice in answer_A:
        option_cv2()
    elif choice in answer_B:
        option_cv3()
    else:
        print(required_ABC)
        option_cv1()




# This option is here to demonstrate the for/in function as well as create/write a notepad file
def option_cv2(file_name = "pwndfile.txt"):
    print("You pick the second CV up for a review")
    print("However... \n the CV is blank?")
    with open(file_name, "w+") as virus:
        for number in range(10):
            virus.write(f"Just writing a number {number + 1}")
        print("Finished writing numbers into a file")
        time.sleep(2)
        print("Please write anything you want in lines")
        line1 = input("Line 1. ")
        line2 = input("Line 2. ")
        line3 = input("Line 3. ")
        print("These will now be written into the file")
        virus.write(line1)
        virus.write("\n")
        virus.write(line2)
        virus.write("\n")
        virus.write(line3)
        time.sleep(1)
        print("Lines have been written into the file")
        virus.close()
        print("Continue with the game?")
        time.sleep(1)
        print("""A. Yes
B. No""")
        choice = input(">> ")
        if choice in yes:
            option_cv3()
        elif choice in no:
            print("Tough shit, you still gotta play, opening cv3")
            time.sleep(2)
            option_cv3()
        else:
            print(required_YN)
            option_cv2()



# This option is literally mixture of everything learned so far
def option_cv3():
    print("Opening CV3 - Literally the best one")
    time.sleep(1)
    bioinfo()
    print(f"{profile}")
    time.sleep(3)
    print("My technical abilities go something like this:")
    time.sleep(2)
    techinfo()
    print("For my work experience, just select which one you want to know about")
    print("""
A) Kuehne Nagel
B) First Beat Media
C) NCR & Sitel
""")
    choice = input (">> ")
    if choice in answer_A:
        kuehneinfo()
    elif choice in answer_B:
        fbminfo()
    elif choice in answer_C:
        ncrsitelinfo()
    else:
        print(required_ABC)
        option_cv3()

# --------------------------------------------------------------

# Def used for KN job choice
def kuehneinfo():
    print(f"{KNinfo}")
    time.sleep(2)
    print("- Day to day communication with the various government inport/export officials. ")
    time.sleep(2)
    print("- Tracking of containers/shippments & Overall logistic support.")
    time.sleep(2)
    print(" To continue, select: NCR/Sitel or First Beat Media ")
    time.sleep(2)
    print("""
A. NCR/Sitel
B. First Beat Media""")
    choice = input(">> ")
    if choice in answer_A:
        ncrsitelinfo()
    elif choice in answer_B:
        fbminfo()
    else:
        print(required_ABC)
        kuehneinfo()

#-----------------------------------------------------------


# Def used for NCR & Sitel job choice

def ncrsitelinfo():
    print(f"{SINCRinfo}")
    time.sleep(2)
    print("- Resolving potential customer escalations in a satisfactory manner.")
    time.sleep(2)
    print("- Providing technical support to Walmart and Sam’s Clubs employees. ")
    time.sleep(2)
    print("- Repairing of devices via FitNet, Cytrix, NetTop and Putty. ")
    time.sleep(2)
    print("- Creating docummentation for clients and work order for technicians.")
    time.sleep(2)
    print(" To continue, select: Kuehne Nagel or First Beat Media")
    time.sleep(2)
    print("""
A. Kuehne + Nagel
B. First Beat Media
""")
    choice = input(">> ")
    if choice in answer_A:
        kuehneinfo()
    elif choice in answer_B:
        fbminfo()
    else:
        print(required_ABC)

# ----------------------------------------------------------------




# Def used for FBM choice info
def fbminfo():
    print(f"{FBMinfo}")
    time.sleep(2)
    print("- Handling inbound customer chats, and e-mails. ")
    time.sleep(2)
    print("- Troubleshooting, and working with subscription and billing data. ")
    time.sleep(2)
    print(" For demonstration this option is currently considered to be a final one ")
    time.sleep(2)
    print(" Now you are given a option ")
    time.sleep(2)
    print(" Hire me? ")
    time.sleep(2)
    print("""
A. Yes
B. No""")
    finalchoice()


# ----------------------------------------------------------




# Loop used to fuck around with a boi
def finalchoice():
    choice = input(">> ")
    if choice in answer_A:
        print("Fuck yea boi")
    elif choice in answer_B:
        print("Hire me?")
        finalchoice()
    else:
        print(required_ABC)











# 1. Ako ostavim ovako kod, napravice fajl i ispisace 10 puta, ako ubacim negde virus.close() desice se ValueError
# 2. Ideja je sledeca:
# Opcija A)
# for number in range(10):
#     virus.write("just writing a number %d\r\n:" % (number+1))
#     if number in range(10) == 10:
#         virus.close()
    # -  Jedna stvar koja mi nije jasna je %d, ovo sam googlovao na netu za /write ali bi bilo kul da mi objasnis zasto dva puta % u virus.write
    # - Fora ovoga je nekako ubaciti if u for

# Opcija B)
# Nema opcije B, jednostavno se upucas i umres, jk da se napravi drugi def i nekako sa time da se igra, da se chejnuju





# virus.write("Just writing a number %d\r\n" % (number + 1))
# print("For demo purpose, you can write something in it")
# line1 = input("Line 1.: ")
# line2 = input("Line 2.: ")
# line3 = input("Line 3.: ")
# print("These will now be written into the file")
# virus.write(line1)
# virus.write("\n")
# virus.write(line2)
# virus.write("\n")
# virus.write(line3)
#  print("Closing the file")













main_menu()
start()




