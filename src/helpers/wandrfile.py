def read(fn):
    with open(fn, 'r') as f:
        return f.read()

def write(fn, c, m='w'):
    with open(fn, m) as f:
        f.write(c+' \n')
