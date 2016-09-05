from tinydb import TinyDB, Query
from headers import HeadThread
from wigr import WigrThread
from robot import RobotThread
from domain import DomainThread
import time
import threading
import logging
import uuid

logging.basicConfig(level=logging.DEBUG)
_log = logging.getLogger(__name__)


class Wigx:

    def __init__(self):
        self.db = TinyDB('db.json')

    def add_target(self, url):
        details = Query()
        if self.db.search(details.subdomin == url):
            id = self.db.get(details.subdomin == url)['uuid']
        else:
            id = str(uuid.uuid4())
            self.db.insert({'uuid': id, 'subdomin': url})
        self.start(id)
        _log.info("Waiting.........................")
        return id

    def start(self, uuid):
        HeadThread(url, self.db, uuid).start()
        DomainThread(url, self.db, uuid).start()
        RobotThread(url, self.db, uuid).start()
        WigrThread(url, self.db, uuid).start()

    def get_result(self, uuid):
        details = Query()
        result = self.db.search(details.uuid == uuid)
        return result

if __name__ == '__main__':
    url = "http://www.studysec.com/"
    wigx = Wigx()
    wigx.add_target(url)

