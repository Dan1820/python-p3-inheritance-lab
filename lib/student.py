#!/usr/bin/env python

from user import User
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


class Student(User):

    def learn(self, knowledge=""):
        self.knowledge = knowledge
        return self.knowledge
