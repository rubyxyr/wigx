from tinydb import Query
import threading
import re
import requests
import logging
import json

logging.basicConfig(level=logging.DEBUG)
_log = logging.getLogger(__name__)


class RobotThread(threading.Thread):
    def __init__(self, src, db, uuid):
        self.src = src
        self.db = db
        self.uuid = uuid
        threading.Thread.__init__(self)

    def run(self):
        _log.info("robot thread start: %s", self.uuid)
        content = Query()
        if re.search(r'User-Agent:', requests.get(self.src + '/robot.txt').text):
            robot = requests.get(self.src + '/robot.txt').text
        else:
            robot = None
        _log.info("robots thread return: %s", robot)
        data = {'robot': robot}
        self.db.update(data, content.uuid == self.uuid)



