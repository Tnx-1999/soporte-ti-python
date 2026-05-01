"""
Módulo de Lectura de Logs
Permite leer, filtrar y analizar archivos de log
"""

import os
import re
import datetime
from pathlib import Path

class LogReader:
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.logs_dir = self.data_dir / "logs"
        self.ensure_logs_dir()
    
    def ensure_logs_dir(self):
        """Crear directorio de logs si no existe"""
        self.logs_dir.mkdir(exist_ok=True)
    
    def menu(self):
        """Menú del lector de logs"""
        while True:
            print("\n" + "-"*40)
            print("LECTOR DE LOGS")
            print("-"*40)
            print("1. Listar archivos de log")
            print("2. Ver contenido de log")
            print("3. Buscar en logs")
            print("4. Filtrar por nivel de error")
            print("5. Ver últimas líneas")
            print("6. Analizar patrones")
            print("7. Crear log de ejemplo")
            print("8. Volver al menú principal")
            print("-"*40)
            
            try:
                option = input("Seleccione una opción (1-8): ").strip()
                
                if option == "1":
                    self.list_log_files()
                elif option == "2":
                    self.view_log_content()
                elif option == "3":
                    self.search_logs()
                elif option == "4":
                    self.filter_by_level()
                elif option == "5":
                    self.view_tail()
                elif option == "6":
                    self.analyze_patterns()
                elif option == "7":
                    self.create_sample_log()
                elif option == "8":
                    break
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"Error: {e}")
    
    def list_log_files(self):
        """Listar archivos de log disponibles"""
        print("\nArchivos de log disponibles:")
        print("-"*40)
        
        log_files = list(self.logs_dir.glob("*.log")) + list(self.logs_dir.glob("*.txt"))
        
        if not log_files:
            print("No hay archivos de log en el directorio.")
            print(f"Directorio: {self.logs_dir}")
            return
        
        for i, log_file in enumerate(log_files, 1):
            size = log_file.stat().st_size
            size_str = self.format_size(size)
            modified = datetime.datetime.fromtimestamp(log_file.stat().st_mtime)
            print(f"{i:2d}. {log_file.name} ({size_str}) - {modified.strftime('%Y-%m-%d %H:%M')}")
    
    def view_log_content(self):
        """Ver contenido de un archivo de log"""
        self.list_log_files()
        
        log_files = list(self.logs_dir.glob("*.log")) + list(self.logs_dir.glob("*.txt"))
        
        if not log_files:
            return
        
        try:
            file_num = int(input("\nNúmero del archivo a ver: ")) - 1
            
            if file_num < 0 or file_num >= len(log_files):
                print("Número de archivo no válido.")
                return
            
            log_file = log_files[file_num]
            
            print(f"\nMostrando contenido de: {log_file.name}")
            print("="*60)
            
            lines_limit = input("Líneas a mostrar (Enter para todas): ").strip()
            
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                if lines_limit:
                    try:
                        limit = int(lines_limit)
                        lines = []
                        for i, line in enumerate(f):
                            if i >= limit:
                                break
                            lines.append(line.rstrip())
                        content = '\n'.join(lines)
                    except ValueError:
                        content = f.read()
                else:
                    content = f.read()
                
                if content:
                    print(content)
                else:
                    print("El archivo está vacío.")
                
                if len(content) > 2000:
                    print("\n... (contenido truncado para mejor visualización)")
        
        except ValueError:
            print("Número de archivo no válido.")
        except Exception as e:
            print(f"Error al leer archivo: {e}")
    
    def search_logs(self):
        """Buscar texto en todos los logs"""
        search_term = input("Ingrese término a buscar: ").strip()
        
        if not search_term:
            print("Debe ingresar un término de búsqueda.")
            return
        
        print(f"\nBuscando '{search_term}' en todos los logs...")
        print("-"*60)
        
        log_files = list(self.logs_dir.glob("*.log")) + list(self.logs_dir.glob("*.txt"))
        total_matches = 0
        
        for log_file in log_files:
            matches = 0
            try:
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        if search_term.lower() in line.lower():
                            if matches == 0:
                                print(f"\n📁 {log_file.name}:")
                            
                            print(f"  Línea {line_num}: {line.strip()}")
                            matches += 1
                            total_matches += 1
                            
                            # Limitar resultados por archivo
                            if matches >= 10:
                                print(f"  ... (más de 10 coincidencias en {log_file.name})")
                                break
            except Exception as e:
                print(f"Error al leer {log_file.name}: {e}")
        
        if total_matches == 0:
            print("No se encontraron coincidencias.")
        else:
            print(f"\nTotal de coincidencias: {total_matches}")
    
    def filter_by_level(self):
        """Filtrar logs por nivel de error"""
        print("\nNiveles de log comunes:")
        print("1. ERROR")
        print("2. WARNING")
        print("3. INFO")
        print("4. DEBUG")
        print("5. CRITICAL")
        
        level_map = {
            '1': 'ERROR',
            '2': 'WARNING',
            '3': 'INFO',
            '4': 'DEBUG',
            '5': 'CRITICAL'
        }
        
        choice = input("Seleccione nivel (1-5): ").strip()
        
        if choice not in level_map:
            print("Opción no válida.")
            return
        
        level = level_map[choice]
        print(f"\nFiltrando logs con nivel: {level}")
        print("-"*60)
        
        log_files = list(self.logs_dir.glob("*.log")) + list(self.logs_dir.glob("*.txt"))
        total_matches = 0
        
        # Patrones regex para diferentes formatos de log
        patterns = [
            rf'\[{level}\]',
            rf'{level}',
            rf'\b{level}\b',
            rf'<{level}>',
            rf'\[{level}\]\s*\d{{4}}-\d{{2}}-\d{{2}}',
        ]
        
        for log_file in log_files:
            matches = 0
            try:
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        for pattern in patterns:
                            if re.search(pattern, line, re.IGNORECASE):
                                if matches == 0:
                                    print(f"\n📁 {log_file.name}:")
                                
                                print(f"  Línea {line_num}: {line.strip()}")
                                matches += 1
                                total_matches += 1
                                break
                        
                        # Limitar resultados por archivo
                        if matches >= 20:
                            print(f"  ... (más de 20 coincidencias en {log_file.name})")
                            break
            except Exception as e:
                print(f"Error al leer {log_file.name}: {e}")
        
        if total_matches == 0:
            print(f"No se encontraron logs con nivel {level}.")
        else:
            print(f"\nTotal de entradas {level}: {total_matches}")
    
    def view_tail(self):
        """Ver últimas líneas de un log"""
        self.list_log_files()
        
        log_files = list(self.logs_dir.glob("*.log")) + list(self.logs_dir.glob("*.txt"))
        
        if not log_files:
            return
        
        try:
            file_num = int(input("\nNúmero del archivo: ")) - 1
            
            if file_num < 0 or file_num >= len(log_files):
                print("Número de archivo no válido.")
                return
            
            log_file = log_files[file_num]
            lines_count = input("Número de líneas a mostrar (default 10): ").strip()
            
            try:
                lines_count = int(lines_count) if lines_count else 10
            except ValueError:
                lines_count = 10
            
            print(f"\nÚltimas {lines_count} líneas de {log_file.name}:")
            print("="*60)
            
            try:
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    all_lines = f.readlines()
                    tail_lines = all_lines[-lines_count:] if len(all_lines) > lines_count else all_lines
                    
                    for i, line in enumerate(tail_lines, 1):
                        print(f"{i:3d}: {line.rstrip()}")
                        
            except Exception as e:
                print(f"Error al leer archivo: {e}")
        
        except ValueError:
            print("Número de archivo no válido.")
    
    def analyze_patterns(self):
        """Analizar patrones comunes en logs"""
        print("\nAnálisis de patrones en logs...")
        print("-"*60)
        
        log_files = list(self.logs_dir.glob("*.log")) + list(self.logs_dir.glob("*.txt"))
        
        if not log_files:
            print("No hay archivos de log para analizar.")
            return
        
        # Patrones comunes a buscar
        patterns = {
            'Direcciones IP': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
            'Fechas': r'\d{4}-\d{2}-\d{2}',
            'Horas': r'\d{2}:\d{2}:\d{2}',
            'Códigos de error': r'\b[0-9]{3,5}\b',
            'URLs': r'https?://[^\s]+',
            'Emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        }
        
        for log_file in log_files:
            print(f"\n📁 Analizando: {log_file.name}")
            print("-"*40)
            
            try:
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                    for pattern_name, pattern in patterns.items():
                        matches = re.findall(pattern, content)
                        if matches:
                            unique_matches = list(set(matches))
                            print(f"  {pattern_name}: {len(unique_matches)} únicos")
                            if len(unique_matches) <= 5:
                                for match in unique_matches[:5]:
                                    print(f"    - {match}")
                            else:
                                for match in unique_matches[:3]:
                                    print(f"    - {match}")
                                print(f"    ... y {len(unique_matches)-3} más")
                        
            except Exception as e:
                print(f"Error al analizar {log_file.name}: {e}")
    
    def create_sample_log(self):
        """Crear un archivo de log de ejemplo"""
        sample_content = """2024-01-15 08:30:15 [INFO] Sistema iniciado correctamente
2024-01-15 08:31:22 [INFO] Usuario admin@empresa.com ha iniciado sesión
2024-01-15 08:32:45 [WARNING] Intento de acceso fallido desde IP 192.168.1.105
2024-01-15 08:33:10 [INFO] Proceso de backup iniciado
2024-01-15 08:35:33 [ERROR] No se puede conectar a la base de datos: Connection timeout
2024-01-15 08:36:15 [INFO] Reconexión a base de datos exitosa
2024-01-15 08:40:22 [INFO] Backup completado exitosamente
2024-01-15 09:15:33 [WARNING] Uso de CPU elevado: 85%
2024-01-15 09:16:45 [ERROR] Error en módulo de pagos: Código 502
2024-01-15 09:17:10 [CRITICAL] Sistema de pagos caído - intervención manual requerida
2024-01-15 09:20:15 [INFO] Sistema de pagos reiniciado
2024-01-15 09:21:30 [INFO] Usuario soporte@empresa.com ha iniciado sesión
2024-01-15 09:25:44 [DEBUG] Verificación de integridad de datos completada
2024-01-15 09:30:15 [INFO] Tarea programada ejecutada: Limpieza de caché
2024-01-15 09:45:22 [WARNING] Espacio en disco bajo: 15% disponible
2024-01-15 10:00:00 [INFO] Reporte diario generado exitosamente
2024-01-15 10:15:33 [ERROR] Fallo al enviar email a cliente@ejemplo.com
2024-01-15 10:16:45 [INFO] Reintentando envío de email...
2024-01-15 10:17:22 [INFO] Email enviado exitosamente
2024-01-15 10:30:15 [WARNING] Actualización de sistema disponible
2024-01-15 10:45:33 [INFO] Usuario cliente_final@gmail.com ha iniciado sesión
"""
        
        filename = f"sample_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        filepath = self.logs_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(sample_content)
        
        print(f"\n✓ Log de ejemplo creado: {filename}")
        print(f"Ubicación: {filepath}")
        print("Este log contiene ejemplos de diferentes niveles y patrones para pruebas.")
    
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
