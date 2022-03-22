from flask import Flask, render_template
import sqlite3

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('SELECT time FROM times WHERE name = "RayP"')
RayP_time_query = cur.fetchall()
RayP_time = RayP_time_query[len(RayP_time_query) - 1][0]
cur.execute('Select in_out FROM times3 WHERE name = "RayP"')
RayP_in_out_query = cur.fetchall()
RayP_in_out = RayP_in_out_query[len(RayP_in_out_query) - 1][0]
cur.execute('SELECT time FROM times WHERE name = "AndrewL"')
AndrewL_time_query = cur.fetchall()
AndrewL_time = AndrewL_time_query[len(AndrewL_time_query) - 1][0]
cur.execute('Select in_out FROM times3 WHERE name = "AndrewL"')
AndrewL_in_out_query = cur.fetchall()
AndrewL_in_out = AndrewL_in_out_query[len(AndrewL_in_out_query) - 1][0]
cur.execute('SELECT time FROM times WHERE name = "PatrickM"')
PatrickM_time_query = cur.fetchall()
PatrickM_time = PatrickM_time_query[len(PatrickM_time_query) - 1][0]
cur.execute('Select in_out FROM times3 WHERE name = "PatrickM"')
PatrickM_in_out_query = cur.fetchall()
PatrickM_in_out = PatrickM_in_out_query[len(PatrickM_in_out_query) - 1][0]
cur.execute('SELECT time FROM times WHERE name = "EricJ"')
EricJ_time_query = cur.fetchall()
EricJ_time = EricJ_time_query[len(EricJ_time_query) - 1][0]
cur.execute('Select in_out FROM times3 WHERE name = "EricJ"')
EricJ_in_out_query = cur.fetchall()
EricJ_in_out = EricJ_in_out_query[len(EricJ_in_out_query) - 1][0]

app = Flask('app')

@app.route('/flask/')
def index():
  return render_template('index.html', student_1 = 'AndrewL', student_2 = 'RayP', student_3 = 'PatrickM', student_4 = 'EricJ', student_1_time = AndrewL_time, student_2_time = RayP_time , student_3_time = PatrickM_time, student_4_time = EricJ_time,student_1_in_out = AndrewL_in_out, student_2_in_out = RayP_in_out, student_3_in_out = PatrickM_in_out, student_4_in_out = EricJ_in_out)



app.run(debug=True, host='0.0.0.0', port=8080)
