# BOT TELEGRAM

> Bot con comandos personalizados.  

**PD: Por el momento solo tiene dos comandos.**  

* **/help**  
&nbsp;&nbsp;&nbsp;&nbsp;*Muestra esta ayuda.*  

* **/searchbook [name-book] [cantidad]**  
&nbsp;&nbsp;&nbsp;&nbsp;*[name-book] inserta el nombre del libro,*  
&nbsp;&nbsp;&nbsp;&nbsp;*que deseas información.*  
&nbsp;&nbsp;&nbsp;&nbsp;*Tambien puedes pasarle una serie de palabras,*  
&nbsp;&nbsp;&nbsp;&nbsp;*te regresara las coincidencias de dichas*  
&nbsp;&nbsp;&nbsp;&nbsp;*palabras.*  
&nbsp;&nbsp;&nbsp;&nbsp;*[cantidad] es opcional, si no le pasa una cantidad*  
&nbsp;&nbsp;&nbsp;&nbsp;*te regresa 5 coincidencias, el máximo es de 10.*  

## Estructura del proyecto

.  
├── configs.py # Configuraciones globales y algunas urls  
├── docs       # Documentacion  
├── README.md  # Breve explicaion del proyecto  
├── run.py     # Ejecuta el bot  
├── src        # Contiene los modulos para el bot  
├── tests      # Pruebas unitarias  
└── venv       # Contiene el pipenfile y el requeriment  

---

./src  
├── api          # Contiene el script para la api de telegram.  
├── controllers  # Estos script controlan los scrapers y el bot.  
├── helpers      # Scripts auxiliares  
├── __init__.py  # modulos  
├── main.py      # Contiene la función run del para ejecutar el bot  
└── scrapers     # Scripts de los scrapers  

## Web Scraping

La informacion de los libros que proporciona lo recaba de [1lib](https://es.1lib.mx/)  


## Requerimientos  

* certifi==2022.6.15  
* charset-normalizer==2.1.0  
* idna==3.3  
* requests==2.28.1  
* urllib3==1.26.10  

> En la carpeta venv esta el `requirements.txt`  


## Instalacion

Instala los `requeriment` y ejecuta el `run.py`


---


Cualquier duda o sugerencia puedes contactarme en:
[facebook](https://www.facebook.com/and0.0bna)
[instagram](https://www.instagram.com/and0.0bna/)




