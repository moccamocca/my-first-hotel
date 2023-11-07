from django.db.models.lookups import In as LookupIn
from django.db.models.fields import Field
from datetime import date
import uuid


# возварщает номер бронирвания в формате '20231027-c316a2c7'
def date_uuid():
    date_now = date.today()
    return str(date_now.year) + str(date_now.month) + str(date_now.day) + '-' + str(uuid.uuid4())[:8]


# ----------------------------
# пользовательский поиск тк в django not in не реализован (есть только not, а не входимость)
# https://stackoverflow.com/questions/60671987/django-orm-equivalent-of-sql-not-in-exclude-and-q-objects-do-not-work
class NotIn(LookupIn):
    lookup_name = "notin"

    def get_rhs_op(self, connection, rhs):
        return "NOT IN %s" % rhs


Field.register_lookup(NotIn)


# ----------------------------

def xstr(s):
    if s is None:
        return ''
    return str(s)
