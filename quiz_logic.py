def calculate_score(questions, user_answers):
    total_score = 0
    max_score = 0
    question_score = 5  # نمره هر سوال

    for i, question in enumerate(questions):
        correct = question['correct_answer']
        max_score += question_score
        
        # اگر کاربر پاسخی نداده باشد (`""`)، نمره‌ای تعلق نمی‌گیرد
        if i >= len(user_answers) or user_answers[i] == "":
            continue  # نمره = 0
        
        if user_answers[i] == correct:
            total_score += question_score
        else:
            total_score += question_score * 0.15  # 15% نمره برای پاسخ غلط

    return total_score, max_score