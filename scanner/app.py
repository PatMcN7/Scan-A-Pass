from flask import Flask, render_template
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('SELECT time FROM times WHERE name = "RayP"')
RayP_time_query = cur.fetchall()
RayP_time = RayP_time_query[0][0]
cur.execute('SELECT time FROM times WHERE name = "AndrewL"')
AndrewL_time_query = cur.fetchall()
AndrewL_time = AndrewL_time_query[0][0]
cur.execute('SELECT time FROM times WHERE name = "PatrickM"')
PatrickM_time_query = cur.fetchall()
PatrickM_time = PatrickM_time_query[0][0]
cur.execute('SELECT time FROM times WHERE name = "EricJ"')
EricJ_time_query = cur.fetchall()
EricJ_time = EricJ_time_query[0][0]
app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html', student_1 = 'RayP', student_2 = 'AndrewL', student_3 = 'PatrickM', student_4 = 'EricJ', student_1_time = RayP_time, student_2_time = AndrewL_time , student_3_time = PatrickM_time, student_4_time = EricJ_time, location ='Classroom')



app.run(host='0.0.0.0', port=8080)
