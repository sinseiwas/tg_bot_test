import asyncio

async def user_answer_processing(user_answers):
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

    # Сортируем категории по количеству ответов, оставляя только те, которые больше 0
    sorted_categories = sorted(
        [(category, count) for category, count in user_categories.items() if count > 0],
        key=lambda x: x[1],
        reverse=True
    )

    # Берем только существующие категории
    most_popular_categories = [category for category, _ in sorted_categories[:3] if category != 0]
    least_popular_categories = [category for category, _ in sorted_categories[3:6] if category != 0]

    # Возвращаем только категории, которые существуют
    return most_popular_categories, least_popular_categories
