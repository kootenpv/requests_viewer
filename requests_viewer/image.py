import time
import requests
import webbrowser
import base64


def wrap_img_into_html(content_type, x):
    return '<html><body><img src="data:{};base64,{}"</body></html>'.format(content_type, x.decode("utf8"))


def view_request(r):
    fname = '/tmp/' + str(hash(r)) + '.html'
    with open(fname, 'w') as f:
        f.write(wrap_img_into_html(r.headers['Content-Type'], base64.b64encode(r.content)))
    webbrowser.open('file://' + fname)
    time.sleep(1)
