class NeverWrong:
    """
    You'll never find an attribute this class doesn't have!
    """

    def __getattribute__(self, name):
        return "Howdy!"


a = NeverWrong()
assert a.x == "Howdy!"
