from tinydb import Query
import threading
import requests
import re
import logging
import json

logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)


class DomainThread(threading.Thread):
    def __init__(self, src, db, uuid):
        self.src = src
        self.db = db
        self.uuid = uuid
        threading.Thread.__init__(self)

    def run(self):
        content = Query()
        _log.info("cross-domain thread start: %s", self.uuid)
        if re.search(r'<cross-domain-policy>', requests.get(self.src + '/crossdomain.xml').text):
            domain = requests.get(self.src + '/crossdomain.xml').text
        else:
            domain = None
        _log.info("cross-domain thread return: %s", domain)
        data = {'domain': domain}
        self.db.update(data, content.uuid == self.uuid)



