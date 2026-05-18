# ============================================================
#  PRÁCTICA CON AUTO-VERIFICACIÓN
#  Escribe tu solución donde dice ... y ejecuta el archivo.
#  Los asserts te dirán si acertaste o no.
# ============================================================

passed = 0
total = 10


def ejercicio(num, descripcion, solucion, esperado):
    """Evalúa un ejercicio individual sin detener el resto."""
    global passed
    try:
        resultado = solucion()
        if resultado is ...:
            print(f"- Ejercicio {num}: {descripcion} — pendiente")
            return
        assert resultado == esperado, f"{resultado}"
        passed += 1
        print(f"✓ Ejercicio {num}: {descripcion} — OK")
    except AssertionError as e:
        print(f"✗ Ejercicio {num}: {descripcion} — FALLÓ: {e}")
    except Exception:
        print(f"- Ejercicio {num}: {descripcion} — pendiente")


# Ejercicio 1: enumerate
# Listar los archivos de un directorio numerados.
# Genera: [" 1: readme.md", " 2: script.py", ...]

files_1 = ["readme.md", "script.py", "foto.png", "datos.csv", "config.json"]

ejercicio(1, "enumerate",
    lambda: ...,  # tu solución aquí
    [" 1: readme.md", " 2: script.py", " 3: foto.png", " 4: datos.csv", " 5: config.json"],
)


# Ejercicio 2: extensiones únicas
# Extrae todas las extensiones (sin duplicados) y ordénalas.

files_2 = ["notas.txt", "foto.png", "script.py", "readme.md", "app.py", "data.csv", "banner.png"]

ejercicio(2, "extensiones únicas",
    lambda: ...,  # tu solución aquí
    [".csv", ".md", ".png", ".py", ".txt"],
)


# Ejercicio 3: extraer nombres de rutas
# Extrae el nombre del archivo de cada ruta.

routes_3 = [
    "/home/user/docs/notas.txt",
    "/home/user/imgs/foto.png",
    "/home/user/code/script.py",
]

ejercicio(3, "extraer nombres",
    lambda: ...,  # tu solución aquí
    ["notas.txt", "foto.png", "script.py"],
)


# Ejercicio 4: filtrar .py
# Extrae solo los archivos .py

files_4 = ["notas.txt", "foto.png", "script.py", "readme.md", "app.py", "data.csv"]

ejercicio(4, "filtrar .py",
    lambda: ...,  # tu solución aquí
    ["script.py", "app.py"],
)


# Ejercicio 5: etiquetar archivos
# Si termina en .py -> "código", si no -> "dato"

files_5 = ["script.py", "datos.csv", "app.py", "reporte.csv", "utils.py"]

ejercicio(5, "etiquetar archivos",
    lambda: ...,  # tu solución aquí
    [("script.py", "código"), ("datos.csv", "dato"), ("app.py", "código"), ("reporte.csv", "dato"), ("utils.py", "código")],
)


# Ejercicio 6: filtrar imágenes + mayúsculas
# Filtrar archivos .png o .jpg y transformar a mayúsculas.

files_6 = ["notas.txt", "foto.png", "script.py", "banner.jpg", "app.py", "icono.png"]

ejercicio(6, "imágenes en mayúsculas",
    lambda: ...,  # tu solución aquí
    ["FOTO.PNG", "BANNER.JPG", "ICONO.PNG"],
)


# Ejercicio 7: reporte desde diccionario
# Genera líneas tipo: "script.py       -> 2.1 KB"

metadata_7 = {
    "script.py": "2.1 KB",
    "foto.png": "840 KB",
    "notas.txt": "12 KB",
    "readme.md": "4.3 KB",
}

ejercicio(7, "reporte desde dict",
    lambda: ...,  # tu solución aquí
    ["script.py       -> 2.1 KB", "foto.png        -> 840 KB", "notas.txt       -> 12 KB", "readme.md       -> 4.3 KB"],
)


# Ejercicio 8: dict comp — archivo -> extensión
# Crea un diccionario que mapee cada archivo a su extensión.

files_8 = ["script.py", "foto.png", "datos.csv", "readme.md", "app.py"]

ejercicio(8, "dict archivo->extensión",
    lambda: ...,  # tu solución aquí
    {"script.py": ".py", "foto.png": ".png", "datos.csv": ".csv", "readme.md": ".md", "app.py": ".py"},
)


# Ejercicio 9: aplanar directorios
# Todos los archivos en una sola lista.

directories_9 = {
    "docs": ["notas.txt", "readme.md", "informe.pdf"],
    "imgs": ["foto.png", "banner.jpg"],
    "code": ["script.py", "app.py", "utils.py"],
}

ejercicio(9, "aplanar directorios",
    lambda: ...,  # tu solución aquí
    ["notas.txt", "readme.md", "informe.pdf", "foto.png", "banner.jpg", "script.py", "app.py", "utils.py"],
)


# Ejercicio 10: zip — combinar nombre y tamaño
# Combinar nombres con tamaños convertidos a KB (división entera // 1000).

names_10 = ["script.py", "foto.png", "datos.csv", "readme.md"]
sizes_10 = [12_400, 840_000, 4_200, 3_100]

ejercicio(10, "zip nombres+tamaños",
    lambda: ...,  # tu solución aquí
    [("script.py", 12), ("foto.png", 840), ("datos.csv", 4), ("readme.md", 3)],
)


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
