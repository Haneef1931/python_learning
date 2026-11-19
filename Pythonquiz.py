def check_answer(question, option, correct_answer):
    """ Function to ask a question, display the option, and check user's answers"""

    print("\n"+question)
    for option in option:
        print(option)
        # Get the  user input
        user_input = input("\nEnter your option (A\B\C\D): ").strip().upper()

        # Check the user's answer against the correct answer
        if user_input == correct_answer:
            print("\nCorrect Answer!")
            return 1
        else:
            print("\nWrong answer! Correct option is {Correst answer }")
            return 0


def run_quiz():
    """Main function to run quiz """

    print("\nWELCOME TO THE PYTHON  QUIZ GAME")
    print("\nAnswer the follwing  5 question ")

    # Initialize score to 0
    score = 0

    # Display the five questions and update th score

    score += check_answer("1. what is the capital of France?",
                          ['A. Berlin', 'B. Mumbia', 'C. Paris' 'D. Sdney'],
                          'C')

    score += check_answer("2. Which keyword is used in Python to describe a function?",
                          ['A. func', 'B. def  ', 'C. fun ' 'D. function'],
                          'B')

    score += check_answer("What is the output of print(2+3*2)?",
                          ['A. 10', 'B. 8 ', 'C. 12 ' 'D. 7'],
                          'A')

    score += check_answer("Which planet is known as the red planet?",
                          ['A.Earth ', 'B.Venus   ', 'C.Mercury  ' 'D.Mars  '],
                          'D')

    score += check_answer("What is the planet giving us heat ",
                          ['A.Sun', 'B.Sun   ', 'C.Uranus ' 'D.Neptune  '],
                          'B')

    score += check_answer( "How many moons does the Earth have?",
                              ['A.1', 'B.50   ', 'C.5 ' 'D.8  '],
                              'A')
    

