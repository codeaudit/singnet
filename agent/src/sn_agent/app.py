import asyncio
import logging

import uvloop
from aiohttp import web

from sn_agent.database import setup_db
from sn_agent.jinja import setup_jinja
from sn_agent.log import setup_logging
from sn_agent.network import setup_network
from sn_agent.routes import setup_routes
from sn_agent.session import setup_session
from sn_agent.worker import setup_workers

logger = logging.getLogger(__file__)


def create_app(loop):
    # Significant performance improvement: https://github.com/MagicStack/uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    app = web.Application()

    setup_logging()
    setup_db(app)
    # setup_middleware(app)
    setup_jinja(app)
    setup_session(app)
    setup_routes(app)

    setup_network(app)
    setup_workers(app)

    app['name'] = 'SingularityNET Agent'
    return app
