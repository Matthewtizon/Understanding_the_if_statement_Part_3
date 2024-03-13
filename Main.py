# we will use def function of clear codes
def question():
    rules = input("You need to answer every question by typing yes or no do you understand? ")
    if rules != "yes":
        return print("try again")
    else:
        print("Next Question")

    question1 = input("Do you want to drink alcohol? ")
    if question1 != "yes":
        print("Okay will have water instead")
    else:
        print("Next Question")

    question2 = input("do you want to eat in a restaurant? ")
    if question2 != "yes":
        print("okay will have home made dinner instead")
    else:
        print("Next Question")

    question3 = input("Do you want to watch movie after me eat? ")
    if question3 != "yes":
        print("okay will have to play ml instead")


question()