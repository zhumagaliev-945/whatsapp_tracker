from enum import Enum


class Status(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    IS_WRITING = 'is_writing'
    NOT_DEFINED = 'not_defined'
