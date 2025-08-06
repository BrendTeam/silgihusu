import threading
from sqlalchemy import func, distinct, Column, String, UnicodeText, Integer
try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError


class Warns(BASE):
    __tablename__ = "warns"
    user_id = Column(Integer, primary_key=True)
    num_warn = Column(Integer, default=0)

    def __init__(self, user_id, num_warn):
        self.user_id = user_id
        self.num_warn = num_warn

    def __repr__(self):
        return "<Warns filter '%s' for %s>" % (self.uid, self.warn)

    def __eq__(self, other):
        return bool(isinstance(other, Warns)
                    and self.user_id == other.user_id
                    and self.num_warn == other.num_warn)


Warns.__table__.create(checkfirst=True)

EMR_INSERTION_LOCK = threading.RLock()

def elave_warn(userid):
    with EMR_INSERTION_LOCK:
        try:
            DIQQET = SESSION.query(Warns).filter(Warns.user_id == userid).first()
            wsayi = int(DIQQET.num_warn)
            SESSION.query(Warns).filter(Warns.user_id == userid).delete()
        except:
            wsayi =  0

        wsayi += 1
        emr = Warns(userid, wsayi)
        SESSION.merge(emr)
        SESSION.commit()

def getir_warn(userid):
    try:
        DIQQET = SESSION.query(Warns).filter(Warns.user_id == userid).first()
        return DIQQET.num_warn
    except:
        return 0
    

def sil_warn(userid):
    try:
        wsayi = SESSION.query(Warns).filter(Warns.user_id == userid).first().num_warn
        if wsayi == 0:
            return False
        nsayi = wsayi - 1
        SESSION.query(Warns).filter(Warns.user_id == userid).delete()

        diqqet = Warns(userid, nsayi)
        SESSION.merge(diqqet)
        SESSION.commit()
        return True
    except:
        return False
    return True

def toplu_sil_warn(userid):
    try:
        diqqet = Warns(userid, 0)
        SESSION.merge(diqqet)
        SESSION.commit()
    except:
        return False
    return True
