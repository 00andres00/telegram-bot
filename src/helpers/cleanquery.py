def cleanQuery(q):
    n_Word = len(q.split())
    if n_Word != 1:
        q = q.replace(' ', '%20')
    else:
        q = q+'?'

    return q
