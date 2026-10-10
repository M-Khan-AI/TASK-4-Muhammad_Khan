"""A simple general knowledge quiz with score calculation."""

questions = [
    ("What is the capital of France?", ["paris"]),
    ("Which planet is known as the Red Planet?", ["mars"]),
    ("How many continents are there?", ["7", "seven"]),
    (
        "What is the largest ocean on Earth?",
        ["pacific", "pacific ocean"],
    ),
    (
        "Who wrote the play Romeo and Juliet?",
        ["shakespeare", "william shakespeare"],
    ),
    ("What is the capital of Pakistan?", ["islamabad"]),
    ("How many days are there in a week?", ["7", "seven"]),
    ("What is the chemical symbol for water?", ["h2o"]),
    ("Which is the largest mammal?", ["blue whale", "whale"]),
    ("What is the national language of Pakistan?", ["urdu"]),
]

POINTS_RIGHT = 1
TARGET = 7

correct = 0
wrong = 0
score = 0

for number, (question, correct_answers) in enumerate(
    questions, start=1
):
    answer = input(
        f"Q{number}/{len(questions)}: {question} "
    ).strip().lower()

    if answer in correct_answers:
        correct += 1
        score += POINTS_RIGHT
        print(
            f"Correct! +{POINTS_RIGHT} | Score: {score}"
        )
    else:
        wrong += 1
        correct_answer = correct_answers[0].title()
        print(
            f"Wrong! (Answer: {correct_answer}) "
            f"| Score: {score}"
        )

# Calculate the final results.
total_asked = correct + wrong

if total_asked > 0:
    correct_percent = (correct / total_asked) * 100
    wrong_percent = (wrong / total_asked) * 100
else:
    correct_percent = 0
    wrong_percent = 0

print("\n--- Final Result ---")
print(f"Questions asked : {total_asked}")
print(
    f"Correct answers : {correct} "
    f"({correct_percent:.1f}%)"
)
print(
    f"Wrong answers   : {wrong} "
    f"({wrong_percent:.1f}%)"
)

max_score = len(questions) * POINTS_RIGHT
print(f"Final score     : {score}/{max_score}")

if score >= TARGET:
    print(f"You win! You reached the target of {TARGET}.")
else:
    print(
        f"Target not reached ({score}/{TARGET}). "
        "Try again!"
    )
    