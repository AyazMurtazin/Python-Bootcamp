import os
import json
from models.test_types import Questions, Question, Indications, NormalIndications, Answer, PossibleAnswer
from typing import List
from pydantic import ValidationError

from models.response_analysis import analyze


def model_from_args(model, args):
    return model(**{field: arg for field, arg in zip(model.model_fields, args)})


def till_it_work(call_func, *args, entry_function=input):
    while True:
        try:
            return call_func(*args, entry_function())
        except Exception as e:
            print(e)
            print("Try again!")


class VoightKampffTest:
    """
    The VoightKampffTest class is an interface for interacting with the interviewee and displaying the test result.

    ...

    Attributes
    ----------
    _filename : str
        name of json file with questions
    _questions : Questions
        Container for checking and interraction with questions list
    _answers : List[Answer]
        Container for storage interviewee answers

    Methods
    -------
    filename : property
        Getter and setter for the filename attribute.
    load_questions_from_json(filename: str)
        Loads questions from a JSON file and initializes the _questions attribute.
    start()
        Initiates the test, prompts questions to the interviewee, and stores their answers.
        Finally, it prints the test result ('Man' or 'Replicant') based on the analysis.
    reciew_answer(question: Question, entry: str) -> PossibleAnswer
        Reviews the interviewee's answer for a given question and returns the corresponding PossibleAnswer.
    reciew_indications(entry: str)
        Parses and returns indications provided by the interviewee.
    get_result() -> bool
        Analyzes the stored answers and returns True if the interviewee is identified as human ('Man'), otherwise False ('Replicant').
    """

    _filename: str
    _questions: Questions
    _answers: List[Answer] = list()

    def __init__(self) -> None:
        pass

    @property
    def filename(self):
        """Getter for the filename attribute."""

        return self._filename

    @filename.setter
    def filename(self, filename):
        """Setter for the filename attribute."""

        try:
            questions_json = json.load(open(filename, 'r'))
            self._questions = Questions(**questions_json)
            self._filename = filename
        except:
            raise AttributeError("Wrong filename")

    def load_questions_from_json(self, filename: str):
        """Loads questions from a JSON file and initializes the _questions attribute."""

        self.filename = filename

    def start(self):
        """
        Initiates the Voight-Kampff test.
        
        Returns:
            bool: True if the interviewee is identified as human ('Man'), otherwise False ('Replicant').
        """

        till_it_work(self.load_questions_from_json)
        for question in self._questions.questions:
            print(question.question)
            for count, j in enumerate(question.answers):
                print(count + 1, ")", j.answer)
            ans = till_it_work(self.reciew_answer, question)
            ind = till_it_work(self.reciew_indications)
            self._answers.append(Answer(answer=ans, indications=ind))
        if self.get_result():
            print("Man")
            return True
        else:
            print("Replicant")
            return False

    def reciew_answer(self, question: Question, entry: str) -> PossibleAnswer:
        """
        Reviews the interviewee's answer for a given question.

        Args:
            question (Question): The question being answered.
            entry (str): The entry representing the interviewee's response.

        Returns:
            PossibleAnswer: The corresponding PossibleAnswer object.
        """

        index = int(entry)-1
        if 0 <= index < len(question.answers):
            return question.answers[index]
        else:
            raise Exception("Variant out of range")

    def reciew_indications(self, entry: str):
        """
        Parses the indications provided by the interviewee.

        Args:
            entry (str): The entry representing the interviewee's indications.

        Returns:
            Indications: The parsed indications.
        """

        indications = model_from_args(
            Indications, [int(i) for i in entry.split()])
        return indications

    def get_result(self):
        """
        Analyzes the stored answers and determines if the interviewee is human or a replicant.

        Returns:
            bool: True if the interviewee is identified as human, otherwise False.
        """
        
        return analyze(self._answers)
