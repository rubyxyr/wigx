from tinydb import Query
import threading
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)


class HeadThread(threading.Thread):
    def __init__(self, src, db, uuid):
        self.src = src
        self.db = db
        self.uuid = uuid
        threading.Thread.__init__(self)

    def run(self):
        _log.info("header thread start: %s", self.uuid)
        content = Query()
        resp = requests.get(self.src)
        _log.info("header thread return: %s", resp.headers)
        data = {'header': json.dumps(dict(resp.headers))}
        self.db.update(data, content.uuid == self.uuid)
