quiz_dict = {
	1:{
		'question':"What is the capital of Tunisia?",
		'choices' : ["Bogota", "Maribu", "Tunis", "Riad"],
		'answer':2
	},
	2:{
		'question':"What is the color of and orange?",
		'choices' : ["Blue", "Red", "Green", "Yellow"],
		'answer':3		
	},
	3:{
		'question':"What kind of light the phone screen produce?",
		'choices' : ["Green", "Red", "Blue", "Yellow"],
		'answer':2		
	},
	4:{
		'question':"How many state there in USA?",
		'choices' : ["51", "32", "75", "40"],
		'answer':0		
	} 
}

def quiz():
    """
		App that produce question with choices and give the user
		the ability to return and answer
    """
    score = 0
    for (key, question) in quiz_dict.items():
        #print the question
        question_printing(key, question)
        #take the user choice
        user_choice = int(input("Please enter your answer: "))
        score = mark_user(user_choice, question, score)
    percentage = (score/len(quiz_dict)) * 100
    print_result(percentage)
        
def question_printing(key, question):
    """
		Print the question with its choices
    """
    print(f'Question {key}: {question["question"]} ')
    for (index, choice) in enumerate(question['choices']):
        print(f'{index + 1}: {choice} ')
        
def mark_user(user_choice, question, score):
    """
		Evaluate the user Choice and score his answer
    """
    if ((user_choice - 1) == question['answer']):
        score += 1
        print("Right answer")
    else:
        print("Wrong answer")
    print("\n")
    return score

def print_result(percentage):
    """
		Prints the results of the Quiz
    """
    print(f'You got {percentage}% as a score')
    if (percentage == 100):
        print("Congratulation you got the full mark.")
    elif 80<= percentage <100:
        print("You got and excelent score.")
    elif 60<= percentage <80:
        print("You got a good score")
    elif 50<= percentage < 60:
        print("You got the average.")
    else:
        print("You suck at quizez")

# Quiz execution
quiz()
