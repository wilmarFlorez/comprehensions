# ============================================================
#  PRÁCTICA CON AUTO-VERIFICACIÓN
#  Escribe tu solución donde dice "___" y ejecuta el archivo.
#  Los asserts te dirán si acertaste o no.
# ============================================================

passed = 0
total = 10

# Ejercicio 1: enumerate
# Listar los archivos de un directorio numerados.
# Genera: [" 1: readme.md", " 2: script.py", ...]

files = ["readme.md", "script.py", "foto.png", "datos.csv", "config.json"]

result_1 = ___  # tu solución aquí

assert result_1 == [
    " 1: readme.md",
    " 2: script.py",
    " 3: foto.png",
    " 4: datos.csv",
    " 5: config.json",
], f"Ejercicio 1 falló: {result_1}"
passed += 1
print("✓ Ejercicio 1: enumerate — OK")


# Ejercicio 2: extensiones únicas
# Extrae todas las extensiones (sin duplicados) y ordénalas.

files = [
    "notas.txt",
    "foto.png",
    "script.py",
    "readme.md",
    "app.py",
    "data.csv",
    "banner.png",
]

result_2 = ___  # tu solución aquí

assert result_2 == [".csv", ".md", ".png", ".py", ".txt"], (
    f"Ejercicio 2 falló: {result_2}"
)
passed += 1
print("✓ Ejercicio 2: extensiones únicas — OK")


# Ejercicio 3: extraer nombres de rutas
# Extrae el nombre del archivo de cada ruta.

routes = [
    "/home/user/docs/notas.txt",
    "/home/user/imgs/foto.png",
    "/home/user/code/script.py",
]

result_3 = ___  # tu solución aquí

assert result_3 == ["notas.txt", "foto.png", "script.py"], (
    f"Ejercicio 3 falló: {result_3}"
)
passed += 1
print("✓ Ejercicio 3: extraer nombres — OK")


# Ejercicio 4: filtrar .py
# Extrae solo los archivos .py

files = ["notas.txt", "foto.png", "script.py", "readme.md", "app.py", "data.csv"]

result_4 = ___  # tu solución aquí

assert result_4 == ["script.py", "app.py"], f"Ejercicio 4 falló: {result_4}"
passed += 1
print("✓ Ejercicio 4: filtrar .py — OK")


# Ejercicio 5: etiquetar archivos
# Si termina en .py -> "código", si no -> "dato"

files = ["script.py", "datos.csv", "app.py", "reporte.csv", "utils.py"]

result_5 = ___  # tu solución aquí

assert result_5 == [
    ("script.py", "código"),
    ("datos.csv", "dato"),
    ("app.py", "código"),
    ("reporte.csv", "dato"),
    ("utils.py", "código"),
], f"Ejercicio 5 falló: {result_5}"
passed += 1
print("✓ Ejercicio 5: etiquetar archivos — OK")


# Ejercicio 6: filtrar imágenes + mayúsculas
# Filtrar archivos .png o .jpg y transformar a mayúsculas.

files = ["notas.txt", "foto.png", "script.py", "banner.jpg", "app.py", "icono.png"]

result_6 = ___  # tu solución aquí

assert result_6 == ["FOTO.PNG", "BANNER.JPG", "ICONO.PNG"], (
    f"Ejercicio 6 falló: {result_6}"
)
passed += 1
print("✓ Ejercicio 6: imágenes en mayúsculas — OK")


# Ejercicio 7: reporte desde diccionario
# Genera líneas tipo: "script.py       -> 2.1 KB"

metadata = {
    "script.py": "2.1 KB",
    "foto.png": "840 KB",
    "notas.txt": "12 KB",
    "readme.md": "4.3 KB",
}

result_7 = ___  # tu solución aquí

assert result_7 == [
    "script.py       -> 2.1 KB",
    "foto.png        -> 840 KB",
    "notas.txt       -> 12 KB",
    "readme.md       -> 4.3 KB",
], f"Ejercicio 7 falló: {result_7}"
passed += 1
print("✓ Ejercicio 7: reporte desde dict — OK")


# Ejercicio 8: dict comp — archivo -> extensión
# Crea un diccionario que mapee cada archivo a su extensión.

files = ["script.py", "foto.png", "datos.csv", "readme.md", "app.py"]

result_8 = ___  # tu solución aquí

assert result_8 == {
    "script.py": ".py",
    "foto.png": ".png",
    "datos.csv": ".csv",
    "readme.md": ".md",
    "app.py": ".py",
}, f"Ejercicio 8 falló: {result_8}"
passed += 1
print("✓ Ejercicio 8: dict archivo->extensión — OK")


# Ejercicio 9: aplanar directorios
# Todos los archivos en una sola lista.

directories = {
    "docs": ["notas.txt", "readme.md", "informe.pdf"],
    "imgs": ["foto.png", "banner.jpg"],
    "code": ["script.py", "app.py", "utils.py"],
}

result_9 = ___  # tu solución aquí

assert result_9 == [
    "notas.txt",
    "readme.md",
    "informe.pdf",
    "foto.png",
    "banner.jpg",
    "script.py",
    "app.py",
    "utils.py",
], f"Ejercicio 9 falló: {result_9}"
passed += 1
print("✓ Ejercicio 9: aplanar directorios — OK")


# Ejercicio 10: zip — combinar nombre y tamaño
# Combinar nombres con tamaños convertidos a KB (división entera // 1000).

names = ["script.py", "foto.png", "datos.csv", "readme.md"]
sizes = [12_400, 840_000, 4_200, 3_100]

result_10 = ___  # tu solución aquí

assert result_10 == [
    ("script.py", 12),
    ("foto.png", 840),
    ("datos.csv", 4),
    ("readme.md", 3),
], f"Ejercicio 10 falló: {result_10}"
passed += 1
print("✓ Ejercicio 10: zip nombres+tamaños — OK")


# ============================================================
print(f"\n{'=' * 50}")
print(f"  RESULTADO: {passed}/{total} ejercicios correctos")
print(f"{'=' * 50}")
if passed == total:
    print("  ¡Perfecto! Todos los ejercicios completados.")
else:
    print(f"  Te faltan {total - passed} ejercicios. ¡Sigue intentando!")
