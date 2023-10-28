from PyDictionary import PyDictionary

def word_meaning():
    dictionary = PyDictionary()
    newLine = '\n* '
    while True:
        
        user_input = input("Please Enter a word to find meaning: ")
        print()
        try:
            meaning = dictionary.meaning(user_input)
            for key, value in meaning.items():
                print(f"{user_input.capitalize()}: '{key}'{newLine}{newLine.join(value)}")
                if (len(meaning) > 1):
                    print()
        except Exception as e:
            print(f"{user_input}: has no meaning.")

        user_input = input("\nDo you want to have the meaning of another word (y/n)? ")
        if user_input.lower() == 'n':
            print("\nThank you for using our application.To the next time.\n")
            break
        elif not user_input.lower() in 'yn':
            while not user_input.lower() in 'yn':
                user_input = input("Please enter (y/n) to continue: ")
        print()

word_meaning()
