#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(self.request.path)
        logging.info("Test")
        try:
            template = JINJA_ENVIRONMENT.get_template('templates%s.html' % self.request.path)
            self.response.write(template.render({'name': self.request.path}))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'name': 'index'}))


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'name': '/contact'}))

    def post(self):
        if self.request.get('name') == 'Colleen' and self.request.get('pw') == 'pass':
            template = JINJA_ENVIRONMENT.get_template('templates/contacted.html')
            self.response.write(template.render({'name': '/contact'}))
        else:
            logging.info(
                "********BAD LOGIN ATTEMPT: " + self.request.get('name') + " " + self.request.get('pw') + "********")
            template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
            self.response.write(template.render({'name': '/contact', 'msg': 'Bad credentials. Try again.'}))


app = webapp2.WSGIApplication([
    ('/contact', LoginHandler),
    ('/.*', IndexHandler)
], debug=True)
