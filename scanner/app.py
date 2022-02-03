from flask import Flask, render_template
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()
app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html', student_1 = 'RayP', student_2 = 'AndrewL', student_3 = 'PatrickM', student_4 = 'EricJ', student_1_time = '1:00', student_2_time = '2:00', student_3_time = '3:00', student_4_time = '4:00', location ='Classroom')



app.run(host='0.0.0.0', port=8080)