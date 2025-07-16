import pytest
from pages.main_page import MainPage


@pytest.mark.parametrize("question_index", range(6))
def test_question_answer(driver, question_index):
    main_page = MainPage(driver)
    main_page.open()
    answer_text = main_page.get_question_answer(question_index)
    assert answer_text.strip() != "", f"Ответ на вопрос {question_index} не отображается"