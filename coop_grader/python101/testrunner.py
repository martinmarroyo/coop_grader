from coop_grader.tools import binder, core
from pathlib import Path

def validator(conf_filename: str = 'questions.yaml') -> dict:
    path = Path.cwd()/conf_filename
    validator_funcs = core.generate_tests(filepath=path)
    return validator_funcs

    
def final_check():
    q1 = binder.VARS['Q1_correct']
    try:
        assert all([q1]) == True
    except AssertionError:
        print('Please review questions and submit when completed')

