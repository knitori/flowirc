__author__ = 'Olle Lundberg'


class MessageBase:
    _type = None
    @classmethod
    def type(cls):
        return cls._type if cls._type \
            else cls.__name__.upper().replace('MESSAGE', '')
