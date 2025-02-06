# A00826875_A5.2
Ejercicio de programación 2 y análisis estático

## compute_sales.py
Este script calcula el costo total de ventas a partir de un catálogo de precios y registros de ventas.
Toma dos archivos JSON como entrada:

- TC1-ProductList.json: Contiene los productos y sus respectivos precios.
- TC#-Sales.json: Contiene las ventas registradas con el nombre del producto y la cantidad vendida.

El programa muestra el total de ventas en la consola y guarda los resultados en un archivo de texto.

## Uso
Ejecuta el script desde la terminal con el siguiente comando:
python compute_sales.py TC1-ProductList.json TC1-Sales.json

## Funcionamiento del código
1. Carga los archivos JSON y convierte el catálogo de productos en un diccionario con los precios.
2. Recorre el registro de ventas, validando que el producto exista y que la cantidad sea válida.
3. Calcula el costo total de ventas sumando el precio de cada producto multiplicado por la cantidad vendida.
4. Muestra los resultados en consola e imprime cualquier advertencia si hay errores en los datos.
5. Guarda los resultados en un archivo SalesResults.txt con el costo total y detalles de ejecución.

## Requisitos
- Python 3.x
- Librerías estándar (json, sys, time)

