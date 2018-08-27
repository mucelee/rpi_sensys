class SensorDataEntry(object):

    def __init__(self):
        print("init SensorDataEntry")
        self._isDirty = False

    def __setattr__(self, arg, value):
        if arg != "_isDirty":
            self._isDirty = True
        return super(SensorDataEntry, self).__setattr__(arg, value)

    def is_dirty(self):
        return self._isDirty

    def clear_dirty(self):
        self._isDirty = False