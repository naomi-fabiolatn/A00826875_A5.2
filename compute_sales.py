"""
compute_sales.py

Este script calcula el costo total de ventas a partir de un catálogo de
precios y registros de ventas.
Toma dos archivos JSON como entrada:
un catálogo de precios de productos (priceCatalogue.json) y
un registro de ventas (salesRecord.json).
El programa muestra el costo total de ventas en la consola y lo guarda
en un archivo de resultados.

Uso:
    python compute_sales.py TC1-ProductList.json TC1-Sales.json

Autor: Naomi Tokunaga
Fecha: 9 de febrero de 2025
"""

import json
import sys
import time


def load_json_file(filename, is_catalogue=False):
    """
    Cargar datos JSON desde un archivo.
    Si es un catálogo de productos, convertirlo en un diccionario de precios.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Convert product catalog list to a dictionary
            if is_catalogue:
                return {item["title"]: item["price"] for item in data}

            return data
    except FileNotFoundError:
        print(f"Error: Archivo {filename} no encontrado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Archivo {filename} no es un JSON válido.")
        sys.exit(1)


def compute_total_sales(price_catalogue, sales_record):
    """
    Calcular el costo total de todas las ventas.
    """
    total_cost = 0.0
    errors = []

    for sale in sales_record:
        product = sale.get("Product")
        quantity = sale.get("Quantity")

        if product not in price_catalogue:
            errors.append(
                f"Advertencia: Producto '{product}' no encontrado en el "
                f"catálogo."
            )
            continue

        if not isinstance(quantity, (int, float)) or quantity < 0:
            errors.append(
                f"Advertencia: Cantidad inválida '{quantity}' para el "
                f"producto '{product}'."
            )
            continue

        total_cost += price_catalogue[product] * quantity

    return total_cost, errors


def main():
    """
    Función principal para ejecutar el programa.
    """
    if len(sys.argv) != 3:
        print(
            "Uso: python compute_sales.py TC1-ProductList.json "
            "TC1-Sales.json"
        )
        sys.exit(1)

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    start_time = time.time()

    price_catalogue = load_json_file(price_catalogue_file, is_catalogue=True)
    sales_record = load_json_file(sales_record_file)
    total_cost, errors = compute_total_sales(price_catalogue, sales_record)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total de ventas: {total_cost:.2f}")
    print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

    if errors:
        print("\nErrores:")
        for error in errors:
            print(error)

    with open("SalesResults.txt", "w", encoding='utf-8') as result_file:
        result_file.write(f"Total de ventas: {total_cost:.2f}\n")
        result_file.write(
            f"Tiempo de ejecución: {execution_time:.4f} segundos\n"
        )

        if errors:
            result_file.write("\nErrores:\n")
            for error in errors:
                result_file.write(f"{error}\n")


if __name__ == "__main__":
    main()
