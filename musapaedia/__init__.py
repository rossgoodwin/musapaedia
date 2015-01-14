import json
import string
from random import choice as rc
from flask import Flask
from flask import render_template

app = Flask(__name__)

data = json.load( open('data.json', 'r') )

current_poem = rc(data)
user_keywords = []
user_poems = []
read_poems = []
liked_poems = []

@app.route("/")
def hello():
    current_poem = rc(data)
    return render_template("index.html", gberg_url="http://www.gutenberg.org/ebooks/"+current_poem['bookID'], poem=lb_replace(current_poem['text']))

@app.route("/y")
def yes():
    global current_poem
    global user_keywords
    global user_poems
    global read_poems
    global liked_poems
    
    liked_poems.append(current_poem)

    keyNo = len(current_poem['keywords'])/3
    user_keywords += current_poem['keywords'][:keyNo]

    for x, y in user_keywords:
        for doc in data:
            doc_keywords = [t[0] for t in doc['keywords']]
            if x in doc_keywords[:len(doc_keywords)/3] and not doc in user_poems:
                user_poems.append(doc)

    if len(user_poems) > 0:
        current_poem = rc(user_poems)
    else:
        current_poem = rc(data)

    return render_template("index.html", gberg_url="http://www.gutenberg.org/ebooks/"+current_poem['bookID'], poem=lb_replace(current_poem['text']))



@app.route("/done")
def done():
    f = open('mypoems.txt', 'w')

    i = 1
    for p in liked_poems:
        f.write(str(i)+". http://www.gutenberg.org/ebooks/"+p['bookID']+'\n\n'+p['text']+'\n\n\n\n')
        i += 1

    f.close()

    return "Poems written to mypoems.txt file!"


def lb_replace(text):
    text = string.replace(text, "\n", "<br />")
    text = string.replace(text, "\r", "")

    return text


if __name__ == "__main__":
    app.run()







