#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        # Submitted words
        data = request.form # in key:value pairs
        print(data)
        word_a = data['aword'] # works!
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
        word_holder = []
        word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_j, word_k, word_l, word_m, word_n, word_o, word_p, word_q, word_r, word_s, word_t, word_u, word_v, word_w, word_x, word_y, word_z, ])
        print(word_holder)

        # if request.method == 'POST':
            # if data['Ent'] in request.form:
                # word-holder.append(word_1)
            # if data['submit_button'] == 'Ent':
                # put the entered word in a list for later processing
                # word-holder.append(word_1)
            # elif data['submit_button'] == 'Chk':
                # conn = sqlite3.connect('words.db')
                # pass # check if the entered word is in the database table
        # else:
            # pass # unknown

        # OUTPUT - compare entered words to words in database
        conn = sqlite3.connect('words.db')
        print("Opened database successfully")
        cur = conn.cursor()
        # cur.execute("SELECT word FROM words ORDER BY id DESC; ")
        cur.execute("SELECT word FROM words;")
        all_words = cur.fetchall()
        # print(len(all_words)) # 88280
        # print(type(all_words)) # class list
        # fetchall() returns a row (in a list)
        # test = cur.fetchone()
        # print(test)
        # most_recent = [item[0] for item in all_words[0:200]]
        # print(most_recent)
        # check if all words inserted are in the words table (ie the 'dictionary')
        all_items = [item[0] for item in all_words[0:88280]]
        # print(type(all_words)) # class list
        # print(all_words[0]) # class list [('a', 'b', ...)]
        # print(all_items[0]) # class list ['a', 'b', ...]
        # print(type(all_items)) # class list
        correct = []
        incorrect = []
        for word in word_holder:
            if word in all_items:
                correct.append(word)
                print(word, "Correct")
            else: 
                incorrect.append(word)
                print("Not in our database")
        




	# word1 = all_words[0:1][0][0]
	# word2 = all_words[1:2][0][0]
        # print(word1)
        # print(word2)
	# word1 = all_words[2:3][0][0]
	# word2 = all_words[3:4][0][0]
	# conn.close()	
	# conn.close()
        # myword = word_holder[1]
        # output the entered word for my testing purposes
        # return render_template('index.html', word1=word1, word2=word2, myword1=myword1)
        # return render_template('index.html', word_a=word_a, word_b=word_b, word_c=word_c)
        return render_template('index.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_j=word_j, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_q=word_q, word_r=word_r, word_s=word_s, word_t=word_t, word_u=word_u, word_v=word_v, word_w=word_w, word_x=word_x, word_y=word_y, word_z=word_z, correct=correct, incorrect=incorrect) 
        # return render_template('index.html') 


# function to refresh page with fields all cleared
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         # do stuff with valid form
#         # then redirect to "end" the form
#         return redirect(url_for('register'))

#     # initial get or form didn't validate
#     return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=9000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.

