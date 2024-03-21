'''
Team Contributions:
                    Bester: Worked on Chat.py
                    Ethan: Worked on main.py
                    Soham: Worked on  Pairs.py
                    Akshay: Worked on Pairs.py
'''
from Chat import Chat

# representation of flow chart to define sequence of information and decision rules
objectiveSequence = [
    ("root","",""),
    ("GetHighLevelErrorCategory","root",""),
    ("GetLowLevelErrorCategory","GetHighLevelErrorCategory","yes"),
    ("logicalError","GetHighLevelErrorCategory","no"),
    ("SyntaxErrors","GetLowLevelErrorCategory","syntax"),
    ("AttributeErrors","GetLowLevelErrorCategory","attribute"),
    ("KeyErrors","GetLowLevelErrorCategory","key"),
    ("TypeErrors","GetLowLevelErrorCategory","type"),
    ("IOErrors","GetLowLevelErrorCategory","io"),
    ("NameErrors","GetLowLevelErrorCategory","name")
]
# Method to get child given parent and decision value
def getChild(parent, branch):
    for x in objectiveSequence:
        if x[1].lower() == parent.lower():
            if x[2].lower() == branch.lower():
                return x[0]

    return parent

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("<------- Rubber Duck Chatbot ------->")
    print("Type 'quit' to end the conversation.")
    print("")
    print("Hi there. I am a rubber duck debugging chatbot. So to begin with, are you getting a runtime or console error?")

    chat = Chat({"###":"###"})

    obj = "root"
    targetVal = ""
    # conversation loop
    while True:
        # initialise variables including initial objective
        finish = False
        obj = getChild(obj, targetVal)
        objmet = False

        # check if user entered quit and exit
        if finish:
            break

        # loop until initial objective met e.g. get response for error type you can understand based on defined rules
        while not objmet:
            user_input = input("> ")
            # check if user typed quit
            if (user_input.lower() == "quit"):
                finish = True
                break
            # process input. Get response, whether objective has been met and target value for use in decision flow chart
            response, objmet, targetVal = chat.respond(obj, user_input)
            if targetVal != "":
                # translate
                targetVal = chat.translateTarget(targetVal, obj)
                pass
            if response:
                print(response)
            else:
                print("I am not sure if I understand.")  # default response

        if finish:
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


