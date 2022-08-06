class SpotTheError:
    """
    There is a place where this code can raise an exception… Can you spot it?
    """

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def __repr__(self):
        return f"{self.foo}, {self.bar}"
