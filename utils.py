"""
pull questions from site as format:
https://projecteuler.net/minimal=1
"""
import requests
from abc import ABC
from html.parser import HTMLParser


class HTMLFilter(HTMLParser, ABC):
    """
    Given html, remove html elements and return string

    :return: de html'd string
    """
    text = ""

    def handle_data(self, data):
        self.text += data


def pull_euler_question(problem_id=0):
    """
    Given the question number, returns the de-html'd question prompt

    :param problem_id: the question number to return the prompt of
    :return: Question prompt string
    """
    if problem_id != 0:
        euler_url = "https://projecteuler.net/minimal=" + str(problem_id)
        r = requests.get(euler_url)

        f = HTMLFilter()
        f.feed(r.text)
        print(f.text)

    else:
        return "Data for that problem cannot be found"


def format_solution_output(question=0, solution=""):
    """
    just a toString for the question & answer

    :param question: the question number
    :param solution: the solution string
    :return: formatted output
    """
    print("==QUESTION " + str(question) + "==")
    print(pull_euler_question(question))

    print("==SOLUTION==")
    print(solution)
