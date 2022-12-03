import pkg_resources
import yaml
from yaml.loader import SafeLoader
from coop_grader.tools import binder, core
from pathlib import Path


def validator(conf_filename: str = 'questions.yaml') -> dict:
    try:
        file = pkg_resources.resource_stream(__name__, conf_filename)
        conf = yaml.load(file, Loader=SafeLoader)
        validator_funcs = core.generate_tests(conf=conf)
    except FileNotFoundError:
        print('Error: Did you write your answer sheet to the `questions.yaml` file for this lesson?')
    else:
        return validator_funcs

    
def final_check():
    q1 = binder.VARS['Q1_correct']
    try:
        assert all([q1]) == True
    except AssertionError:
        print('Please review questions and submit when completed')

