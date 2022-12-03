import yaml
from coop_grader.tools import binder
from typing import Any
from yaml.loader import SafeLoader

def function_factory(conf: dict) -> dict:
    questions = list(conf.keys())
    functions = {}
    for question in questions:
        messages = conf[question]['messages']
        variable = conf[question]['variable_name']
        expected = conf[question]['expected_value']
        assertion = conf[question]['assertion']
        assert_statement = generate_assertion_statement(assertion, expected)
        correct_msg = messages['correct']
        incorrect_msg = messages['incorrect']
        missing_msg = messages['missing']
        template = f"""
        def {question}():
            try:
                assert binder.VARS['{variable}'] {assert_statement}
                print('{correct_msg}')
                binder.VARS['{question}_correct'] = True
            except AssertionError:
                print('{incorrect_msg}')
            except KeyError:
                print('{missing_msg}')
        """.strip()
        exec(template)
        functions[question] = locals()[question]
    return functions


    # Import yaml and generate functions for testrunner
def generate_tests(conf: dict) -> dict:
    try:
        funcs = function_factory(conf)
        return funcs
    except Exception:
        print('Something went wrong')
        raise


def generate_assertion_statement(assertion: str, expected: Any) -> str:
    """ Generates an assertion statement using the given assertion operation and value.

    Given one of the following assertion operations ('GT', 'LT', 'EQ', 'GE', 'LE', 'NE', 'IN'),
    this function generates a string containing the desired operation on the expected value.

    e.g. generate_assertion_statement('EQ', 1) => '== 1'

    Args:
        assertion:  The assertion operation to use. Must be one of ('GT', 'LT', 'EQ', 'GE', 
                    'LE', 'NE', 'IN')
        expected:   The value that the assertion is operating on
    Returns:
        A string containing the given assertion operation on the expected value

    """
    operations = ['GT', 'LT', 'EQ', 'GE', 'LE', 'NE', 'IN']
    assertion = assertion.upper()
    if assertion not in operations:
        raise KeyError('Invalid assertion operation submitted') 
    if assertion == 'EQ':
        statement = f'== {expected}'
    elif assertion == 'NE':
        statement = f'!= {expected}'
    elif assertion == 'GE':
        statement = f'>= {expected}'
    elif assertion == 'LE':
        statement = f'<= {expected}'
    elif assertion == 'GT':
        statement = f'> {expected}'
    elif assertion == 'LT':
        statement = f'< {expected}'
    elif assertion == 'IN':
        statement = f'in ({expected})'
    return statement


# def test_generate_assertion_statement():
#     assert generate_assertion_statement('EQ', 1) == '== 1'
#     assert generate_assertion_statement('GT', 1) == '> 1'
#     assert generate_assertion_statement('LT', 1) == '< 1'
#     assert generate_assertion_statement('GE', 1) == '>= 1'
#     assert generate_assertion_statement('LE', 1) == '<= 1'
#     assert generate_assertion_statement('NE', 1) == '!= 1'
#     assert generate_assertion_statement('IN', 1) == 'in (1)'
#     try:
#         assert generate_assertion_statement('EP', 1) == '== 1'
#         print('Something went wrong - shouldn\'t recognize EP')
#     except (AssertionError, KeyError):
#         print('All tests passed')