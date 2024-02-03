import importlib
class superinvalidate:
    def __init__(self):
        self = self

    def invalidate(self):
       importlib.invalidate_caches.__builtins__

class run(superinvalidate):
    def __init__(self):
        super(run, self).__init__()

interact = run()
interact.invalidate()