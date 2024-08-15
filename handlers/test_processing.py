

def user_answer_processing(user_answers):
    user_categories = {
        'труд': user_answers.count('0'),
        'умственный труд': user_answers.count('1'),
        'бег': user_answers.count('2'),
        'прыжки': user_answers.count('3'),
        'скалолазание': user_answers.count('4'),
        'комп': user_answers.count('5'),
        'телефон': user_answers.count('6'),
        'планшет': user_answers.count('7'),
        'игры': user_answers.count('8'),
        'учёба': user_answers.count('9')
    }

    sorted_categories = sorted(user_categories.items(), key=lambda x: x[1], reverse=True)
    first_max_category = sorted_categories[0][0]
    second_max_category = sorted_categories[1][0]
    third_max_category = sorted_categories[2][0]
    forth_max_category = sorted_categories[3][0]
    fifth_max_category = sorted_categories[4][0]
    sixth_max_category = sorted_categories[5][0]

    return first_max_category, second_max_category, third_max_category, forth_max_category, fifth_max_category, sixth_max_category

