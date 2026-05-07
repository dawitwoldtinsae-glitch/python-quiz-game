import pandas as pd

quiz_questions=pd.read_csv('quizquestions.csv')

def choice_question(category_choices,level):
    """this function going to accept the user category choice then use random to choice the 5
    random question and return it"""
    filtered_question=quiz_questions.loc[(quiz_questions.level==level)&(quiz_questions.category==category_choices)]
    random_choice_questions=filtered_question.sample(n=5)
    list_of_choice_questions=random_choice_questions.to_dict(orient="records")
    return list_of_choice_questions
def ask_question(single_question,level):
    """this function going to display those random choice
    questions and their choice one by one,accept users answer compare
    it to the real answer and return true if it is correct or
    false if it is false"""
    print(single_question['question'])
    if level=='medium':
       i=1
       question_dictionary={single_question[f'option {i}']:'A',single_question[f'option {i+1}']:'B',
                                    single_question[f'option {i+2}']:'C',single_question[f'option {i+3}']:'D'}
       for i in range(1,5):
           print(f'{question_dictionary[f'{single_question[f'option {i}']}']}.{single_question[f'option {i}']}')
       user_answer=input("Choose the correct answer by writing the letter of your choice ").strip().lower()
       correct_answer=question_dictionary[f'{single_question['answer']}'].strip().lower()
       if correct_answer==user_answer:
           print("your answer is correct\n")
           return True
       else:
           print(f'your answer is wrong the correct answer is {correct_answer.upper()}')
           return False
    else:
        for i in range(1,5):
            if pd.notna(single_question[f'option {i}']):
                print(single_question[f'option {i}'])
        user_answer=input("enter your answer by word ")
        correct_answer=single_question['answer'].strip().lower()
        user_answer=user_answer.strip().lower()
        if correct_answer==user_answer:
            print("your answer is correct\n")
            return True
        else:
            print(f"wrong answer the answer is {correct_answer}\n")
            return False
def run_level(category,level):
    """this is the main function it loops through 5 question and call the functions
    update score"""
    score=0
    the_five_question=choice_question(category,level)
    for q in the_five_question:
        result=ask_question(q,level)
        if result:
            score+=1
    return score
def handle_level_results(category,level,score):
    """this function made to tell the user if he pass and fail and ask him about his next move"""
    if level=='easy':
        if score >=2:
            asker = input(f"you smashed it you got {score} out of 5.\n do you want to try next level 'yes' to try new category 'new' to stop anything ")
            asker = asker.strip().lower()
            if asker == 'yes':
                result2=run_level(category, 'medium')
                handle_level_results(category, 'medium', result2)
            elif asker=='new':
                restarter()
            else:
                print("thank you for your participation")
        else:
            asker = input("unfortunately you failed do you want to try again 'yes' for the same level and category"
                          " new for new category ")
            if asker == 'yes':
                result2=run_level(category, 'easy')
                handle_level_results(category, 'easy', result2)
            elif asker == 'new':
                restarter()
    elif level=='medium':
        if score >=3:
            asker = input("you smashed it.\n do you want to try next level 'yes' to try new category 'new' to stop anything ")
            asker = asker.strip().lower()
            if asker == 'yes':
                result2=run_level(category, 'hard')
                handle_level_results(category, 'hard', result2)
            elif asker=='new':
                restarter()
            else:
                print("thank you for your participation")
        else:
            asker = input("unfortunately you failed do you want to try again 'yes' for the same level and category"
                          "new for new category ")
            if asker == 'yes':
                result2=run_level(category, 'medium')
                handle_level_results(category, 'medium', result2)
            elif asker == 'new':
                restarter()
    elif level=='hard':
        if score >=4:
            asker = input("you smashed it.\n do you want to  try new category 'new' to stop anything ")
            asker = asker.strip().lower()
            if asker=='new':
                restarter()
            else:
                print("thank you for your participation and mastered the questions")
        else:
            asker = input("unfortunately you failed do you want to try again 'yes' for the same level and category"
                          "new for new category ")
            if asker == 'yes':
                result2=run_level(category, 'hard')
                handle_level_results(category, 'hard', result2)
            elif asker == 'new':
                restarter()
def restarter():
    while True:
        category_choices = input("what type of question do you want Astronomy or Programming: ")
        category_choices = category_choices.lower()
        if category_choices == 'astronomy':
            result1=run_level('astronomy', 'easy')
            handle_level_results('astronomy', 'easy', result1)
        elif category_choices == 'programming':
            result1=run_level('programming', 'easy')
            handle_level_results('programming', 'easy', result1)
        else:
            print("invalid input!!\n")
            continue
while True:
    category_choice=input("what type of question do you want Astronomy or Programming: ")
    category_choice=category_choice.strip().lower()

    if category_choice=='astronomy':
        result3=run_level('astronomy','easy')
        handle_level_results('astronomy','easy',result3)
        break
    elif category_choice=='programming':
       """this part is going to use for th astronomy part"""
       result3=run_level('programming','easy')
       handle_level_results('programming','easy',result3)
       #this part going to be for the random choice and call the function of asking question then when it finished it going to break
       break
    else:
        print("invalid input!!\n")
        continue


