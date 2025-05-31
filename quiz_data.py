from questions import Question

quiz = [{
    "Question: " : "Where was the Patterson Gimlan bigfoot footage shot?",
    "Options" : ["A. Bakersfield" , "B. Fresno" , "C. Bluff Creek"],
    },

    { "Question: " : "What continent is the Mkele Mbembe native to?,",
      "Options" : ["A. Antarctica" , "B. South America" , "C. Africa"],
      },
    {"Question" : "Where is the Mothman from?",
     "Options" : ["A. West Virginia" , "B. Maryland" , "C. Oregon"],
    }]


questions = [
    Question(quiz[0], "C"),
    Question(quiz[1], "C"),
    Question(quiz[2], "A"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} correct.")

run_test(questions)