from voight_kampff_test import VoightKampffTest
from models.test_types import Question
import pytest
from sys import path
path.append("../")
TEST_MODEL = VoightKampffTest()
QUESTION = Question(**{"question": "A tortoise lays on its back, its belly baking in the hot sun. You're not helping.",
                       "answers": [
                           {
                               "answer": "I flip the tortoise over, ensuring it survives.",
                               "result": True
                           },
                           {
                               "answer": "I observe the tortoise but take no action.",
                               "result": False
                           },
                           {
                               "answer": "I ignore the tortoise and continue with my task.",
                               "result": False
                           },
                           {
                               "answer": "I feel empathy for the tortoise but leave it be, considering the natural course of life.",
                               "result": False
                           }
                       ]})


@pytest.mark.parametrize("filename", ["./test_files/test_false.json", "./test_files/test_false_1.json", "./test_files/test_false_2.json", "./test_files/test_false_3.json"])
def test_load_questions_from_json_true(filename):
    """
    Test loading questions from JSON file when it's expected to raise an exception.

    Args:
        filename (str): The filename of the JSON file.

    Raises:
        Exception: If loading questions from JSON file succeeds when it's expected to fail.
    """

    with pytest.raises(Exception) as e_info:
        TEST_MODEL.load_questions_from_json(filename)


@pytest.mark.parametrize("filename", ["./test_files/test_true.json", "./test_files/test_true_1.json", "./test_files/test_true_2.json", "./test_files/test_true_3.json"])
def test_load_questions_from_json_false(filename):
    """
    Test loading questions from JSON file when it's expected to succeed.

    Args:
        filename (str): The filename of the JSON file.
    """
    assert TEST_MODEL.load_questions_from_json(filename) == None


@pytest.mark.parametrize("entry", ["-1", "0", "12", "5"])
def test_reciew_answer_false(entry):
    """
    Test reviewing an answer when the entry is invalid.

    Args:
        entry (str): The invalid entry for reviewing an answer.

    Raises:
        Exception: If reviewing the answer succeeds when it's expected to fail.
    """

    with pytest.raises(Exception) as e_info:
        TEST_MODEL.reciew_answer(QUESTION, entry)


@pytest.mark.parametrize("entry", ["1", "2", "3", "4"])
def test_reciew_answer_true(entry):
    """
    Test reviewing an answer when the entry is valid.

    Args:
        entry (str): The valid entry for reviewing an answer.
    """

    assert TEST_MODEL.reciew_answer(
        QUESTION, entry) == QUESTION.answers[int(entry) - 1]


@pytest.mark.parametrize("entry", ["-1 60 2 2", "12 -1 2 2", "12 60 -1 2", "12 60 2 -1", "101 60 2 2", "12 301 2 2", "12 60 0 2", "12 60 2 12"])
def test_reciew_indications_false(entry):
    """
    Test reviewing indications when the entry is invalid.

    Args:
        entry (str): The invalid entry for reviewing indications.

    Raises:
        Exception: If reviewing the indications succeeds when it's expected to fail.
    """
    
    with pytest.raises(Exception) as e_info:
        TEST_MODEL.reciew_indications(entry)
