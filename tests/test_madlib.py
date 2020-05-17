import pytest

from madlib_cli.madlib import read_template, get_question, create_string, prompt_user

#checks if new_list contains the missing components
def test_get_question():
  actual = get_question("This is a noun {noun} and a verb {verb} with adjective {adjective} noun {noun}")
  expected = ['noun', 'verb', 'adjective', 'noun']
  assert actual == expected

# check the prompt for user
def test_prompt_user():
  actual = prompt_user("noun")
  expected = "*** Please enter one noun? ***"
  assert actual == expected

# check the final string created
def test_create_string():
  actual = create_string("This is a noun {noun} and a verb {verb} with adjective {adjective} noun {noun}", {'monkey': 'noun', 'eating': 'verb', 'graceful': 'adjective', 'jam': 'noun'})
  expected = "This is a noun monkey and a verb eating with adjective graceful noun jam"
  assert actual == expected

def test_read_template():
  with open('./assets/spam.txt')as f:
    actual = f.read().strip()
    expected = "This is a noun {noun} and a verb {verb} with adjective {adjective} noun {noun}"
    assert actual == expected