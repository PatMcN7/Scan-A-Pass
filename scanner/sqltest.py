import sqlite3

sql = sqlite3.connect('data.db')

crsr = sql.cursor()
card = 'EricJ'
crsr.execute('SELECT in_out FROM times3 WHERE name = (?)', (card,))
test = crsr.fetchall()

in_out_bool = [len(test) - 1][0]

if in_out_bool == 'True':
    crsr.execute('UPDATE times3 SET in_out = "False" WHERE name = (?)', (card,))
    sql.commit()
else:
    crsr.execute('UPDATE times3 SET in_out = "True" WHERE name = (?)', (card,))
    sql.commit()