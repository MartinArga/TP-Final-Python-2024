# TP-Final-Python-2024
Proyecto final del curso de Python del ITBA. Año 2024. [Consigna Trabajo práctico final](Consigna.md)
## Instalación del proyecto usando Conda

```
conda create -n tp-final-python
conda activate tp-final-python
conda install python==3.13.0
conda install jupyterlab==4.2.5
pip install -r requirements.txt

```
## Resumen
Se genera una aplicacion en código Python, que obtiene los datos financieros a través de una API de finanzas: "http://api.marketstack.com/v1/", los guarda en una base de datos SQLite junto con la correspondiente tabla y genera un gráfico a partir de los tickers almacenados.

La aplicacion se dividió en seis funciones para reducir el nümero total de líneas de código, haciendo que sea mas fácil de generar, entender y corregir