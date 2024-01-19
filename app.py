from flask import Flask, render_template, jsonify
from flask import request

import datetime
import random

streak = 0
app = Flask(__name__)
conversionsDic = {
    "5.6": "4c ",
    "5.7": "5a",
    "5.8": "5b",
    "5.9": "5c",
    "5.10a": "6a",
    "5.10b": "6a+",
    "5.10c": "6b",
    "5.10d": "6b+",
    "5.11a": "6c",
    "5.11b": "6c",
    "5.11c": "6c+",
    "5.11d": "7a",
    "5.12a": "7a+",
    "5.12b": "7b",
    "5.12c": "7b+",
    "5.12d": "7c",
    "5.13a": "7c+",
    "5.13b": "8a",
    "5.13c": "8a+",
    "5.13d": "8b",
    "5.14a": "8b+",
    "5.14b": "8c",
    "5.14c": "8c+",
    "5.14d": "9a",
    "5.15a": "9a+",
    "5.15b": "9b",
    "5.15c": "9b+",
    "5.15d": "9c",
    "4c": "5.6",
    "5a": "5.7",
    "5b": "5.8",
    "5c": "5.9",
    "6a": "5.10a",
    "6a+": "5.10b",
    "6b": "5.10c",
    "6b+": "5.10d",
    "6c": "5.11a",
    "6c+": "5.11c",
    "7a": "5.11d",
    "7a+": "5.12a",
    "7b": "5.12b",
    "7b+": "5.12c",
    "7c": "5.12d",
    "7c+": "5.13a",
    "8a": "5.13b",
    "8a+": "5.13c",
    "8b": "5.13d",
    "8b+": "5.14a",
    "8c": "5.14b",
    "8c+": "5.14c",
    "9a": "5.14d",
    "9a+": "5.15a",
    "9b": "5.15b",
    "9b+": "5.15c",
    "9c": "5.15d"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stopwatch')
def stopwatch():
    # Logic for stopwatch
    return render_template('stopwatch.html')


@app.route('/game')
def game():
    return render_template('gradeConversion.html')


@app.route('/grade_conversion')
def grade_conversion():
    grade = request.args.get('grade')  # Get the grade value from the query parameter
    # Perform grade conversion logic using the provided grade value
    equivalent_grade = conversionsDic.get(grade, "Grade not found")

    # Return the equivalent grade as JSON response
    return jsonify({'equivalent_grade': equivalent_grade})


@app.route('/study_grades')
def study_grades():
    global streak
    grade_list = list(conversionsDic.items())
    random_grade = random.choice(grade_list)
    question, correct_answer = random_grade

    return jsonify({'question': question, 'correct_answer': correct_answer, 'streak': streak})


@app.route('/check_answer', methods=['POST'])
def check_answer():
    global streak
    data = request.json
    user_answer = data.get('answer')
    correct_answer = data.get('correct_answer')

    is_correct = user_answer.strip() == correct_answer.strip()

    if is_correct:
        streak += 1
    else:
        streak = 0

    response = {
        'correct': is_correct,
        'message': 'Well done! You got it right!' if is_correct else f'Incorrect. The correct answer is {correct_answer}',
        'streak': streak
    }

    return jsonify(response)


@app.route('/easy')
def easy():
    # Define the easy hangboard workout as a structured HTML with classes for styling
    easy_workout = """
    <div class="workout-details">
        <div class="key">1st minute:</div>
        <div class="value">15 sec hang, Jug</div>

        <div class="key">2nd minute:</div>
        <div class="value">1 pull-up, Round Sloper</div>

        <div class="key">3rd minute:</div>
        <div class="value">10 second hang, Medium Edge</div>

        <div class="key">4th minute:</div>
        <div class="value">15 second hang w/ 3 shrugs, Pocket</div>

        <div class="key">5th minute:</div>
        <div class="value">20 second hang w/ 2 pull-ups, Large Edge</div>

        <div class="key">6th minute:</div>
        <div class="value">10 second hang, Round Sloper 5 knee raises, Pocket</div>

        <div class="key">7th minute:</div>
        <div class="value">4 pull-ups, Large Edge</div>

        <div class="key">8th minute:</div>
        <div class="value">10 second hang, Medium Edge</div>

        <div class="key">9th minute:</div>
        <div class="value">3 pull-ups, Jug</div>

        <div class="key">10th minute:</div>
        <div class="value">Hang as long as you can, Round Sloper</div>
    </div>
    """

    return jsonify({'easy_workout': easy_workout})


@app.route('/medium')
def medium():
    medium_workout = """
    <div class="workout-details">
        <div class="key">1st minute:</div>
        <div class="value">15 second hang, 3 pull-ups, Large Edge</div>

        <div class="key">2nd minute:</div>
        <div class="value">2 pull ups, Round Sloper 20 second hang, Medium Edge</div>

        <div class="key">3rd minute:</div>
        <div class="value">20 second hang, Small Edge 15 second 90Âº bent arm hang, Pocket</div>

        <div class="key">4th minute:</div>
        <div class="value">30 second hang, Round Sloper</div>

        <div class="key">5th minute:</div>
        <div class="value">20 second hang, Large Edge 4 pull-ups, Pocket</div>

        <div class="key">6th minute:</div>
        <div class="value">3 offset pulls each arm (high arm jug, low arm small hold)</div>

        <div class="key">7th minute:</div>
        <div class="value">15 knee raises, Jug 15 second hang, Medium Edge</div>

        <div class="key">8th minute:</div>
        <div class="value">25 second hang, Medium Edge</div>

        <div class="key">9th minute:</div>
        <div class="value">15 second hang, Slope 3 pull-ups, Jug</div>

        <div class="key">10th minute:</div>
        <div class="value">Hang as long as you can, Round Sloper</div>
    </div>
    """
    return jsonify({'medium_workout': medium_workout})


@app.route('/hard')
def hard():
    hard_workout = """
       <div class="workout-details">
        <div class="key">1st minute:</div>
        <div class="value">20 seconds straight arm hang, Large Slope 3 pull-ups, 4-Finger Flat Edge</div>

        <div class="key">2nd minute:</div>
        <div class="value">20 seconds slightly bent arm hang, Large Slope, stay on 20 seconds L-sit or 20 hanging knee curls</div>

        <div class="key">3rd minute:</div>
        <div class="value">5 pull-ups, 3-Finger Pocket, stay on 25 seconds straight arm hang</div>

        <div class="key">4th minute:</div> 
        <div class="value">Use every hold starting at the 3-Finger Pocket and 
        working up, staying on each for 5 seconds (don't get off to change holds) Finish on Large Slope with a 20 
        second hang</div>

        <div class="key">5th minute:</div>
        <div class="value">20 seconds single arm hang, Four-Finger Flat Edge, switch hands and repeat</div>

        <div class="key">6th minute:</div>
        <div class="value">5 offset pull ups, Large Slope (top hand) 3-Finger Pocket (bottom hand), change hands and repeat</div>

        <div class="key">7th minute:</div>
        <div class="value">30 seconds 90 degree bent arm hang, Four-Finger Incut Edge, 15 seconds straight arm hang, 3 Finger Pocket</div>

        <div class="key">8th minute:</div>
        <div class="value">3 L-sit pull-ups (bend knees if you have to), 5 seconds front lever or 15 seconds straight arm hang, Large Slope</div>

        <div class="key">9th minute:</div>
        <div class="value">20 seconds straight arm hang using only 2 fingers on 3 Finger Pockets, 3 power pull-ups (use weights or helper for resistance, should just be able to do 3 pulls)</div>

        <div class="key">10th minute:</div>
        <div class="value">maximum slightly bent arm hang, Large Slope (go to failure) no rest, maximum straight arm hang - Large Slope</div>
    </div>
    """
    return jsonify({'hard_workout': hard_workout})


if __name__ == '__main__':
    app.run(debug=True)
