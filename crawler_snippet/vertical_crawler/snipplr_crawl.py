
import threading
import lxml.html
import requests
import random
import itertools
import time
import hashlib

user_agent = [
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',

        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/6.0;'
        ' SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C) QQBrowser/6.14.15493.201' ,

        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)' ,

        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)' ,

        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1' ,

        'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) '
        'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
        ]

index_hash = set()
content_hash = set()

class SnipplrDownloader(threading.Thread):
    def __init__(self, queue, index):
        threading.Thread.__init__(self)
        self.queue = queue
        self.any_true = lambda predicate, sequence: True in itertools.imap(predicate, sequence)
        self.fi = open('./all_scrapy_urls' + "_%s"%index, 'w')
        self.urls = set()
        self.cnt = 0

    def run(self):
        while 1:
            url = self.queue.get()
            try:
                time.sleep(random.random())
                header = {
                        'User-Agent': random.choice(user_agent)
                        }
                resp = requests.get(url, headers = header)
                c_h = hashlib.md5(resp.content).hexdigest()
                if c_h in content_hash:
                    continue
                else:
                    content_hash.add(c_h)

                xparser = lxml.html.fromstring(resp.content)
                res = xparser.xpath("//@href")
                res.extend(xparser.xpath("//@src"))
                for url in res:
                    if self.any_true(url.endswith, ('.jpg', '.gif', '.png')) is False:
                        if url.startswith('http') is False:
                            url = 'http://snipplr.com/'  + url.lstrip('/')
                        else:
                            continue

                        h = hashlib.md5(url).hexdigest()
                        if not h in index_hash:
                            index_hash.add(h)
                            self.queue.put(url)

                            print url
                            self.urls.add(url)
                            if len(self.urls) > 300:
                                self.fi.write( '%s-%s' % (self.cnt * 300, self.cnt * 300 + 299) )
                                self.cnt += 1
                                for url in self.urls:
                                    self.fi.write(url)
                                    self.fi.write('\n')
                                self.fi.write('\n')
                                self.fi.flush()
                                self.urls.clear()

            except Exception as e:
                print e

            self.queue.task_done()

        def __del__(self):
            self.fi.close()

class SnipplrAnalyze(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        from Queue import Queue
        self.queue = Queue()
        self.queue.put('http://snipplr.com/all/tags/scrapy/')
        self.client = [SnipplrDownloader(self.queue, i) for i in xrange(10)]

    def tearDown(self):
        for i in self.client: del i
        pass

    def test_main(self):
        for client in self.client:client.setDaemon(True)
        for client in self.client:client.start()
        self.queue.join()

if __name__ == "__main__":
    unittest.main()
