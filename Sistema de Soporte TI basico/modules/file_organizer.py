"""
Módulo de Organización de Archivos
Permite organizar archivos por tipo, fecha y tamaño
"""

import os
import shutil
import datetime
from pathlib import Path

class FileOrganizer:
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.files_dir = self.data_dir / "files"
        self.organized_dir = self.data_dir / "organized"
    
    def menu(self):
        """Menú de organización de archivos"""
        while True:
            print("\n" + "-"*40)
            print("ORGANIZACIÓN DE ARCHIVOS")
            print("-"*40)
            print("1. Listar archivos disponibles")
            print("2. Organizar por tipo")
            print("3. Organizar por fecha")
            print("4. Organizar por tamaño")
            print("5. Mover archivo manualmente")
            print("6. Devolver archivos a carpeta principal")
            print("7. Volver al menú principal")
            print("-"*40)
            
            try:
                option = input("Seleccione una opción (1-7): ").strip()
                
                if option == "1":
                    self.list_files()
                elif option == "2":
                    self.organize_by_type()
                elif option == "3":
                    self.organize_by_date()
                elif option == "4":
                    self.organize_by_size()
                elif option == "5":
                    self.move_file_manual()
                elif option == "6":
                    self.return_files_to_main()
                elif option == "7":
                    break
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"Error: {e}")
    
    def list_files(self):
        """Listar archivos en el directorio de archivos"""
        print("\nArchivos disponibles:")
        print("-"*30)
        
        if not self.files_dir.exists():
            print("No hay directorio de archivos.")
            return
        
        files = list(self.files_dir.glob("*"))
        if not files:
            print("No hay archivos en el directorio.")
            return
        
        for i, file in enumerate(files, 1):
            if file.is_file():
                size = file.stat().st_size
                size_str = self.format_size(size)
                modified = datetime.datetime.fromtimestamp(file.stat().st_mtime)
                print(f"{i:2d}. {file.name} ({size_str}) - {modified.strftime('%Y-%m-%d %H:%M')}")
    
    def organize_by_type(self):
        """Organizar archivos por extensión/tipo"""
        print("\nOrganizando archivos por tipo...")
        
        if not self.files_dir.exists():
            print("No hay directorio de archivos.")
            return
        
        type_mapping = {
            '.txt': 'documentos',
            '.pdf': 'documentos',
            '.doc': 'documentos',
            '.docx': 'documentos',
            '.jpg': 'imagenes',
            '.jpeg': 'imagenes',
            '.png': 'imagenes',
            '.gif': 'imagenes',
            '.mp4': 'videos',
            '.avi': 'videos',
            '.mkv': 'videos',
            '.mp3': 'audio',
            '.wav': 'audio',
            '.flac': 'audio',
            '.zip': 'comprimidos',
            '.rar': 'comprimidos',
            '.7z': 'comprimidos',
            '.exe': 'programas',
            '.msi': 'programas'
        }
        
        organized_count = 0
        
        for file_path in self.files_dir.glob("*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                folder_name = type_mapping.get(ext, 'otros')
                
                target_dir = self.organized_dir / folder_name
                target_dir.mkdir(exist_ok=True)
                
                target_path = target_dir / file_path.name
                
                # Evitar sobrescribir archivos
                counter = 1
                while target_path.exists():
                    stem = file_path.stem
                    target_path = target_dir / f"{stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                shutil.move(str(file_path), str(target_path))
                organized_count += 1
                print(f"Movido: {file_path.name} -> {folder_name}/")
        
        print(f"\nSe organizaron {organized_count} archivos.")
    
    def organize_by_date(self):
        """Organizar archivos por fecha de modificación"""
        print("\nOrganizando archivos por fecha...")
        
        if not self.files_dir.exists():
            print("No hay directorio de archivos.")
            return
        
        organized_count = 0
        
        for file_path in self.files_dir.glob("*"):
            if file_path.is_file():
                mod_time = datetime.datetime.fromtimestamp(file_path.stat().st_mtime)
                folder_name = mod_time.strftime("%Y-%m")
                
                target_dir = self.organized_dir / folder_name
                target_dir.mkdir(exist_ok=True)
                
                target_path = target_dir / file_path.name
                
                # Evitar sobrescribir archivos
                counter = 1
                while target_path.exists():
                    stem = file_path.stem
                    target_path = target_dir / f"{stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                shutil.move(str(file_path), str(target_path))
                organized_count += 1
                print(f"Movido: {file_path.name} -> {folder_name}/")
        
        print(f"\nSe organizaron {organized_count} archivos.")
    
    def organize_by_size(self):
        """Organizar archivos por tamaño"""
        print("\nOrganizando archivos por tamaño...")
        
        if not self.files_dir.exists():
            print("No hay directorio de archivos.")
            return
        
        organized_count = 0
        
        for file_path in self.files_dir.glob("*"):
            if file_path.is_file():
                size = file_path.stat().st_size
                
                if size < 1024 * 1024:  # < 1MB
                    folder_name = "pequenos"
                elif size < 1024 * 1024 * 10:  # < 10MB
                    folder_name = "medianos"
                else:  # >= 10MB
                    folder_name = "grandes"
                
                target_dir = self.organized_dir / folder_name
                target_dir.mkdir(exist_ok=True)
                
                target_path = target_dir / file_path.name
                
                # Evitar sobrescribir archivos
                counter = 1
                while target_path.exists():
                    stem = file_path.stem
                    target_path = target_dir / f"{stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                shutil.move(str(file_path), str(target_path))
                organized_count += 1
                print(f"Movido: {file_path.name} -> {folder_name}/")
        
        print(f"\nSe organizaron {organized_count} archivos.")
    
    def move_file_manual(self):
        """Mover un archivo manualmente a una carpeta específica"""
        self.list_files()
        
        if not self.files_dir.exists():
            return
        
        try:
            file_num = int(input("\nNúmero del archivo a mover: ")) - 1
            files = list(self.files_dir.glob("*"))
            
            if file_num < 0 or file_num >= len(files):
                print("Número de archivo no válido.")
                return
            
            file_path = files[file_num]
            if not file_path.is_file():
                print("El elemento seleccionado no es un archivo.")
                return
            
            folder_name = input("Nombre de la carpeta destino: ").strip()
            if not folder_name:
                print("Debe especificar un nombre de carpeta.")
                return
            
            target_dir = self.organized_dir / folder_name
            target_dir.mkdir(exist_ok=True)
            
            target_path = target_dir / file_path.name
            
            # Evitar sobrescribir archivos
            counter = 1
            while target_path.exists():
                stem = file_path.stem
                target_path = target_dir / f"{stem}_{counter}{file_path.suffix}"
                counter += 1
            
            shutil.move(str(file_path), str(target_path))
            print(f"Archivo movido: {file_path.name} -> {folder_name}/")
            
        except ValueError:
            print("Número de archivo no válido.")
        except Exception as e:
            print(f"Error al mover archivo: {e}")
    
    def return_files_to_main(self):
        """Devolver archivos de la carpeta organized a la carpeta principal"""
        print("\nDevolver archivos a carpeta principal...")
        
        if not self.organized_dir.exists():
            print("No hay directorio de archivos organizados.")
            return
        
        # Listar todos los archivos en organized y subcarpetas
        all_files = []
        for folder in self.organized_dir.iterdir():
            if folder.is_dir():
                for file_path in folder.glob("*"):
                    if file_path.is_file():
                        all_files.append(file_path)
        
        if not all_files:
            print("No hay archivos organizados para devolver.")
            return
        
        print(f"\nArchivos organizados encontrados: {len(all_files)}")
        print("-"*50)
        
        for i, file_path in enumerate(all_files, 1):
            size = file_path.stat().st_size
            size_str = self.format_size(size)
            folder_name = file_path.parent.name
            print(f"{i:2d}. {file_path.name} ({size_str}) - Carpeta: {folder_name}")
        
        try:
            choice = input("\n¿Devolver todos los archivos a la carpeta principal? (s/n): ").strip().lower()
            
            if choice == 's':
                returned_count = 0
                
                for file_path in all_files:
                    target_path = self.files_dir / file_path.name
                    
                    # Evitar sobrescribir archivos
                    counter = 1
                    while target_path.exists():
                        stem = file_path.stem
                        target_path = self.files_dir / f"{stem}_{counter}{file_path.suffix}"
                        counter += 1
                    
                    shutil.move(str(file_path), str(target_path))
                    returned_count += 1
                    print(f"Devuelto: {file_path.name} <- {file_path.parent.name}/")
                
                print(f"\n✓ Se devolvieron {returned_count} archivos a la carpeta principal.")
                
                # Eliminar carpetas vacías
                for folder in self.organized_dir.iterdir():
                    if folder.is_dir() and not any(folder.iterdir()):
                        folder.rmdir()
                        print(f"Carpeta vacía eliminada: {folder.name}")
            
            else:
                # Devolver archivos individuales
                while True:
                    try:
                        file_num = input("\nNúmero de archivo a devolver (o 'fin' para terminar): ").strip()
                        
                        if file_num.lower() == 'fin':
                            break
                        
                        file_num = int(file_num) - 1
                        
                        if file_num < 0 or file_num >= len(all_files):
                            print("Número de archivo no válido.")
                            continue
                        
                        file_path = all_files[file_num]
                        target_path = self.files_dir / file_path.name
                        
                        # Evitar sobrescribir archivos
                        counter = 1
                        while target_path.exists():
                            stem = file_path.stem
                            target_path = self.files_dir / f"{stem}_{counter}{file_path.suffix}"
                            counter += 1
                        
                        shutil.move(str(file_path), str(target_path))
                        print(f"Devuelto: {file_path.name} <- {file_path.parent.name}/")
                        
                        # Actualizar lista de archivos
                        all_files.pop(file_num)
                        
                    except ValueError:
                        print("Entrada no válida. Use un número o 'fin'.")
                    except Exception as e:
                        print(f"Error al devolver archivo: {e}")
        
        except Exception as e:
            print(f"Error en la operación: {e}")
    
    def format_size(self, size_bytes):
        """Formatear tamaño en bytes a formato legible"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes/1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes/(1024*1024):.1f} MB"
        else:
            return f"{size_bytes/(1024*1024*1024):.1f} GB"
