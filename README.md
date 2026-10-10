# General Knowledge Quiz

A quiz game project written in Python. It asks 10 general knowledge questions, keeps track of right and wrong answers, calculates percentages, and tells you whether you reached the target score.

## Features

- Asks **10 questions**, numbered `Q1/10` to `Q10/10`
- **Case-insensitive** answers (`Paris`, `PARIS` and `paris` all work)
- **Ignores extra spaces** before and after the answer
- Accepts **multiple correct answers** for a question (e.g. `7` or `seven`)
- Shows the **correct answer** when you get one wrong
- Shows a **running score** after every question
- Final report with **correct and wrong counts and percentages**
- **Pass/fail result:** you win with a score of **7 or more**

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries needed

Check your version:

```bash
python --version
```

## How to Run

1. Save the code as `quiz.py` inside a folder (for example `python_quiz_project`).
2. Open the folder in VS Code, or open a terminal in that folder.
3. Run:

```bash
python quiz.py
```

On Mac/Linux you may need `python3 quiz.py`.

## How to Play

- Read the question and type your answer.
- Press **Enter** to submit.
- Type just the answer, with no quotation marks.
- Spelling matters, but capital letters and extra spaces do not.

## Example Run

Q1/10: What is the capital of France? paris
Correct! +1 | Score: 1
Q2/10: Which planet is known as the Red Planet? venus
Wrong! (Answer: Mars) | Score: 1
Q3/10: How many continents are there? seven
Correct! +1 | Score: 2

--- Final Result ---
Questions asked : 10
Correct answers : 8  (80.0%)
Wrong answers   : 2  (20.0%)
Final score     : 8/10
You win! You reached the target of 7.

## Scoring Rules

| Rule | Value |
|---|---|
| Points for each right answer | +1 |
| Points for each wrong answer | 0 (no negative marking) |
| Maximum score | 10 |
| Target to win | **7 or more** |

Percentages are calculated as:

correct % = (correct answers / questions asked) x 100
wrong %   = (wrong answers / questions asked) x 100

## Customizing the Quiz

All settings are at the top of the file.

**Change the target or points:**

POINTS_RIGHT = 1    # points gained for each right answer
TARGET = 7          # score needed to pass

**Add or change a question:** edit the `questions` list. Each item has the question text and a list of accepted answers (write the answers in lowercase):

("What is the capital of Japan?", ["tokyo"]),

The question numbers, total score and percentages update automatically when you add or remove questions. If you change the number of questions, also check that `TARGET` still makes sense.

## How It Works

For each question, the program repeats the same four steps:

1. **Ask and capture:** `input()` reads the user's answer as a string.
2. **Sanitize:** `.strip().lower()` removes extra spaces and converts the text to lowercase.
3. **Evaluate:** `answer in correct_answers` checks whether the answer matches any accepted answer.
4. **Execute:** an `if / else` block updates the counters and prints feedback.

At the end, the program calculates the percentages and compares the score with `TARGET` using `score >= TARGET`.

## Project Structure

python_quiz_project/
├── quiz.py
└── README.md

## Possible Improvements

- Shuffle the questions with the `random` module
- Add a "play again" option
- Add grade messages (Excellent, Good, Needs improvement)
- Load questions from a JSON or CSV file
- Add difficulty levels with different point values

## Author
Muhammad Khan