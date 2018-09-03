class BaseFiwareClass(object):

    def __init__(self):
        self._isDirty = False

    def is_dirty(self):
        return False

    def clear_dirty(self):
        self._isDirty = False
