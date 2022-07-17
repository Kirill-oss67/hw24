from flask_restx import abort
from typing import Iterator, List, Any


def make_query(cnd: str, val: str, file_list: Iterator) ->List[Any]:
    try:
        if cnd == "filter":
            res = list(filter(lambda x: val in x, file_list))
            return res
    except:
        return abort(400)
    if cnd == "map":
        try:
            res = list([x.split()[int(val)] for x in file_list])
            return res
        except:
            return abort(400)
    if cnd == "unique":
        res = list(set(file_list))
        return res
    if cnd == 'sort':
        reverse = val == 'desc'
        res = list(sorted(file_list, reverse=reverse))
        return res
    if cnd == "limit":
        try:
            res = list(file_list)[:int(val)]
            return res
        except:
            return abort(400)
    return []