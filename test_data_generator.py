"""
Учебный файл для практической работы №5.
Назначение: генерация простых тестовых данных для формы обратной связи.
Файл можно загрузить в отдельную ветвь GitHub, например feature-code.
"""

from dataclasses import dataclass


@dataclass
class FeedbackCase:
    name: str
    email: str
    message: str
    expected_result: str


def get_feedback_cases() -> list[FeedbackCase]:
    return [
        FeedbackCase(
            name="Иван Петров",
            email="ivan.petrov@example.com",
            message="Прошу связаться со мной по вопросу регистрации.",
            expected_result="Форма успешно отправлена",
        ),
        FeedbackCase(
            name="",
            email="invalid-email",
            message="Тест некорректного ввода",
            expected_result="Показано сообщение об ошибке валидации",
        ),
    ]


if __name__ == "__main__":
    for number, case in enumerate(get_feedback_cases(), start=1):
        print(f"TC-{number}: {case.name or '<empty>'} | {case.email} | {case.expected_result}")
