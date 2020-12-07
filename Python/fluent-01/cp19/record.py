class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"<Record: {self.__dict__}>"


a = Record(x=10, b=20, c='oi')
print(a)
print(repr(a))
print(a.x)
print(a.b)
print(a.c)