from app.web import web

from flask import render_template, request


@web.route('/')
def index():
    ua = request.headers.get('User-Agent')
    endpoint = request.endpoint
    blueprint = request.blueprint
    baseurl = request.base_url

    return render_template('index.html',
                           ua=ua,
                           endpoint=endpoint,
                           blueprint=blueprint,
                           baseurl=baseurl)
