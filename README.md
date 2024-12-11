# TP-Final-Python-2024
Proyecto final del curso de Python del ITBA. Año 2024.
## Instalación del proyecto usando Conda

```
conda create -n <env>
conda activate <env>
conda install python==3.13.0
conda install jupyterlab==4.2.5
pip install -r requirements.txt

```
## Resumen
Se genera un una aplicacion en código Python, que obtiene los datos a través de una API de finanzafis: "http://api.marketstack.com/v1/", los guarda en una base de datos SQLite junto con la correspondiente tabla y genera un grá
fico a partir de los ticker almacenados