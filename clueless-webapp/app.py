#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask, url_for, render_template, request, redirect
import sqlite3
from config import Config
from string import ascii_lowercase as alfbet # lowercase letters of the alphabet built in
from collections import OrderedDict

from check_words import obeys_rule

app = Flask(__name__)
app.config.from_object(Config) # Secret key in config.py
secret_key = app.config['SECRET_KEY']

class Constraints:
    """ class to set the rules of the game """  

    def __init__(self, num, level, rule, time):

        self.num = num
        self.level = level
        self.rule = rule
        self.time = time
        # self.game = f"# {self.num} Level: {self.level} Rule: {self.rule} Time allowed: {self.time}"
        self.game = "# {0} Level: {1} Rule: {2} Time allowed: {3}".format( self.num, self.level, self.rule, self.time)

constraints = Constraints(3, "Easy", "Key letter in first AND last position", "4 mins")

num = constraints.num
level = constraints.level
rule = constraints.rule
time = constraints.time


def sanitized_input(alist):
    """ takes a list and makes all elements into lowercase and also strips leading and trailing whitespaces"""
    cleaned_input = []
    for user_input in alist:
        user_input = user_input.lower()
        user_input = user_input.strip()
        cleaned_input.append(user_input)
    return cleaned_input


@app.route('/', methods=['GET', 'POST'])
def index():
    # Welcome page with constraints
    return render_template('index.html', num=num, level=level, rule=rule, time=time)



@app.route('/game', methods=['GET', 'POST'])
def game():
    print("in the /game route now")
    # The present game
    # loaded when the player presses enter in any of the input boxes or presses the submit button
    if request.method == 'POST': 
        data = request.form # in key:value pairs
        print(data)
        print(num)

        word_holder = [] # initialise list of words entered by user - will be used to store the users words

        word_a = data.get('aword') # data['aword'] requires an initial value in the input field
        word_b = data.get('bword')
        word_c = data.get('cword') 
        word_d = data.get('dword')
        word_e = data.get('eword')
        word_f = data.get('fword')
        word_g = data.get('gword')
        word_h = data.get('hword')
        word_i = data.get('iword')
        # word_j = data.get('jword')
        word_k = data.get('kword')
        word_l = data.get('lword')
        word_m = data.get('mword')
        word_n = data.get('nword')
        word_o = data.get('oword')
        word_p = data.get('pword')
        # word_q = data.get('qword')
        word_r = data.get('rword')
        word_s = data.get('sword')
        word_t = data.get('tword')
        # word_u = data.get('uword')
        # word_v = data.get('vword')
        word_w = data.get('wword')
        # word_x = data.get('xword')
        word_y = data.get('yword')
        # word_z = data.get('zword')
        # word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_j, word_k, word_l, word_m, word_n, word_o, word_p, word_q, word_r, word_s, word_t, word_u, word_v, word_w, word_x, word_y, word_z, ])
        word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_k, word_l, word_m, word_n, word_o, word_p, word_r, word_s, word_t, word_w, word_y])
        word_holder = sanitized_input(word_holder)

        def get_db_words():

            """ method to make a list of the words in the database """   

            conn = sqlite3.connect('words.db')
            print("Opened database successfully")
            cur = conn.cursor()
            cur.execute("SELECT word FROM words;")
            all_words = cur.fetchall()
            # print(len(all_words)) # 88280
            # check if all words inserted are in the database (ie the 'dictionary')
            all_items = [item[0] for item in all_words[0:88280]] # make into a regular list
            conn.close()	
            print("Closed database successfully")
            return all_items

        get_db_words() 

        print("Checkpoint 1") 

        # Check if user's words are in the database
        correct = []
        incorrect = []
        def in_database():
            """ method to check if user's word is in database """
            all_items = get_db_words()
            for word in word_holder:
                if word not in all_items and word != "None":
                    incorrect.append(word) # incorrect words added to list for display on the webpage
                else:
                    correct.append(word)

        in_database() # call method to check that word is in database

        # TODO check words follow the rule
        # Game 3: words start and end with key letter

        # print(word_holder)
        try:
            mydict = obeys_rule(word_holder) # calls the external app to confirm words follow the rule for Game 3 - allows Y or N adjacent to each word
            print("mydict", mydict)
        except:
            print("there is an problem with mydict or obeys_rules")
        finally:
            pass

        print("mydict again ==>", mydict)
        print("mydict elem", mydict['d'])




        print("word_holder", word_holder)

        # print(word) # correct words printed to terminal
        print(incorrect)
        print(correct)

        # return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_j=word_j, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_q=word_q, word_r=word_r, word_s=word_s, word_t=word_t, word_u=word_u, word_v=word_v, word_w=word_w, word_x=word_x, word_y=word_y, word_z=word_z, word_holder=word_holder, correct=correct,  incorrect=incorrect,  rule=rule, time=time )
        return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_r=word_r, word_s=word_s, word_t=word_t, word_w=word_w, word_y=word_y, word_holder=word_holder, correct=correct,  incorrect=incorrect,  rule=rule, time=time, mydict=mydict)

     # Input fields are blank if loaded by pressing the PLAY! button in index.html
    else:
        mydict = OrderedDict([('a', ''), ('b', ''), ('c', ''), ('d', ''), ('e', ''), ('f', ''), ('g', ''), ('h', ''), ('i', ''), ('k', ''), ('l', ''), ('m', ''), ('n', ''), ('o', ''), ('p', ''), ('r', ''), ('s', ''), ('t', ''), ('w', ''), ('y', '')])
        return render_template('game.html', num=num, level=level, rule=rule, time=time, mydict=mydict) 

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.
    # app.run(host ='192.168.1.103', port=5000, debug=True)  
    # app.run(host ='192.168.1.103', port=5000, debug=False)  
    # app.run(host ='127.0.0.1', port=5000, debug=False)  


#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect
import sqlite3
from config import Config
from string import ascii_lowercase as net # lowercase letters of the alphabet built in
from collections import OrderedDict

from check_words import obeys_rule # currently only checks for game 3 constraints

app = Flask(__name__)
app.config.from_object(Config) # Secret key in config.py
secret_key = app.config['SECRET_KEY']

class Constraints:
    """ class to set the rules of the game """  

    def __init__(self, num, level, rule, time):

        self.num = num
        self.level = level
        self.rule = rule
        self.time = time
        # self.game = f"# {self.num} Level: {self.level} Rule: {self.rule} Time allowed: {self.time}"
        self.game = "# {0} Level: {1} Rule: {2} Time allowed: {3}".format( self.num, self.level, self.rule, self.time)

constraints = Constraints(3, "Easy", "Key letter in first AND last position", "4 mins")

num = constraints.num
level = constraints.level
rule = constraints.rule
time = constraints.time

def sanitized_input(alist):
    """ takes a list and makes all elements into lowercase and also strips leading and trailing whitespaces"""
    cleaned_input = []
    for user_input in alist:
        user_input = user_input.lower()
        user_input = user_input.strip()
        cleaned_input.append(user_input)
    return cleaned_input


@app.route('/', methods=['GET', 'POST'])
def index():
    # Welcome page with constraints
    return render_template('index.html', num=num, level=level, rule=rule, time=time)



@app.route('/game', methods=['GET', 'POST'])
def game():
    # print("in the /game route now")
    # The present game
    # loaded when the player presses enter in any of the input boxes or presses the submit button
    if request.method == 'POST': 
        data = request.form # in key:value pairs
        # print(data)
        # print(num)

        word_holder = [] # initialise list of words entered by user - will be used to store the users words

        word_a = data.get('aword') # data['aword'] requires an initial value in the input field
        word_b = data.get('bword')
        word_c = data.get('cword') 
        word_d = data.get('dword')
        word_e = data.get('eword')
        word_f = data.get('fword')
        word_g = data.get('gword')
        word_h = data.get('hword')
        word_i = data.get('iword')
        # word_j = data.get('jword')
        word_k = data.get('kword')
        word_l = data.get('lword')
        word_m = data.get('mword')
        word_n = data.get('nword')
        word_o = data.get('oword')
        word_p = data.get('pword')
        # word_q = data.get('qword')
        word_r = data.get('rword')
        word_s = data.get('sword')
        word_t = data.get('tword')
        # word_u = data.get('uword')
        # word_v = data.get('vword')
        word_w = data.get('wword')
        # word_x = data.get('xword')
        word_y = data.get('yword')
        # word_z = data.get('zword')
        # word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_j, word_k, word_l, word_m, word_n, word_o, word_p, word_q, word_r, word_s, word_t, word_u, word_v, word_w, word_x, word_y, word_z, ])
        word_holder.extend([word_a, word_b, word_c, word_d, word_e, word_f, word_g, word_h, word_i, word_k, word_l, word_m, word_n, word_o, word_p, word_r, word_s, word_t, word_w, word_y])
        print("wooooooooooooooooooooooooooo")
        word_holder = sanitized_input(word_holder)
        print("User's words", word_holder)


        def get_db_words():

            """ method to make a list of the words in the database """   

            conn = sqlite3.connect('words.db')
            # print("Opened database successfully")
            cur = conn.cursor()
            cur.execute("SELECT word FROM words;")
            all_words = cur.fetchall()
            # print(len(all_words)) # 88280
            # check if all words inserted are in the database (ie the 'dictionary')
            all_items = [item[0] for item in all_words[0:88280]] # make into a regular list
            conn.close()	
            # print("Closed database successfully")
            return all_items

        get_db_words() 

        print("Checkpoint 1") 


        # Check if user's words are in the database
        correct = []
        incorrect = []
        def in_database():
            """ method to check if user's word is in database """
            all_items = get_db_words()
            for word in word_holder:
                if word not in all_items and word != "None":
                    incorrect.append(word) # incorrect words added to list for display on the webpage
                    sanitized_input(incorrect)
                else:
                    correct.append(word) # make a list of user's words that ARE in the database
                    sanitized_input(correct)

        in_database() # call method to check that word is in database
        print("Correct", correct)



        # correct = sanitized_input(correct) # put this in check_words?



        # test out a try except rule
        # try:
            # mydict = obeys_rule(word_holder) # calls the external module to confirm words follow the rule for Game 3 - allows Y or N adjacent to each word
            # print("mydict", mydict)
            # return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_r=word_r, word_s=word_s, word_t=word_t, word_w=word_w, word_y=word_y, word_holder=word_holder, correct=correct,  incorrect=incorrect,  rule=rule, time=time, mydict=mydict)
        # except:
            # print("there is a problem with mydict or obeys_rules")

        if word_holder:
            mydict = obeys_rule(word_holder) # calls the external module to confirm words follow the rule for Game 3 - allows Y or N adjacent to each word
        else: 
            print("there was a woo woo problem")

        # mydict = mydict
        # print("mydict again ==>", mydict)
        # print("mydict elem", mydict['d'])




        # print("word_holder", word_holder)

        # print(word) # correct words printed to terminal
        # print(incorrect)
        # print(correct)

        # return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_j=word_j, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_q=word_q, word_r=word_r, word_s=word_s, word_t=word_t, word_u=word_u, word_v=word_v, word_w=word_w, word_x=word_x, word_y=word_y, word_z=word_z, word_holder=word_holder, correct=correct,  incorrect=incorrect,  rule=rule, time=time )
        return render_template('game.html', word_a=word_a, word_b=word_b, word_c=word_c, word_d=word_d, word_e=word_e, word_f=word_f, word_g=word_g, word_h=word_h, word_i=word_i, word_k=word_k, word_l=word_l, word_m=word_m, word_n=word_n, word_o=word_o, word_p=word_p, word_r=word_r, word_s=word_s, word_t=word_t, word_w=word_w, word_y=word_y, word_holder=word_holder, correct=correct,  incorrect=incorrect,  rule=rule, time=time, mydict=mydict)

     # Input fields are blank if loaded by pressing the PLAY! button in index.html
    else: # call 'blank slate' on pressing PLAY button - a GET request as opposed to POST
        mydict = OrderedDict([('a', ''), ('b', ''), ('c', ''), ('d', ''), ('e', ''), ('f', ''), ('g', ''), ('h', ''), ('i', ''), ('k', ''), ('l', ''), ('m', ''), ('n', ''), ('o', ''), ('p', ''), ('r', ''), ('s', ''), ('t', ''), ('w', ''), ('y', '')])
        return render_template('game.html', num=num, level=level, rule=rule, time=time, mydict=mydict) # returns BLANK mydict if the method is NOT POST i.e. a start of play.







if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True) # '0.0.0.0' allows browsing from other devices on the lan.
    # app.run(host ='192.168.1.103', port=5000, debug=True)  
    # app.run(host ='192.168.1.103', port=5000, debug=False)  
    # app.run(host ='127.0.0.1', port=5000, debug=False)  


