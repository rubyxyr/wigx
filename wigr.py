from wig.wig import wig
from tinydb import Query
import threading
import logging
import json

logging.basicConfig(level=logging.DEBUG)
_log = logging.getLogger(__name__)


class WigrThread(threading.Thread):
    def __init__(self, src, db, uuid):
        self.src = src
        self.db = db
        self.uuid = uuid
        threading.Thread.__init__(self)

    def run(self):
        content = Query()
        args = {
            'url': self.src
        }
        _log.info("wig thread start: %s", self.uuid)
        w = wig(**args)
        w.run()
        data = {'wig': w.get_results()}
        _log.info("wig thread return: %s", data)
        self.db.update(data, content.uuid == self.uuid)


