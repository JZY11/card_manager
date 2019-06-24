from collections import defaultdict
import re

class NaiveFilter():
    def __init__(self):
        self.keywords = set([])

    def parse(self,path):
        for keyword in open(path):
            self.keywords.add(keyword.strip().decode('utf-8').lower())

    def filter(self, message, repl="*"):
        message = unicode(message).lower()
        for kw in self.keywords:
            message = message.replace(kw,repl)
        return message



class BSFilter:
    def __init__(self):
        self.keywords = []
        self.kwsets = set([])
        self.bsdict = defaultdict(set)
        self.pat_en = re.compile(r'^[0-9a-zA-Z]+$')  # english parse or not


    def add(self,keyword):
        if not isinstance(keyword,unicode):
            keyword = keyword.decode('utf-8')

        keyword = keyword.lower()
        if keyword not in self.keywords:
            self.keywords.append(keyword)
            self.kwsets.add(keyword)
            index = len(self.keywords) - 1
            for word in keyword.split():
                if self.pat_en.search(word):
                    self.bsdict[word].add(index)
                else:
                    for char in word:
                        self.bsdict[char].add(index)


    def parse(self,path):
        with open(path, "r") as f:
            for keyword in f:
                self.add(keyword.strip())

    def filter(self,message,repl="*"):
        if not isinstance(message,unicode):
            message = message.decode('utf-8')
        message = message.lower()
        for word in message.split():
            if self.pat_en.search(word):
                message = message.replace(self.keywords[index],repl)
            else:
                for char in word:
                    for index in self.bsdict[char]:
                        message = message.replace(self.keywords[index],repl)
        return message


