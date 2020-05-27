#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
import sqlite3
from config import Config


app = Flask(__name__)
app.config.from_object(Config) # Secret key in config.py
# secret_key = app.config['SECRET_KEY']

@app.route('/')
@app.route('/index')
def index():
    # Submitted words
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    data = request.form # in key:value pairs
    print(data)
    word_holder = [] # initialise list of words entered by user
    if data['action'] == 'reload':
        redirect(request.url)
            # print("Yay!!")
    if request.method == 'POST':
        word_a = data['aword']
        word_b = data['bword']
        word_c = data['cword'] 
        word_d = data['dword']
        word_e = data['eword']
        word_f = data['fword']
        word_g = data['gword']
        word_h = data['hword']
        word_i = data['iword']
        word_j = data['jword']
        word_k = data['kword']
        word_l = data['lword']
        word_m = data['mword']
        word_n = data['nword']
        word_o = data['oword']
        word_p = data['pword']
        word_q = data['qword']
        word_r = data['rword']
        word_s = data['sword']
        word_t = data['tword']
        word_u = data['uword']
        word_v = data['vword']
        word_w = data['wword']
        word_x = data['xword']
        word_y = data['yword']
        word_z = data['zword']
        word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_j, word_k, word_l, word_m, word_n, word_o, word_p, word_q, word_r, word_s, word_t, word_u, word_v, word_w, word_x, word_y, word_z, ])

        # If Submit button pressed, try to clear the fields for another run
            # if data['action'] == 'submit':
                # print("YAY!")
                # return redirect('/')
            # else:
                # pass


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
            if word not in all_items:
                incorrect.append(word) # incorrect words added to list for display on the webpage
            else:
                print(word) # correct words printed to terminal
        conn.close()	
        print("Closed database successfully")

        # see will the following refresh page with fields all cleared
        # if data['action'] == 'reload':
            # print("Yay!!")
        # if form.validate_on_submit():
            # return redirect('./templates/submitted.html')
        # try this to see if it will reload a blank form
        # return redirect(request.url)

    return render_template('index.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_j=word_j, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_q=word_q, word_r=word_r, word_s=word_s, word_t=word_t, word_u=word_u, word_v=word_v, word_w=word_w, word_x=word_x, word_y=word_y, word_z=word_z, incorrect=incorrect) 
    # return render_template('index.html')
    # else:
        # redirect(request.url)
 




# function to refresh page with fields all cleared
# @app.route('/submitted', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         # do stuff with valid form
#         # then redirect to "end" the form
#         return redirect(url_for('register'))

#     # initial get or form didn't validate
#     return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=7000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.

