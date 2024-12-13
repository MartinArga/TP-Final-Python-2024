# TP-Final-Python-2024
Proyecto final del curso de Python del ITBA. Año 2024. [Consigna Trabajo práctico final](Consigna.md)
## Instalación del proyecto usando Conda
Para descarga de conda se puede acceder al siguiente link :https://www.anaconda.com/products/distribution
```
conda create -n tp-final-python
conda activate tp-final-python
conda install python==3.10.13
conda install jupyterlab==4.2.5
pip install -r requirements.txt

```
## Resumen
Se genera una aplicacion en código Python, que obtiene los datos financieros a través de una API de finanzas: "http://api.marketstack.com/v1/", los guarda en una base de datos SQLite junto con la correspondiente tabla y genera un gráfico a partir de los tickers almacenados.

La aplicacion se dividió en seis funciones para reducir el número total de líneas de código, haciendo que sea mas fácil de generar, entender y corregir:

* **crear_base_de_datos()**
Crea la base de datos SQLite y una tabla llamada datos_mercado si no existen. Esta tabla almacenará los datos financieros obtenidos de la API, organizados por columnas: ticker, fecha, apertura, máximo, mínimo, cierre y volumen.

* **obtener_datos_de_api(ticker, fecha_inicio, fecha_fin)**
Consulta la API de MarketStack para obtener datos históricos de precios de acciones basados en el ticker, la fecha_inicio y la fecha_fin son proporcionados por el usuario. Devuelve los datos recibidos en formato JSON o un error si la consulta falla.

* **guardar_datos_en_base(ticker, datos)**
Guarda en la base de datos SQLite los datos obtenidos de la API. Cada entrada incluye información como el ticker, fechas, precios de apertura y cierre, máximos, mínimos y volumen de transacciones.

* **mostrar_resumen()**
Muestra un resumen de los datos almacenados en la base de datos. Lista los tickers disponibles junto con sus rangos de fechas mínimos y máximos. Sirve para identificar qué datos ya están guardados.

* **graficar_datos_ticker(ticker)**
Genera un gráfico de los precios de cierre para un ticker específico, utilizando los datos almacenados en la base de datos. Permite visualizar tendencias de precios de manera gráfica.

* **menu_principal()**
Controla la interacción principal con el usuario. Presenta opciones como actualización de datos desde la API, visualización de datos almacenados (resumen o gráfico), y la posibilidad de salir del programa. Actúa como el flujo principal del programa.