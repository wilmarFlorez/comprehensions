# filtrar archivos con extensión png o jpg y tranformar a mayusculas

files = ["notas.txt", "foto.png", "script.py", "banner.jpg", "app.py", "icono.png"]

# image files (.png, .jpg) to uppercase
images = [f.upper() for f in files if f.endswith((".png", ".jpg"))]

print(images)