from flask import Flask, render_template, redirect
from form import MessageForm
from config import Config
from todo import my_function

app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_message = []
def setMessage(message):
  global my_message
  my_message=message
  print(my_message)

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form = MessageForm()
  if form.is_submitted():
    print("made it")
    setMessage(form.message.data)
    return redirect('/display')
  return render_template('pageOne.html', form=form)

  
@app.route('/display')
def page_two():
  return render_template('pageTwo.html', my_message=my_message)

app.run(host='0.0.0.0', port=8080)

@app.route('/', methods=['GET', 'POST'])
def page_one():
  form = MessageForm()
  if form.is_submitted():
    print("made it")
    setMessage(form.message.data)
    return redirect('/display')
  return render_template('pageOne.html', form=form)
  

 