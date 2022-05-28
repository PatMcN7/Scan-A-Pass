#cards tables
from gpiozero import PWMLED
import RPi.GPIO as GPIO
import sqlite3
import time
from pn532 import *
import datetime
#defines the db and cursor
sql = sqlite3.connect('data.db')

crsr = sql.cursor()
card = ''
uid_string = []

andrew_location = 0
andrew_loc_list = ['Classroom', 'Hallway', 'Bathroom', 'Hallway', 'Classroom']
#led = PWMLED(27)

names = {
 "21710511289": 'PatrickM',
 "21714812489": 'AndrewL',
 '21720811489': 'RayP',
 '18524910289': 'EricJ',
 '7324110089':  'Mrs. Bauer'
}

sql_name = []

sql_card = []

#gets all data from cards and timeinout tables + defines the name query var
crsr.execute('SELECT * FROM cards')

cards =  crsr.fetchall()

crsr.execute('SELECT * FROM times')

card = ''

#name_query = ('SELECT name FROM cards WHERE card = (?)')

times = crsr.fetchall()

print(cards)

for i in range(0, 5):
    sql_name.append(cards[i][1])
    

for i in  range(0, 5):
    sql_card.append(cards[i][2])
    



counter = 0
#starts the program
if __name__ == '__main__':
    try:
        #tells you which communication method is being used
        pn532 = PN532_SPI(debug=False, reset=20, cs=4)
        #pn532 = PN532_I2C(debug=False, reset=20, req=16)
        #pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        print('Waiting for NFC card...')
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            print('.', end="")
#            led.value = 1
            # Try again if no card is available.
            if uid is None:
                continue

 #           led.value = 0 
            uid_string = [str(i) for i in uid]
            uid_string = ''.join(uid_string)
            for i in sql_card:
                if i == uid_string:
                    name_index = sql_card.index(i)
                    break
            unix = time.time()
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            keyword = 'Python'
            card = sql_name[name_index]
            crsr.execute('SELECT in_out FROM times3 WHERE name = (?)', (card,))
            in_out_fetch = crsr.fetchall()
            in_out_bool = in_out_fetch[len(in_out_fetch) - 1][0]
            if in_out_bool == 'True':
                in_out = 'False'
            else:
                in_out = 'True'
            crsr.execute("INSERT INTO times3 (name, time, in_out) VALUES (?, ?, ?)", (card, date, in_out))
            sql.commit()
            #name_query_execution = crsr.execute(name_query)
            #name = ''.join(name_query_execution)
            print('Found card with UID:', uid_string, card )
            if uid_string == '21714812489':
                andrew_location += 1
                andyloc = andrew_loc_list[andrew_location]
                print(andyloc)
                crsr.execute("UPDATE andrew set location = (?) WHERE id=1", (andyloc,))
                sql.commit()
            uid = None
            time.sleep(1.5)
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()

