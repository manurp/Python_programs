class Record:
    def __init__(self, **kw):
        self.__dict__.update(kw)
Colors = Record(alarm='red', warning='orange', normal='green')
print(Colors.alarm)
