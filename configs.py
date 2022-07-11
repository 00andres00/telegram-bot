### ### ### CONFIG BOT ### ### ###

### ### ### URLS ### ### ###
URLS = {
            ### BOT ###
        'bot_url': 'https://api.telegram.org/bot'+TOKEN,
            ### SCRAPING BOOKS ###
        'init': 'https://es.1lib.mx/',
        'Search': 'https://es.1lib.mx/s/'
        }

### ### ### DATAS ### ### ###
data = {
        'message':{
            'chat_id': CHAT_ID,
            'parse_mode': 'HTML',
            }
        }

### ### ### DIR LAST UPDATE FILE ### ### ###
fileLastUpdate = 'src/controllers/lastUpdate.py'
### ### ### ### ### ###

