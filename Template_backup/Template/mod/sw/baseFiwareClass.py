class BaseFiwareClass(object):
    _publisher = []

    def attach_publisher(self, publisher):
        if(publisher not in self._publisher):
            self._publisher.append(publisher)

    def dettach_publisher(self, publisher):
        if(publisher in self._publisher):
            self._publisher.remove(publisher)


    # once an attribute has been changed, update and publish it
    def __setattr__(self, arg, value):
        if(self._publisher is not None):
            if(len(self._publisher)):
                for publisher in self._publisher:
                    publisher.Update(self, arg, value);
        return super(BaseFiwareClass, self).__setattr__(arg, value)
