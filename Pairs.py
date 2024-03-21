'''
Team Contributions:
                    Bester: Worked on Chat.py
                    Ethan: Worked on main.py
                    Soham: Worked on  Pairs.py
                    Akshay: Worked on Pairs.py
'''



# List of pair groups
intents = {
    "GetHighLevelErrorCategory": {
        "targetRegex": "(.*)(yes|ya|yeah|affirmative|no|nope|negative|nada)(.*)",
        "targetGroup": 2,
        "rules": [
            (r"(.*)(yes|ya|yeah|affirmative)(.*)", ["Please provide the error type. (e.g. syntax error, io error, indentation, IO error, key error, name error)"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["Okay. at least that's out of the way. So what's the issue?", "So it's logical then i guess. So what's the issue"]),
            (r"(.*)an(.*)(issue)(.*)",["Are you getting any error?"]),
            (r"(.*)a(.*)(problem)(.*)",["Are you getting any error?"]),
            (r"(.*)(I)(.*)(not|nt|n't)(.*)(understand)(.*)", ["oh, let me try this way, is the program running?"]),
            (r"(.*)(Hi|Hello|Sup|Howdy)(.*)",["So are you getting any runtime or console error?"]),
            (r"(.*)(bye|see you later|adios)(.*)", ["Going so soon?", "Okay, Good bye!","Quack! Happy I could help","Oh Quack, did i make that bad of a first impression. Okay see you. I'll do better next time"]),
            (r"(.*)(its working|I figured it out!)(.*)", ["Great! Happy I could help", "Nice! Happy programming!"])
        ],
        "targetTranslator": [
            (r"(yes|ya|yeah|affirmative)", "Yes"),
            (r"(not|no|nope|negative|nada)", "No")
        ]
    },
    "GetLowLevelErrorCategory": {
        "targetRegex": "(.*)(name|type|syntax|attribute|indentation|io|key)(.*)",
        "targetGroup": 2,
        "rules": [
            (r"(.*)(attribute)(.*)(error)(.*)", ["Looks like you have an %2 error. You might be calling a method on the wrong type of object."]),
            (r"(.*)(syntax)(.*)", ["You might have forgotten the quotes around a string.",
                                       "You might have forgotten to put a colon at the end of a def/if/for line."]),
            (r"(.*)(type)(.*)", ["You might be trying to use an operator on the wrong type of object.",
                                     "An object you are using has a value of None.",
                                     "You might have used non-integer numbers in a list slice.",
                                     "You might have called a function/method with the wrong number or type of arguments."]),
            (r"(.*)(indentation)(.*)", ["You might have used a mixture of tabs and spaces.",
                                            "You might not have indented all lines in a block equally."]),
            (r"(.*)(name)(.*)", ["You might have misspelled the variable/function/method name.",
                                     "You might have forgotten to import a module.",
                                     "You might have forgotten to define a variable.",
                                     "You might be trying to call a function before it is defined.",
                                     "You might be trying to print a single word without the quotes."]),
            (r"(.*)(io)(.*)", ["You might be trying to open a file that doesn't exist."]),
            (r"(.*)(key)(.*)N", ["You might be trying to look up a key that does not exist in a dictionary."])
        ],
        "targetTranslator": [
            (r"(.*)(name)(.*)","name"),
            (r"(.*)(syntax)(.*)","syntax"),
            (r"(.*)(attribute)(.*)","attribute"),
            (r"(.*)(type)(.*)","type"),
            (r"(.*)(IO)(.*)","io"),
            (r"(.*)(key)(.*)","key"),
            (r"(.*)(indentation)(.*)","indentation")
        ]
    },
    "SyntaxErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "AttributeErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "NameErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "KeyErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "IOErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "TypeErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "IndentationErrors": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(not|n't|nt)(.*)(working)", ["too bad! Tell me more then. Whats happening now?"]),
            (r"(.*)(not|no|nope|negative|nada)(.*)", ["too bad! Tell me more then. Whats happening"]),
            ("(.*)", ["Quack! is it working now?"])
        ],
        "targetTranslator": []
    },
    "logicalError": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)I(.*)try(.*)to (.*)", ["Okay. So your trying to %4. What have you done so far?"]),
            (r"(.*)I(.*)to (.*)", ["Okay. You want it to %3. What have you done so far"]),
            (r"(.*)I(.*)am (.*)", ["Okay. Interesting. So %3. What have you done so far"]),
            (r"(.*)(yes|ya|yeah|affirmative)(.*)", ["Okay, great!. What else?","Nice. Tell me more. Tell me everything"]),
            (r"(.*)just(.*)not(.*)working", ["I apologise. That must be frustrating. Let me try to help you. tell me more..."]),
            (r"(.*)(have|'ve) (.*)", ["Okay. You have %3. can you confirm thats working?"]),
            (r"(.*)if(.*)", ["Interseting, what comparision did you use?"]),
            (r"(.*)(two numbers)(.*)(equal)(.*)(or not)", ["You are comapring a number with a string representation of a number (eg if 3 == '3')"]),
            (r"(.*)(condition)(.*)(not giving|not getting)(.*)(expected result|correct answer)", ["The order of precedence in the condition is ambiguous 'add' some parentheses"]),
            (r"(.*)(related|issue)(.*)(loop|loops)(.*)", ["Got it. Can you explain what exactly the issue is?"]),
            (r"(.*)Loop(.*)(range|range function)(.*)(missing last value|misses last value)", ["The range function is exclusive at the finish. Please increase it by one."]),
            (r"(.*)i'm trying(.*)(multiple lines|many lines of code|many lines)(.*)(but)(.*)(getting a single one|displaying one)", ["YOu have opened the file inside the loop move it outside."]),
            (r"(.*)loop(.*)(multiple strings|collection of strings)(.*)(individual characters)", ["You are iterating over a string by mistake."]),
            (r"(.*)variable (.*) (should contain value|must store value)(.*)(do not contains|not storing)", ["Alright, you are storing the return value of a function which changes the variable soon (eg. sorting)"]),
            (r"(.*)(trying to print|asking to get)(.*)(value)(.*)(instead|but)(.*)(weird string|different output)", ["You are putting an object (e.g a FileObject) when you want the result of calling a mrthod on the object."]),
            (r"(.*)number(.*)(should be a fraction|is a fraction)(.*)(displaing as|coming out as|printing as)(.*)(zero|zero in Python 2)", ["You are dividing integers rather than floats. Convertthe numbers to floats or from _future_ import division"]),
            (r"(.*)reading(.*)file(.*)but getting no input", ["You have already read the contents of file earlier in the code. So the cursor is at the end."])
        ],
        "targetTranslator": []
    },
    "courtesyGreeting": {
        "regex": "",
        "rules": [

        ],
        "targetTranslator": []
    },
    "generalConversation": {
        "targetRegex": "",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(hello|hi|hey)(.*)", ["Hi there!", "Hello!", "Hey!"]),
            (r"(.*)(good)(.*)(morning)(.*)", ["Good morning! How can I help you today?", "Good morning! What's on your mind?"]),
            (r"(.*)(good)(.*)(afternoon)(.*)", ["Good afternoon! How can I help you today?", "Good afternoon! What's on your mind?"]),
            (r"(.*)(good)(.*)(evening)(.*)", ["Good evening! How can I help you today?", "Good evening! What's on your mind?"]),
            (r"(.*)(help)(.*)(me)(.*)", ["Of course! What do you need assistance with?", "Absolutely, I'm here to help. What do you need?"]),
            (r"(.*)what(.*)you(.*)think(.*)about (.*)", ["Well, it depends on the context. Can you give me more information?",
                                                         "It's hard to say without more context. Can you tell me more about it?"]),
            (r"(.*)why isn't my code working(.*)", ["Let's take a look. Can you provide some more details about the issue you're experiencing?",
                                            "Hmm, that's a good question. Can you give me more information about what's happening?"]),
            (r"(.*)how(.*)I(.*)solve(.*)problem(.*)", ["Here are some possible solutions: (provide solutions)",
                                                       "Let's explore some possible solutions together. Can you give me more information about the problem?"]),
            (r"(.*)what(.*)best(.*)approach (for|to) (.*)", ["Sorry, I'm not quite sure. Have you tried my super brother chat GPT"]),
            (r"(.*)(thank you)(.*)", ["You're welcome! Let me know if you need anything else.", "No problem, happy to help."]),
            (r"(.*)thanks(.*)", ["You're welcome! Let me know if you need anything else.", "No problem, happy to help."]),
            (r"(.*)(much appreciated)(.*)", ["You're welcome! Let me know if you need anything else.", "No problem, happy to help."]),
            (r"(.*)(bye|see you later|adios)(.*)", ["Going so soon?", "Okay, Good bye!", "Quack! Happy i could help"]),
            (r"(.*)(its working|I figured it out)(.*)", ["Great! have a great day!", "Nice. Happy programming"]),
            ("(Hi|Hello|Sup|Howdy)", ["Hello", "Howdy!"]),
            ("(How are you|u good)", ["I'm fine how are you."]),
            ("(Error|not working) (.*)", ["That sounds serious. Walk me through what you have done so far"]),
            ("(.*) you (.*) me(.*)", ["Why do you think I %2 you"]),
            ("(.*)", ["Tell me more...", "A little bit more please...", "Interesting..."]),
            (r"(.*)(yes|ya|yeah|affirmative)(.*)", ["Please provide the error type. (e.g. syntax error, type error, value error, indentation, IO error, key error, name error)"]),
            (r"(.*)(no|nope|negative|nada)(.*)", ["Interesting. So how can I help you then?"]),
            (r"(I)(.*)(help|figure out|figure|understand)(.*)", ["Okay, tell me more..."]),
            (r"(.*)I(.*)try(.*)to (.*)", ["Yipee! Interesting. So your trying to %4. What have you done so far?"]),
            (r"(.*)(I)(.*)(ve)(.*)", ["Okay, and can you confirm that has worked?"]),
            (r"(.*)error message(.*)", ["Please provide the error type. (e.g. syntax error, type error, value error, indentation, IO error, key error, name error)"]),
            (r"(.*)(an)(.*)(error|issue|exception)(.*)", ["Can you please describe the %4 you are facing?","What error are you facing", "What's the name of the error"]), #
            (r"(.*)(a)(.*)(bug|problem)", ["Please explain the %4 you're encountering, and I'll try to help."]),
            # (r"(.*) exception", ["It looks like you're facing an exception. Can you share the traceback or error message?"]),
            (r"the error is (.*)", ["Got it. Let's analyze the error: %1. What do you think might be causing this?"]),
            (r"i think it might be (.*)", ["Interesting, why do you think %1 might be causing the problem?"]),
            (r"(.*)not sure(.*)", ["That's okay. Let's try to narrow it down. What part of your code do you think could be causing the issue?"]),
            (r"the issue is in (.*)", ["What is the purpose of %1 in your code? Can you explain what it's supposed to do?"]),
            (r"(.*)is supposed to(.*)", ["Alright. Can you walk me through the logic of how %1 is supposed to %2?"]),
            (r"how can i test (.*)", ["You can test {} by writing unit tests or integration tests, depending on the scope. Consider using a testing framework, such as `unittest` or `pytest`, to structure your tests."]),
            (r"how do i write unit tests", ["To write unit tests, start by identifying the smallest units of your code, such as functions or methods. Write test cases that cover different inputs and edge cases, and use a testing framework like `unittest` or `pytest` to help manage and run your tests."]),
            (r"my code is working, but the output is not correct", ["Try to isolate the part of your code that produces the incorrect output. Examine the logic, input values, and any intermediate results. Also, ensure that your code handles edge cases correctly."]),
            (r"how do i use a debugger", ["To use a debugger, set breakpoints in your code where you want to pause execution, then step through the code line-by-line, inspecting variables and evaluating expressions as needed. In Python, you can use the built-in `pdb` debugger or an IDE with debugging support, like PyCharm."]),
            (r"how do i read a traceback", ["To read a traceback, start at the bottom, where the error message is displayed. Then, follow the traceback upwards to see the chain of function calls that led to the error. This can help you identify where the problem originated in your code."]),
            (r"i need help with multithreading", ["What specifically do you need help with regarding multithreading? Are you having trouble understanding the concept or implementing it in your code?"]),
            (r"how do i profile my code", ["To profile your code, use a profiling tool like `cProfile` or `py-spy` to measure the execution time of your code and identify performance bottlenecks. Analyze the profiling results to find areas of your code that can be optimized."]),
            (r"how do i parse (.*)", ["To parse {}, you can use built-in functions, regular expressions, or external libraries, depending on the format and complexity. For example, you can use `json` for JSON, `xml.etree.ElementTree` for XML, or `BeautifulSoup` for HTML."]),
            (r"how do i convert (.*) to (.*)", ["To convert {} to {}, consider using built-in functions, external libraries, or writing custom conversion functions. Please provide more information about the data types or formats you're working with so I can provide more specific guidance."]),
            (r"how do i prevent (.*)", ["To prevent {}, it's important to understand the root cause and apply best practices, such as input validation, proper error handling, and secure coding practices. Can you provide more information about the specific issue or vulnerability you're concerned about?"])
        ],
        "targetTranslator": []
    },
    "bye": {
        "targetRegex": r"(.*)(bye|its working)(.*))(.*)",
        "targetGroup": 0,
        "rules": [
            (r"(.*)(bye|its working)(.*)", ["Happy I could be of help", "See you next time!", "It was a pleasure speaking to you"])
        ],
        "targetTranslator": []
    }
}