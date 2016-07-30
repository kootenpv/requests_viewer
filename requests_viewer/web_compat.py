import requests
import time
import webbrowser


def view_request(r):
    html = r.text
    fname = '/tmp/' + str(hash(html)) + '.html'
    with open(fname, 'w') as f:
        f.write(html)
    webbrowser.open('file://' + fname)
    time.sleep(1)
