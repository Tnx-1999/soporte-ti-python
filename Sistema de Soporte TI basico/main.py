#!/usr/bin/env python3
"""
Sistema de Soporte TI Básico
Funcionalidades:
- Organización de archivos
- Registro de tickets simples
- Lectura de logs
"""

import os
import json
import datetime
from pathlib import Path
from modules.file_organizer import FileOrganizer
from modules.ticket_system import TicketSystem
from modules.log_reader import LogReader

class TISupportSystem:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.data_dir = self.base_dir / "data"
        self.ensure_directories()
        
        self.file_organizer = FileOrganizer(self.data_dir)
        self.ticket_system = TicketSystem(self.data_dir)
        self.log_reader = LogReader(self.data_dir)
    
    def ensure_directories(self):
        """Crear directorios necesarios para el sistema"""
        directories = [
            self.data_dir,
            self.data_dir / "files",
            self.data_dir / "tickets",
            self.data_dir / "logs",
            self.data_dir / "organized"
        ]
        
        for directory in directories:
            directory.mkdir(exist_ok=True)
    
    def show_menu(self):
        """Mostrar menú principal del sistema"""
        print("\n" + "="*50)
        print("SISTEMA DE SOPORTE TI Basico")
        print("="*50)
        print("              Matias Santander")
        print("1. Organizar archivos")
        print("2. Gestionar tickets")
        print("3. Leer logs")
        print("4. Salir")
        print("="*50)
    
    def run(self):
        """Ejecutar el sistema principal"""
        while True:
            self.show_menu()
            try:
                option = input("Seleccione una opción (1-4): ").strip()
                
                if option == "1":
                    self.file_organizer.menu()
                elif option == "2":
                    self.ticket_system.menu()
                elif option == "3":
                    self.log_reader.menu()
                elif option == "4":
                    print("¡Gracias por usar el Sistema de Soporte TI!")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except KeyboardInterrupt:
                print("\n\nSaliendo del sistema...")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    system = TISupportSystem()
    system.run()
