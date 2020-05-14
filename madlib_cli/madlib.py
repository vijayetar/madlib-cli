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
  print('This is the count', count)
  end = 0
  new_list=[]
  for i in range(count):
    print('this is i', i)
    print('This is inside the loop')
    start = template.find("{",end)+1
    end = template.find("}",start)
    print(start,end)
    word = template[start:end]
    print('this is word', word)
    new_list.append(word)
    print('this is new_list', new_list)
    print('this is new word in template', template)
  get_user_input(new_list)

def prompt_user(word):
  print('*** Please enter your choice of {}? ***'.format(word))

def get_user_input(list):
  for question in list:
    prompt_user(question)
    user_input = input()
    print(user_input)
    answer = "".join([j for j in input().split()])
    if answer in answer_dict:
      print("try something new")
      prompt_user(question)
      answer = "".join([j for j in input().split()])
    answer_dict[answer]=question
  print(answer_dict)




# remove the words within the "{}" and leave it empty
#[x] store the words in another list
# make these words into a dictionary
# let user input a value for each key in the dictionary 
# insert the value in the template
# return the new string
# save the new string in the file

if __name__ == "__main__":
    welcome()
    get_question()

