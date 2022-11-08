# Crisco

Crisco is a simple URL shortener written in Python. It relies on a [base-62 conversion](https://gist.github.com/bhelx/778542) to turn the rowid of a SQLite database into an alphanumeric string (the short link) and back again.

## Install

Just clone the source code into a convenient folder. Run it from the command line with

`python crisco.py`

## Use

Once the server is running, you can connect on the address and port printed to the screen. Posting a long URL routes you to a different page that's waiting with a short URL.

## Status

This was a quick one-off project over a few days at Hacker School and isn't being actively developed.

