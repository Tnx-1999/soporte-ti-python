#!/usr/bin/env python3
"""
Script de prueba para el Sistema de Soporte TI
Verifica que todos los módulos se importen correctamente
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Probar que todos los módulos se importen correctamente"""
    print("🔍 Probando importación de módulos...")
    
    try:
        # Agregar el directorio actual al path
        current_dir = Path(__file__).parent
        sys.path.insert(0, str(current_dir))
        
        # Importar módulos
        from modules.file_organizer import FileOrganizer
        print("✅ FileOrganizer importado correctamente")
        
        from modules.ticket_system import TicketSystem
        print("✅ TicketSystem importado correctamente")
        
        from modules.log_reader import LogReader
        print("✅ LogReader importado correctamente")
        
        # Importar el sistema principal
        import main
        print("✅ Sistema principal importado correctamente")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_directories():
    """Probar creación de directorios"""
    print("\n📁 Probando creación de directorios...")
    
    try:
        current_dir = Path(__file__).parent
        data_dir = current_dir / "data"
        
        # Crear directorios de prueba
        directories = [
            data_dir,
            data_dir / "files",
            data_dir / "tickets",
            data_dir / "logs",
            data_dir / "organized"
        ]
        
        for directory in directories:
            directory.mkdir(exist_ok=True)
            if directory.exists():
                print(f"✅ Directorio creado/existe: {directory.name}")
            else:
                print(f"❌ No se pudo crear directorio: {directory}")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando directorios: {e}")
        return False

def test_ticket_system():
    """Probar funcionalidad básica del sistema de tickets"""
    print("\n🎫 Probando sistema de tickets...")
    
    try:
        current_dir = Path(__file__).parent
        data_dir = current_dir / "data"
        
        # Importar y crear instancia
        sys.path.insert(0, str(current_dir))
        from modules.ticket_system import TicketSystem
        
        ticket_system = TicketSystem(data_dir)
        print("✅ Sistema de tickets iniciado correctamente")
        
        # Probar generación de ID
        ticket_id = ticket_system.generate_ticket_id()
        print(f"✅ ID generado: {ticket_id}")
        
        # Probar carga de tickets
        tickets = ticket_system.load_tickets()
        print(f"✅ Tickets cargados: {len(tickets)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en sistema de tickets: {e}")
        return False

def test_file_organizer():
    """Probar funcionalidad básica del organizador de archivos"""
    print("\n📁 Probando organizador de archivos...")
    
    try:
        current_dir = Path(__file__).parent
        data_dir = current_dir / "data"
        
        # Importar y crear instancia
        sys.path.insert(0, str(current_dir))
        from modules.file_organizer import FileOrganizer
        
        organizer = FileOrganizer(data_dir)
        print("✅ Organizador de archivos iniciado correctamente")
        
        # Probar formateo de tamaño
        size_str = organizer.format_size(1024 * 1024)
        print(f"✅ Formateo de tamaño: {size_str}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en organizador de archivos: {e}")
        return False

def test_log_reader():
    """Probar funcionalidad básica del lector de logs"""
    print("\n📋 Probando lector de logs...")
    
    try:
        current_dir = Path(__file__).parent
        data_dir = current_dir / "data"
        
        # Importar y crear instancia
        sys.path.insert(0, str(current_dir))
        from modules.log_reader import LogReader
        
        log_reader = LogReader(data_dir)
        print("✅ Lector de logs iniciado correctamente")
        
        # Probar formateo de tamaño
        size_str = log_reader.format_size(1024 * 1024)
        print(f"✅ Formateo de tamaño: {size_str}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en lector de logs: {e}")
        return False

def main():
    """Ejecutar todas las pruebas"""
    print("🧪 INICIANDO PRUEBAS DEL SISTEMA DE SOPORTE TI")
    print("=" * 50)
    
    tests = [
        ("Importación de módulos", test_imports),
        ("Creación de directorios", test_directories),
        ("Sistema de tickets", test_ticket_system),
        ("Organizador de archivos", test_file_organizer),
        ("Lector de logs", test_log_reader)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
        else:
            print(f"❌ Falló la prueba: {test_name}")
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTADOS: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 Todas las pruebas pasaron correctamente")
        print("✅ El sistema está listo para usar")
    else:
        print("⚠️ Algunas pruebas fallaron")
        print("🔧 Revisa los errores mostrados arriba")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
