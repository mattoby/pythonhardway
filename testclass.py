class Thing(object):
    def __init__(self):
        self.attr = 1

    def dothing(self):
        print self.attr

class Thing2(object):
    attr = 1
    print attr
    def dothing(self):
        self.attr = self.attr + 1
        print self.attr