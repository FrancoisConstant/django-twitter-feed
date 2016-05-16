from django.db.transaction import set_autocommit, commit


def commit_manually(function):
    def _commit_manually(*args, **kwargs):
        set_autocommit(False)
        res = function(*args, **kwargs)
        commit()
        set_autocommit(True)
        return res
    return _commit_manually