class BaseFiwareClass(object):

    def __init__(self):
        self._isDirty = False
        """ self._ignored_changes = { "_updates", "_publishers" }
        self._updates = dict()
        self._publishers = [] """

    """ def attach_publisher(self, publisher):
        if(publisher not in self._publishers):
            self._publishers.append(publisher)

    def dettach_publisher(self, publisher):
        if(publisher in self._publishers):
            self._publishers.remove(publisher) """

    def is_dirty(self):
        return False

    def clear_dirty(self):
        self._isDirty = False

    """ # once an attribute has been changed, update and publish it
    def __setattr__(self, arg, value):
        print("setting attribute in BaseFiwareClass")
        if arg != "_ignored_changes" and arg not in self._ignored_changes:
            self._updates[arg] = value
            self.publish_changes()
        return super(BaseFiwareClass, self).__setattr__(arg, value)

    def publish_changes(self):
        if self._publishers is not None:
            if len(self._publishers):
                for publisher in self._publishers:
                    publisher.Update(self, self._updates) """
