#!/usr/bin/python

from flask import Flask, render_template, request, redirect
from crisco import shortener
import re

app = Flask('crisco')  # What does this do?
a = shortener()


# Super hacky
@app.route('/<input_slug>', methods=['GET'])
def catchall(input_slug):
    url = a.lengthen(input_slug)
    print url
    match = re.match('http(s?)://', url)
    if match:
        return redirect(url)
    elif url is not None:
        return redirect('http://' + url)
    else:
        return redirect('/')


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/shorten', methods=['POST'])
def shortening():
    in_link = request.form['long_link']
    out_link = 'http://127.0.0.1:5000/' + a.shorten(in_link)
    return render_template('shorten.html',
                           short=out_link)


if __name__ == '__main__':
    app.run(debug=True)
