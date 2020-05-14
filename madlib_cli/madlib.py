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


with open('assets/template.txt') as file:
  template = file.read()
  template = template.strip()
  print('this is template',template)

print('file is closed?', file.closed)

def get_question():
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
  print('*** Please enter one {}? ***'.format(word))

def get_user_input(list):
  for question in list:
    prompt_user(question)
    user_input = "".join([j for j in input().split()])
    while user_input=="" or user_input in answer_dict:
      print("try again")
      user_input = "".join([j for j in input().split()])
    answer_dict[user_input]=question
  return answer_dict

def create_string(template, dic):
  count = template.count("{")
  print('This is the count', count)
  end = 0
  new_template = template
  for i in (range(count)):
    start = template.find("{",end)
    end = template.find("}",start)+1
    word = template[start:end]
    # replace word in template to that in dic
    for x,y in dic.items():
      if y in word:
        if y in word:
          new_template = new_template.replace(word,x)
  print('this is new template',new_template)


# remove the words within the "{}" and leave it empty
#[x] store the words in another list
#[x] make these words into a dictionary
#[x] let user input a value for each key in the dictionary 
#[x]insert the value in the template
#[x]return the new string
#[x]save the new string in the file

if __name__ == "__main__":
    welcome()
    new_list = get_question()
    user_dict = get_user_input(new_list)
    create_string(template, user_dict)


