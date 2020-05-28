#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
import sqlite3
from config import Config


app = Flask(__name__)
app.config.from_object(Config) # Secret key in config.py
# secret_key = app.config['SECRET_KEY']

def constraints():
    num = 2
    level = "Easy"
    rule = "Ends in letter w"
    time = "4 minutes"
    game = f"Game: {num}  |  Level: {level}  |  Constraint: {rule}  |  Time allowed: {time}"
    return game

@app.route('/', methods=['GET', 'POST'])
def index():
    # Welcome page with constraints
    game = constraints()
    return render_template('index.html', game=game)



@app.route('/game', methods=['GET', 'POST'])
def game():
    print("in the /game route now")
    # The present game
    game = constraints() # call the puzzle of the day method
    print(constraints())
    # loaded when the player presses enter in any of the input boxes
    if request.method == 'POST': 
        data = request.form # in key:value pairs
        print(data)
        word_holder = [] # initialise list of words entered by user
        word_a = data.get('aword') #['aword'] 
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
        for word in word_holder:
            if word not in all_items and word != "None":
                incorrect.append(word) # incorrect words added to list for display on the webpage
            else:
                print(word) # correct words printed to terminal
        conn.close()	
        print("Closed database successfully")

        return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_j=word_j, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_q=word_q, word_r=word_r, word_s=word_s, word_t=word_t, word_u=word_u, word_v=word_v, word_w=word_w, word_x=word_x, word_y=word_y, word_z=word_z, incorrect=incorrect, game=game)

    else:
        return render_template('game.html', game=game) # Blank if loaded by pressing the PLAY! button in index.html

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.

