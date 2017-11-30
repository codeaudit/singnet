import aiohttp_jinja2
import jinja2

from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp_jinja2 import APP_KEY as JINJA2_APP_KEY

from sn_agent.ui.settings import WebSettings

THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent

settings = WebSettings()


def setup_ui(app):
    template_path = str(THIS_DIR.joinpath('templates'))
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(template_path))
    app['static_root_url'] = '/static'
    #
    # app[JINJA2_APP_KEY].filters.update(
    #     url=reverse_url,
    #     static=static_url,
    # )

#
# @jinja2.contextfilter
# def reverse_url(context, name, **parts):
#     """
#     jinja2 filter for generating urls,
#     see http://aiohttp.readthedocs.io/en/stable/web.html#reverse-url-constructing-using-named-resources
#
#     Usage:
#
#       {{ 'the-view-name'|url }} might become "/path/to/view"
#
#     or with parts and a query
#
#       {{ 'item-details'|url(id=123, query={'active': 'true'}) }} might become "/items/1?active=true
#
#     see app/templates.index.jinja for usage.
#
#     :param context: see http://jinja.pocoo.org/docs/dev/api/#jinja2.contextfilter
#     :param name: the name of the route
#     :param parts: url parts to be passed to route.url(), if parts includes "query" it's removed and passed seperately
#     :return: url as generated by app.route[<name>].url(parts=parts, query=query)
#     """
#     app = context['app']
#
#     kwargs = {}
#     if 'query' in parts:
#         kwargs['query'] = parts.pop('query')
#     if parts:
#         kwargs['parts'] = parts
#     return app.router[name].url(**kwargs)
#
#
# @jinja2.contextfilter
# def static_url(context, static_file_path):
#     """
#     jinja2 filter for generating urls for static files. NOTE: heed the warning in create_app about "static_root_url"
#     as this filter uses app['static_root_url'].
#
#     Usage:
#       {{ 'styles.css'|static }} might become "http://mycdn.example.com/styles.css"
#
#     see app/templates.index.jinja for usage.
#
#     :param context: see http://jinja.pocoo.org/docs/dev/api/#jinja2.contextfilter
#     :param static_file_path: path to static file under static route
#     :return: roughly just "<static_root_url>/<static_file_path>"
#     """
#
#     return '{}/{}'.format(settings.STATIC_ROOT_URL.rstrip('/'), static_file_path.lstrip('/'))
