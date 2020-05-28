#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
import sqlite3
from config import Config


app = Flask(__name__)
app.config.from_object(Config) # Secret key in config.py
# secret_key = app.config['SECRET_KEY']

class Constraints:


    def __init__(self, num, level, rule, time):

        self.num = num
        self.level = level
        self.rule = rule
        self.time = time
        # self.game = f"# {self.num} Level: {self.level} Rule: {self.rule} Time allowed: {self.time}"
        self.game = "# {0} Level: {1} Rule: {2} Time allowed: {3}".format( self.num, self.level, self.rule, self.time)

constraints = Constraints(2, "Easy", "Ends in a w", "4 mins")
num = constraints.num
level = constraints.level
rule = constraints.rule
time = constraints.time

@app.route('/', methods=['GET', 'POST'])
def index():
    # Welcome page with constraints
    return render_template('index.html', num=num, level=level, rule=rule, time=time)



@app.route('/game', methods=['GET', 'POST'])
def game():
    print("in the /game route now")
    # The present game
    # loaded when the player presses enter in any of the input boxes
    if request.method == 'POST': 
        data = request.form # in key:value pairs
        print(data)
        print(num)
        word_holder = [] # initialise list of words entered by user
        word_a = data.get('aword') # data['aword'] requires an initial value in the input field
        word_b = data.get('bword')
        word_c = data.get('cword') 
        word_d = data.get('dword')
        word_e = data.get('eword')
        word_f = data.get('fword')
        word_g = data.get('gword')
        word_h = data.get('hword')
        word_i = data.get('iword')
        word_j = data.get('jword')
        word_k = data.get('kword')
        word_l = data.get('lword')
        word_m = data.get('mword')
        word_n = data.get('nword')
        word_o = data.get('oword')
        word_p = data.get('pword')
        word_q = data.get('qword')
        word_r = data.get('rword')
        word_s = data.get('sword')
        word_t = data.get('tword')
        word_u = data.get('uword')
        word_v = data.get('vword')
        word_w = data.get('wword')
        word_x = data.get('xword')
        word_y = data.get('yword')
        word_z = data.get('zword')
        word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_j, word_k, word_l, word_m, word_n, word_o, word_p, word_q, word_r, word_s, word_t, word_u, word_v, word_w, word_x, word_y, word_z, ])
        # OUTPUT - compare entered words to words in database
        conn = sqlite3.connect('words.db')
        print("Opened database successfully")
        cur = conn.cursor()
        cur.execute("SELECT word FROM words;")
        all_words = cur.fetchall()
        # print(len(all_words)) # 88280
        # check if all words inserted are in the words table (ie the 'dictionary')
        all_items = [item[0] for item in all_words[0:88280]] # make into a regular list
        incorrect = []
        correct = []
        for word in word_holder:
            if word not in all_items and word != "None":
                incorrect.append(word) # incorrect words added to list for display on the webpage
            else:
                correct.append(word)
                # print(word) # correct words printed to terminal
        print(incorrect)
        print(correct)
        conn.close()	
        print("Closed database successfully")

        return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_j=word_j, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_q=word_q, word_r=word_r, word_s=word_s, word_t=word_t, word_u=word_u, word_v=word_v, word_w=word_w, word_x=word_x, word_y=word_y, word_z=word_z, word_holder=word_holder, correct=correct,  incorrect=incorrect,  rule=rule, time=time )

     # Input fields are blank if loaded by pressing the PLAY! button in index.html
    else:
        return render_template('game.html', num=num, level=level, rule=rule, time=time) 

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.
    # app.run(host ='192.168.1.103', port=5000, debug=True)  
    # app.run(host ='192.168.1.103', port=5000, debug=False)  
    # app.run(host ='127.0.0.1', port=5000, debug=False)  


