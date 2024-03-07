from typing import List
from models.test_types import Answer, PossibleAnswer, Indications, NormalIndications


def confirm_indications(ind: Indications):
    """
    Confirms if the provided indications are normal.

    Args:
        ind (Indications): The indications to confirm.

    Returns:
        bool: True if the indications are normal, otherwise False.
    """

    try:
        NormalIndications.model_validate(dict(ind))
        return True
    except:
        return False


def analyze(answers: List[Answer]):
    """
    Analyzes the provided answers to determine if the interviewee is human or a replicant.

    Args:
        answers (List[Answer]): The list of answers provided by the interviewee.

    Returns:
        bool: True if the interviewee is identified as human, otherwise False.
    """

    res = list()
    for i in answers:
        res.append(i.answer.result and confirm_indications(i.indications))
    return (False if res.count(False)/len(res) > 0.3 else True)
