from flask import Flask, render_template, redirect
from form import SchoolForm
from form import HomeForm
from config import Config
from todo import my_function

app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_school_list = []
def set_school_message(message):
  global my_school_list
  my_school_list.append(message)
  print(my_school_list)

my_home_list = []
def set_home_message(message):
  global my_home_list
  my_home_list.append(message)
  print(my_home_list)

def my_function():
  print("Todolist")

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form1 = SchoolForm()
  my_function()
  form2 = HomeForm()
  if form1.validate_on_submit():
    if form1.is_submitted():
      print("made it")
      set_school_message(form1.message.data)
      return redirect('/display')
  elif form2.validate_on_submit():
    if form2.is_submitted():
      print("made it")
      set_home_message(form2.message.data)
      return redirect('/display')
  return render_template('pageOne.html', form1=form1,form2=form2)

  
@app.route('/display')
def page_two():
  return render_template('pageTwo.html', my_school_list=my_school_list)

@app.route('/display')
def page2_two():
  return render_template('pageTwo.html', my_home_list=my_home_list)

app.run(host='0.0.0.0', port=8080)

# @app.route('/onetwo', methods=['GET', 'POST'])
# def page_one_two():
#   form = HomeForm()
#   if form.is_submitted():
#     print("made it")
#     set_home_message(form.message.data)
#     return redirect('/display')
#   return render_template('pageOne.html', form=form)
  
app.run(host='0.0.0.0',port=8080)

