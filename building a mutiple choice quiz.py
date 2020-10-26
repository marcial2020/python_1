from Question import Question

question_prompts = [
     "What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n(d) Yellow\n\n",
     "What color are Bananas? \n(a) Yellow/Green\n(b) Violet\n(c) Black\n(d) Brown\n\n",
     "What color are Strawberries? \n(a) Blue/Yellow\n(b) Magenta\n(c) Orange\n(d) Red\n\n"
 ]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "a"),
     Question(question_prompts[2], "d")
 ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)