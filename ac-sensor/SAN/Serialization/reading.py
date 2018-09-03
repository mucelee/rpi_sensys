import entityAttribute

class Reading(object):
    def __init__(self, _object):
        self.__dict__.clear()
        self.reading = entityAttribute.EntityAttribute(_object.reading)
        self.modifiedTime = entityAttribute.EntityAttribute(_object.modifiedTime, _object._metadata_modifiedTime)
        # for key, value in _object.__dict__.iteritems():
        #     if str(key).startswith('_', 0, 1):
        #         pass
        #     else:
        #         self.__dict__[key] = entityAttribute.EntityAttribute(value, {})