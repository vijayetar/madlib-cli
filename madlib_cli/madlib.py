from textwrap import dedent
## global variables
answer_dict = {}

def welcome():
  print("*"*50)
  print(dedent(""" 
  **    Welcome to the MadLib Game!               **
  **    Please see our instructions below.        **
  **    Enter word appropriate to what is asked   **
  **                                              **
  **    To quit at any time, type "quit"          **
  """))
  print("*"*50)
  print("\n")

def read_template(path):
  with open(path) as file:
    template = file.read()
    template = template.strip()
    return template

def get_question(template):
  count = template.count("{")
  end = 0
  new_list=[]
  for i in range(count):
    start = template.find("{",end)+1
    end = template.find("}",start)
    word = template[start:end]
    new_list.append(word)
  return(new_list)

def prompt_user(word):
  return f'*** Please enter one {word}? ***'

def get_user_input(list):
  for question in list:
    print(prompt_user(question))
    user_input = "".join([j for j in input().split()])
    while user_input=="" or user_input in answer_dict:
      print("try again")
      user_input = "".join([j for j in input().split()])
    answer_dict[user_input]=question
  return answer_dict

def create_string(template, dic):
  count = template.count("{")
  end = 0
  new_template = template
  for i in (range(count)):
    start = template.find("{",end)
    end = template.find("}",start)+1
    word = template[start:end]
    # replace word in template to that in dic
    for x,y in dic.items():
      if y in word:
        new_template = new_template.replace(word,x,1)
  print(new_template)
  return new_template

def write_file(path, template):
  with open(path, 'w') as writer:
    writer.write(template)

if __name__ == "__main__":
  template = read_template('assets/spam.txt')
  welcome()
  new_list = get_question(template)
  user_dict = get_user_input(new_list)
  new_template = create_string(template, user_dict)
  write_file('assets/new_template.txt',new_template)


