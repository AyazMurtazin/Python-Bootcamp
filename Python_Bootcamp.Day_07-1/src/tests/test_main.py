from models.test_types import Indications
from models.test_types import PossibleAnswer, Answer
from models.response_analysis import analyze
import pytest
from sys import path
path.append("../")

TRUE_ANSWER = PossibleAnswer(**{"answer": "", "result": True})
FALSE_ANSWER = PossibleAnswer(**{"answer": "", "result": False})
TRUE_INDICATIONS = Indications(**{"respiration":  13,
                                  "heart_rate": 70,
                                  "blushing_level": 2,
                                  "pupillary_dilation": 3})
FALSE_INDICATIONS = Indications(**{"respiration":  13,
                                   "heart_rate": 180,
                                   "blushing_level": 5,
                                   "pupillary_dilation": 3})

TRUE_ANSWERS = [Answer(**{"answer": TRUE_ANSWER,
                          "indications": TRUE_INDICATIONS})]
FALSE_ANSWERS_1 = [Answer(**{"answer": TRUE_ANSWER,
                             "indications": FALSE_INDICATIONS})]
FALSE_ANSWERS_2 = [Answer(**{"answer": FALSE_ANSWER,
                             "indications": TRUE_INDICATIONS})]
FALSE_ANSWERS_3 = [Answer(**{"answer": FALSE_ANSWER,
                             "indications": FALSE_INDICATIONS})]


@pytest.mark.parametrize("answers", [TRUE_ANSWER])
def test_load_questions_from_json_false(answers):
    """
    Test the analysis of answers when all answers are true.

    Args:
        answers (PossibleAnswer): The list of true answers.

    Asserts:
        bool: Asserts that the analysis result is True.
    """

    assert analyze(answers) == True


@pytest.mark.parametrize("answers", [FALSE_ANSWERS_1, FALSE_ANSWERS_2, FALSE_ANSWERS_3])
def test_load_questions_from_json_false(answers):
    """
    Test the analysis of answers when at least one answer is false.

    Args:
        answers (List[Answer]): The list of answers to be analyzed.

    Asserts:
        bool: Asserts that the analysis result is False.
    """
    
    assert analyze(answers) == False
