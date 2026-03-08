# Extrae el nombre del archivo

import os

routes = [
    "/home/user/docs/notas.txt",
    "/home/user/imgs/foto.png",
    "/home/user/code/script.py",
]

# os.path.basename() extrae el nombre del archivo
names = [os.path.basename(r) for r in routes ]

print(names)

