import json
import random

def generate_math_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '+':
        answer = a + b
        question = f"What is {a} + {b}?"
    elif operation == '-':
        answer = a - b
        question = f"What is {a} - {b}?"
    elif operation == '*':
        answer = a * b
        question = f"What is {a} * {b}?"
    elif operation == '/':
        b = random.randint(1, 10)
        a = b * random.randint(1, 10)
        answer = a // b
        question = f"What is {a} / {b}?"

    # تولید گزینه‌های منحصربفرد
    options = {answer}
    while len(options) < 4:
        if random.random() > 0.5:
            # گزینه‌های نزدیک به پاسخ صحیح
            options.add(answer + random.choice([-3, -2, -1, 1, 2, 3]))
        else:
            # گزینه‌های کاملا تصادفی
            options.add(random.randint(1, 100))
    
    options = list(options)
    random.shuffle(options)
    
    return {
        "question": question,
        "options": [str(o) for o in options],
        "correct_answer": str(answer)
    }

def generate_geography_question():
    countries = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Japan": "Tokyo",
        "Afghanistan": "Kabul",
        "Brazil": "Brasilia",
        "Canada": "Ottawa",
        "Australia": "Canberra"
    }
    country, capital = random.choice(list(countries.items()))
    
    wrong_answers = []
    while len(wrong_answers) < 3:
        wrong = random.choice(list(countries.values()))
        if wrong != capital and wrong not in wrong_answers:
            wrong_answers.append(wrong)
    
    options = wrong_answers + [capital]
    random.shuffle(options)
    
    return {
        "question": f"What is the capital of {country}?",
        "options": options,
        "correct_answer": capital
    }

def generate_history_question():
    events = {
        "World War I started": "1914",
        "World War II ended": "1945",
        "The fall of the Berlin Wall": "1989",
        "Independence of Afghanistan": "1919",
        "Moon landing": "1969",
        "American Revolution began": "1775",
        "French Revolution": "1789",
        "First man in space": "1961"
    }
    
    event, year = random.choice(list(events.items()))
    year_int = int(year)
    
    options = {year}
    while len(options) < 4:
        offset = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        options.add(str(year_int + offset))
    
    options = list(options)
    random.shuffle(options)
    
    return {
        "question": f"In which year did {event}?",
        "options": options,
        "correct_answer": year
    }

# تولید سوالات
questions = []
for _ in range(100):
    questions.append(generate_math_question())

for _ in range(50):
    questions.append(generate_geography_question())

for _ in range(50):
    questions.append(generate_history_question())

# ذخیره در فایل
with open("real_questions.json", "w") as f:
    json.dump(questions, f, indent=4, ensure_ascii=False)

print("✅ File 'real_questions.json' with 200 optimized questions created.")