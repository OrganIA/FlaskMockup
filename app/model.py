from sqlalchemy import inspect

def dictify_rows(rows):
    return [
        {c: getattr(row, c) for c in row.__dict__ if c[0] != '_'}
        for row in rows
    ]

def table_rows(rows, order=None, excludes=[]):
    if len(rows) == 0:
        return {}
    table = rows[0].__table__
    keys = order or [str(x)[len(str(table)) + 1:] for x in table.columns]
    return [
        {
            getattr(table.columns, key).info.get('label', key):
            getattr(row, key)
            for key in keys if key not in excludes
        } for row in rows
    ]
