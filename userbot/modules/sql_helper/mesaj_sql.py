import threading
from sqlalchemy import func, distinct, Column, String, UnicodeText
try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError


class Mesajlar(BASE):
    __tablename__ = "mesaj"
    emr = Column(UnicodeText, primary_key=True, nullable=False)
    mesaj = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, emr, mesaj):
        self.emr = emr
        self.mesaj = mesaj

    def __repr__(self):
        return "<Mesaj '%s' üçün %s>" % (self.emr, self.mesaj)

    def __eq__(self, other):
        return bool(isinstance(other, Mesajlar)
                    and self.emr == other.emr
                    and self.mesaj == other.mesaj)


Mesajlar.__table__.create(checkfirst=True)

EMR_INSERTION_LOCK = threading.RLock()

def elave_mesaj(emr, mesaj):
    with EMR_INSERTION_LOCK:
        try:
            SESSION.query(Mesajlar).filter(Mesajlar.emr == emr).delete()
        except:
            pass

        emr = Mesajlar(emr, mesaj)
        SESSION.merge(emr)
        SESSION.commit()


def getir_mesaj(em):
    try:
        MESAJ = SESSION.query(Mesajlar).filter(Mesajlar.emr == em).first()
        return MESAJ.mesaj
    except:
        return False
    

def sil_mesaj(em):
    try:
        SESSION.query(Mesajlar).filter(Mesajlar.emr == em).delete()
        SESSION.commit()
    except Exception as e:
        return e
    return True
