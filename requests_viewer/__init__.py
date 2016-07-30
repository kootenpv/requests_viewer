""" requests_viewer; able to show how requests look like """

__project__ = 'requests_viewer'
__version__ = '0.0.0'

from requests_viewer.main import main

try:
    from requests_viewer.web import get_tree
    from requests_viewer.web import view_tree
except ImportError:
    print("Cannot import `lxml`, limited functionality.")
