import datetime
import random
import re
import string
import json

import webapp2
from google.appengine.api import mail
from webapp2_extras import jinja2
from webapp2_extras import routes
from google.appengine.ext import ndb

class Article(ndb.Model):
    """Represents article written"""
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    soft_deleted = ndb.BooleanProperty(default=False)
