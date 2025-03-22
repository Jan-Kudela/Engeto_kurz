"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgenr@gmail.com
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

username = input("username: ")

if username in users:
    user_password = input("password: ")
    if username == "bob" and user_password == "123":
        print(f"Welcome to the app, {username}")
    elif username == "ann" and user_password == "pass123":
        print(f"Welcome to the app, {username}")
    elif username == "mike" and user_password == "password123":
        print(f"Welcome to the app, {username}")
    elif username == "liz" and user_password == "pass123":
        print(f"Welcome to the app, {username}")
    else:
        print("Wrong password.")

else:
    print("You are not registered.")


print("We have 3 texts to be analyzed.")
print("-" * 30)
text_numbers = ["1", "2", "3"]
choosen_number = (input("Enter a number btw. 1 and 3 to select: "))
if choosen_number not in text_numbers:
    print("You are out of range or you didn´t write a number.")

choosen_number = int(choosen_number)

choosen_text = TEXTS[choosen_number - 1]
#split_text = choosen_text.split(" ")
#choosen_text_clear = []
#for words in range(0,len(split_text)-1):
    #if split_text[words] != '':
        #choosen_text_clear.append(split_text[words])

#print(choosen_text_clear)
# choosen_text_clear
one_line = choosen_text.replace("\n","" )
one_line = one_line.replace("    "," ")
one_line_clear = one_line.replace(".","")
one_line_clear = one_line_clear.replace(",","")
choosen_text_list = one_line_clear.split(" ")
#print(choosen_text_list)
#print(len(choosen_text_list))
print(f"There are {len(choosen_text_list)} words in the selected text.")