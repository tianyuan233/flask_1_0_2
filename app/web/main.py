from app.web import web

from flask import render_template, request


@web.route('/')
def index():
    ua = request.headers.get('User-Agent')
    return render_template('index.html', ua=ua)
