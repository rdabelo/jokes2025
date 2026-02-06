
# Gael Martinez and Rodelo Abelo

# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
# question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
    # if question == "robbers":
    #     input("Knock Knock ")
    #     input("Calder")
    #     print("Calder police - I've been robbed!")
    #     joke = input("Do you want to hear another joke or are you finished? ")
    # elif question == "tanks":
    #     input("Knock Knock ")
    #     input("Tank ")
    #     input("You are welcome! ")
    #     joke = input("Do you want to hear another joke or are you finished? ")
    # elif question == "pencils":
    #     input("Knock Knock ")
    #     input("Broken pencil ")
    #     input("Nevermind, it's pointless! ")
    #     joke = input("Do you want to hear another joke or are you finished? ")(old code)

#If they respond no create loop with function that asks Please say yes to listen to the joke its super funny and do it until they dont say no anymore



# jokelist = ["robbers", "tanks", "pencils"]

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# elif joke == "yes":
#     print("Great, Let's Play")
# question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")





# def punch_line(category):
#         if category == "robbers":
#             input("Knock Knock ")
#             input("Calder ")
#             print("Calder police — I've been robbed!")
#         elif category == "tanks":
#             input("Knock Knock ")
#             input("Tank ")
#             print("You're welcome!")
#         elif category == "pencils":
#             input("Knock Knock ")
#             input("Broken pencil ")
#             print("Nevermind — it's pointless!")
# punch_line(question)
# while True:
#     def ask_continue():
#         return input("Do you want to hear another joke? (yes/no) ")
#     joke = ask_continue()
#     if joke == "yes":
#         question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#         punch_line(question)
#     else:
#         break
# joke == "finished"
# rate = int(input("Please rate our game 1-10! "))
# final_score = int(rate * 10)
# print(str(final_score) + " percent satisfaction rate")
# friend = input("Would you recommend this game to a friend? ")

# if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
# else:
#         print("Sorry you did not enjoy it. ")



# for item in jokelist:
#     if category == item:
#         print(jokes[item])
#         break
#     else:
#         print("That joke category doesn't exist. Let's remove it from the list!")
#     if category in jokelist:
#         jokelist.remove(category)  # list modification
#     else:
#         print("It wasn't in the list anyway.")

# punch_line(question)
# while True:
#     def ask_continue():
#         return input("Do you want to hear another joke? (yes/no) ")
#     joke = ask_continue()
#     if joke == "yes":
#         question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#         punch_line(question)
#     else:
#         break
# joke == "finished"
# rate = int(input("Please rate our game 1-10! "))
# final_score = int(rate * 10)
# print(str(final_score) + " percent satisfaction rate")
# friend = input("Would you recommend this game to a friend? ")

# if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
# else:
#         print("Sorry you did not enjoy it. ")



# jokelist = ["robbers", "tanks", "pencils"]


# jokes = {
#     "robbers": "Why did the robber steal a painting? ----> He's been framed!",
#     "tanks": "Why don't tanks ever get lost? ----> They always follow on a heavy path!",
#     "pencils": "What does a dull pencil and a glass hammer have in common ----> It has no point!"
# }

# def ask_continue():
#     return input("Do you want to hear another joke? (yes/no) ")


# def punch_line(category):
#     if category in jokes:
#         print(jokes[category])
#     else:
#         print("That joke category doesn't exist!")


# joke = input("Do you want to hear a joke? (yes/no) ")
# if joke == "no":
#     print("Okay suit yourself!")
# elif joke == "yes":
#     print("Great, let's play!")


# while jokelist:
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     for item in jokelist:
#         if question == item:
#             punch_line(question)        
#             jokelist.remove(item)       
#             break
#     else:
#         print("That joke category doesn't exist. Try again!")
    
#     if not jokelist:
#         print("No more joke categories left. Goodbye!")
#         break
#     elif ask_continue() != "yes":
#         print("Okay, no more jokes. Goodbye!")
#         break


# rate = int(input("Please rate our game 1-10! "))
# final_score = rate * 10
# print(f"{final_score} percent satisfaction rate")

# friend = input("Would you recommend this game to a friend? ")
# if friend == "yes" or friend == "maybe":
#     print("Thanks, we appreciate it.")
# else:
#     print("Sorry you did not enjoy it.")


jokelist = ["robbers", "tanks", "pencils"]

jokes = {
    "robbers": "Why did the robber steal a painting? ----> He's been framed!",
    "tanks": "Why don't tanks ever get lost? ----> They always follow on a heavy path!",
    "pencils": "What does a dull pencil and a glass hammer have in common ----> It has no point!"
}
def ask_continue():
    return input("Do you want to hear another joke? (yes/no) ")
def punch_line(category):
    if category in jokes:
        print(jokes[category])
    else:
        print("That joke category doesn't exist!")
def tell_joke(jokelist):
    print("Available joke categories:", jokelist)
    question = input("Which joke do you want to hear?")
    for item in jokelist:               
        if question == item:            
            punch_line(item)
            jokelist.remove(item)      
            return
    else:
        print("That joke category doesn't exist. Try again!")

joke = input("Do you want to hear a joke? (yes/no) ")
if joke == "no":
    print("Okay suit yourself!")
elif joke == "yes":
    print("Great, let's play!")

while jokelist:
    tell_joke(jokelist)

    if not jokelist:
        print("No more joke categories left. Goodbye!")
        break
    elif ask_continue() != "yes":
        print("Okay, no more jokes. Goodbye!")
        break

rate = int(input("Please rate our game 1-10! "))
final_score = rate * 10
print(f"{final_score} percent satisfaction rate")

friend = input("Would you recommend this game to a friend? ")
if friend == "yes":
    print("Thanks, we appreciate brotato chip.")
else:
    print("Sorry,go home.")