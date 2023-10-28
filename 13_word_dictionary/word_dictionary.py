from PyDictionary import PyDictionary

def word_meaning():
    dictionary = PyDictionary()
    newLine = '\n*'
    while True:
        
        user_input = input("Please Enter a word to find meaning: ")
        try:
            meaning = dictionary.meaning(user_input)
            for key, value in meaning.items():
                print(f"{user_input}: '{key}'{newLine}{newLine.join(value)}")
        except Exception as e:
            print(f"{user_input}: has no meaning.")

        user_input = input("Do you want to have the meaning of another word (y/n)? ")
        if user_input.lower() == 'n':
            print("Thank you for using our application.To the next time.")
            break
        elif not user_input.lower() in 'yn':
            while not user_input.lower() in 'yn':
                user_input = input("Please enter (y/n) to continue: ")

word_meaning()
