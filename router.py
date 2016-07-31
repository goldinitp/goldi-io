import logging
import webapp2

from controllers import blog
from webapp2_extras import jinja2
from webapp2_extras import routes


# method for handling errors
def error(request, response, exception):
    logging.exception(exception)
    params = {
        'error': exception
    }
    jinja = jinja2.get_jinja2()
    response.write(jinja.render_template('error.html', **params))

app = webapp2.WSGIApplication([
    routes.DomainRoute('goldi.io', [
        routes.RedirectRoute(
            '/',
            handler=blog.MainHandler,
            name='mainHandler'
        )
    ]),
    routes.DomainRoute('blog.goldi.io', [
        routes.RedirectRoute(
            '/',
            handler=blog.BlogHandler,
            name='blogHandler'
        )
    ])
], debug=True)
