
def Help():
    msm = '<b><i>|--- HELP ---|</i></b>\n\n\n<b>PD: Por el momento solo tiene dos comandos:</b>\n\n* <b>/help </b>\n            Muestra esta ayuda.\n\n* <b>/searchbook [name-book] [cantidad] </b>\n            <i>[name-book] inserta el nombre del libro,\n            que deseas información.\n            Tambien puedes pasarle una serie de palabras,\n            te regresará las coincidencias de dichas\n            palabras.\n            [cantidad] es opcional, si no le pasa una cantidad\n            te regresa 5 coincidencias, el máximo es de 10.</i>\n'

    #'<b>Help</b>\n\n<i>Comando: </i>/help\n<i>Descripción: </i>Muesta la esta ayuda\n\n<i>Comando: </i>/searchbook [query]\n<i>Descripción: </i>Devuelve informacion del libro que solicites.'
    return msm

def Searchbooks(query):
    from .getbooks import Get_Books
    from ..helpers import parseBooks

    if query:
        gb = Get_Books()
        gb.searchBook(query)
        msm = parseBooks(gb.Books)
        return msm
    return '<b>|--- /searchbook requiere [name-book] ---|</b>\n\n<i>Si no conoces el nombre del libro intenta\n insertar algunas palabras aleatorias\n\nPor ejemplo: lobo rojo</i>'

def Invalidcmd():
    msm =  '<b>|--- COMANDO INVALIDO ---|</b>\n\n<i>Intenta con:</i>\n* <b>/help</b>'
    return msm

