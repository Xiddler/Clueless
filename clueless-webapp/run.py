#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
request.form['name']: use indexing if you know the key exists
request.form.get('name')
'''

from flask import Flask, url_for, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        # Submitted words
        data = request.form # in key:value pairs
        # data = request.args # in strings
        # word_a = data['word_a'] # nope!  
        # print(word_a)
        # print(data['name']) # nope! 
        print('*')
        # print(data.get('name')) # nope! 
        # neh = request.form.get('word_a') # nope! 
        # neh = request.form.get('value') # nope! 
        # neh = request.form.get('name') # nope! 
        # neh = request.form['word_a'] # nope! 
        # neh = request.form['name'] # nope! 
        word_a = request.form['booh'] # works!
        print(word_a)
        # print(data.get('word_a'))
        # word_a = data.get('a_word')
        # word_a = data.get('word_a')
        # word_a = data['word_a']
        # print(word_a)
        # word_b = data.get('b-word')
        # print(word_b)
        # word_c = data.get('c-word')
        # word_d = data['d-word']
        # word_e = data['e-word']
        # word_f = data['f-word']
        # word_g = data['g-word']
        # word_h = data['h-word']
        # word_i = data['i-word']
        # word_j = data['j-word']
        # word_k = data['k-word']
        # word_l = data['l-word']
        # word_m = data['m-word']
        # word_n = data['n-word']
        # word_o = data['o-word']
        # word_p = data['p-word']
        # word_q = data['q-word']
        # word_r = data['r-word']
        # word_s = data['s-word']
        # word_t = data['t-word']
        # word_u = data['u-word']
        # word_v = data['v-word']
        # word_w = data['w-word']
        # word_x = data['x-word']
        # word_y = data['y-word']
        # word_z = data['z-word']
        word_holder = []
        # word_holder.append(word_a)
        # word_holder.append(word_b)
        # word_holder.append(word_c)
        # print(word_holder)
        # print(data['Ent'])
        # myword_a = data['a_word']
        # word_holder.append(myword_a)
        # print(myword_a)
        # myword_b = data['b-word']
        # word_holder.append(myword_b)
        # print(myword_b)
        # print(word_holder[0:])
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

        # OUTPUT new snippet
        # conn = sqlite3.connect('words.db')
	# print("Opened database successfully")
        # cur = conn.cursor()
        # cur.execute("SELECT word FROM words ORDER BY id DESC; ")
        # cur.execute("SELECT word FROM words where id < 9; ")
	# all_words = cur.fetchall()
	# fetchall() returns a row list
	# test = cur.fetchone()
	# most_recent = [item[0] for item in all_snippets[0:2]]
	# word1 = all_words[0:1][0][0]
	# word2 = all_words[1:2][0][0]
	# word1 = all_words[2:3][0][0]
	# word2 = all_words[3:4][0][0]
	# conn.close()	
	# conn.close()
        # myword = word_holder[1]
        # output the entered word for my testing purposes
        # return render_template('index.html', word1=word1, word2=word2, myword1=myword1)
        # return render_template('index.html', word_a=word_a, word_b=word_b, word_c=word_c)
        return render_template('index.html', word_a=word_a)
        # return render_template('index.html')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=9000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.

