def replace_word():
    str = "Hi gyes , i am chaith, and hi hi hi"
    print(f'Here is the sentence {str}')
    word_to_replace  = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()
