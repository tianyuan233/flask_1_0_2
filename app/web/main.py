from flask.helpers import get_root_path, get_env

from app.web import web

from flask import render_template, request, flash


@web.route('/')
def index():
    ua = request.headers.get('User-Agent')
    endpoint = request.endpoint
    blueprint = request.blueprint
    baseurl = request.base_url
    rule = request.url_rule
    args = request.args
    #ImmutableMultiDict([('a', '123')])

    args_dict = request.args.to_dict()
    #{'a': '123'}
    flash("flash test")
    print(get_env())

    return render_template('index.html',
                           ua=ua,
                           endpoint=endpoint,
                           blueprint=blueprint,
                           baseurl=baseurl)
