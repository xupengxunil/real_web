from saltui import db

class Minion(db.Model):
    __tablename__ = 'minions'
    def __init__(self, id, name, ip):
        self.id = str(id)
        self.name = name
        self.ip = ip

    def __repr__(self):
        return "<Minion %s>" %(self.name)
    __str__ = __repr__

    @classmethod
    def search_by_id(cls, ids, deadline=0):
        if not ids:
            return []

        holders = ["%s" for x in ids]
        placeholder = ",".join(holders)
        args = ids + [deadline, ]

        cursor = db_conn.execute('''select id, endpoint, ts from endpoint where id in (''' + placeholder + ''') and ts > %s''', args)
        rows = cursor.fetchall()
        cursor and cursor.close()

        return [cls(*row) for row in rows]