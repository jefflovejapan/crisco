#!/usr/bin/python

from flask import Flask, render_template, request, redirect
from crisco import shortener

app = Flask(__name__)  # What does this do?
a = shortener()
app.in_link = ''
app.out_link = ''


# Super hacky
@app.route('/<input_slug>', methods=['GET'])
def catchall(input_slug):
    url = a.lengthen(input_slug)
    print url
    if url is not None:
        return redirect(url, code=302)
    else:
        return redirect('/')


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/shorten', methods=['POST'])
def shortening():
    app.in_link = request.form['long_link']
    app.out_link = 'http://127.0.0.1:5000/' + a.shorten(app.in_link)
    return render_template('shorten.html',
                           short=app.out_link)


if __name__ == '__main__':
    app.run()
