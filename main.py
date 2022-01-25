from flask import Flask, render_template, redirect
from form import SchoolForm
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



# def my_function():
#   print("Todolist")

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form1 = SchoolForm()
  my_function()
  if form1.validate_on_submit():
    if form1.is_submitted():
      print("made it")
      set_school_message(form1.message.data)
      return redirect('/display')


  
@app.route('/display')
def page_two():
  return render_template('pageTwo.html', my_school_list=my_school_list)

app.run(host='0.0.0.0',port=8080)

