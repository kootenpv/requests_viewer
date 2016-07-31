## requests_viewer

The idea is that `requests_viewer` can tell us information about our requests-objects quickly.

It opens up an HTML page with information for the request.

```python
import requests
from requests_viewer.web import view_request
view_request(requests.get("https://xkcd.com/"))

# or

from requests_viewer import main
main("https://xkcd.com/") # considers different mime types
```

### Main features

- HTML page is being shown as how the crawler sees it
    * Can extract the domain and hot-link so that it looks almost indistuinguishable
- Contains other nice functions to show lxml tree nodes
- Can visually show diffs between 2 html pages / trees

```python
from requests_viewer.web import view_diff_tree, get_tree
url1 = "http://xkcd.com/"
url2 = "http://xkcd.com/1/"
tree1 = get_tree(url1)  # get tree from request object directly
tree2 = get_tree(url2)  # could instead use `make_tree` if you already have a req
view_diff_tree(tree1, tree2)
```

Results in:

<p align="center">
<img src="https://raw.githubusercontent.com/kootenpv/requests_viewer/master/resources/screenshot1.png" width="80%" />
</p>

### Installation

    pip install requests_viewer
    pip3 install requests_viewer

Note that in order to do the real fancy stuff, you should install:

    pip install requests_viewer[fancy]
    pip3 install requests_viewer[fancy]

this will install `lxml`, `bs4` and `tldextract`.

### Types it can show currently:

- text/html
- image/*
- application/json

### Usability

Some example `web.py` functions:

``` python
def slugify(value):
def view_request(r, domain=None):
def view_html(x):
def view_node(node, attach_head=False, question_contains=None):
def view_tree(node):
def view_diff_tree(tree1, tree2, url, diff_method):
def view_diff_html(html1, html2, url, diff_method):
def view_diff(html1, html2, tree1, tree2, url, diff_method):
def make_parent_line(node, attach_head=False, question_contains=None):
def extract_domain(url):
def make_tree(html, domain=None):
def get_tree(url, domain=None):
def get_local_tree(url, domain=None):
```

### Contribute

This package is very small at the moment. I very much encourage you to contribute:

- Most likely we will want to show headers on the top of the package (html)
