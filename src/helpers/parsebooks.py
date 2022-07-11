def parseBooks(books):
    Books = []
    for n in books.values():

        b = f'<i>Titulo: <b>{"".join(n[1])}</b></i>\n<i>Autor: <b>{"".join(n[2])}</b></i>\n<i>{"".join(n[3])}</i>\n<i>{"".join(n[4])}</i>\n<i>{"".join(n[5])}</i>\n'
        Books.append(b)
    return Books
