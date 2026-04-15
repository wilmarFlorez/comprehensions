# Todos los archivos en una sola lista
# ejemplo ['notas.txt', 'readme.md', 'informe.pdf', 'foto.png', 'banner.jpg'...]

directories = {
    "docs": ["notas.txt", "readme.md", "informe.pdf"],
    "imgs": ["foto.png", "banner.jpg"],
    "code": ["script.py", "app.py", "utils.py"],
}

all_files = [file for files in directories.values() for file in files]

print(all_files)
print(f"Total : {len(all_files)} files")
