import datetime
import random
import re
import string
import json

import webapp2
from google.appengine.api import mail
from webapp2_extras import jinja2
from webapp2_extras import routes
from models import blogModel

# base handler
class BaseHandler(webapp2.RequestHandler):
    """Base handler for webpage"""

    @webapp2.cached_property
    def jinja2(self):
        """Returns a Jinja2 renderer cached in the app registry."""
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **params):
        """Renders a template and writes the result to the response."""
        temp = self.jinja2.render_template(_template, **params)
        self.response.write(temp)

    def send_email(self, emailTo, emailSubject, emailBody):
        """method to send mail"""
        mail.send_mail(sender=config.admin['admin_mail'],
                       to=emailTo,
                       subject=emailSubject,
                       body=emailBody)
        return

class MainHandler(BaseHandler):
    def get(self):
        params = {
            'page': 'Goldi Kumar'
        }
        self.render_response('home.html', **params)

class BlogHandler(BaseHandler):
    def get(self):
        blogPosts = blogModel.Article.query().fetch(20)
        params = {
            'page': 'Goldi Kumar',
            'blogPosts': blogPosts
        }
        self.render_response('blog.html', **params)


class BlogWriteHandler(BaseHandler):
    """docstring for BlogWriteHandler"""
    def get(self):
        params = {
            'page': 'Goldi Kumar'
        }
        self.render_response('write.html', **params)

    def post(self):
        params = {
            'page': 'Goldi Kumar'
        }
        title = self.request.get('title')
        content = self.request.get('content')
        save = blogModel.Article(title = title, content = content)
        save.put()
        # self.redirect('/')

# class BlogPostHandler(BaseHandler):
#     """docstring for BlogPostHandler"""
#     def get(self):
#         params = {
#             'page': 'Goldi Kumar'
#         }
#         title = 'First test'
#         content = 'this is my first blog post'
#         save = blogModel.Article(title = title, content = content)
#         save.put()
#         self.render_response('blog.html', **params)
