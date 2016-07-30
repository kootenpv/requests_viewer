import requests
import json
import time
import webbrowser


def wrap_json_into_html(x):
    return "<html><body><code style='white-space: pre-wrap;'>{}</code></body></html>".format(x)


def view_request(r):
    js = json.dumps(r.json(), indent=4)
    fname = '/tmp/' + str(hash(js)) + '.html'
    with open(fname, 'w') as f:
        f.write(wrap_json_into_html(js))
    webbrowser.open('file://' + fname)
    time.sleep(1)
