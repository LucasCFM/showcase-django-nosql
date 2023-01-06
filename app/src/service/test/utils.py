from typing import List
from service.test.models import Question, INACTIVE_QUESTIONS_STATUS


def extract_questions_from_list(questions: List[dict]) -> List[Question]:
    result = []
    for question_dict in questions:
        q = Question(
            text = question_dict.get('text'),
            answers = question_dict.get('answers'),
            correctAnswers = question_dict.get('correctAnswers'),
            status = INACTIVE_QUESTIONS_STATUS,
            order = question_dict.get('order')
        )
        result.append(q)
    return result
