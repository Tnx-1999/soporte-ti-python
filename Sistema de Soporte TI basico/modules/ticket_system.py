"""
Módulo de Sistema de Tickets
Permite crear, gestionar y seguir tickets de soporte
"""

import json
import datetime
from pathlib import Path

class TicketSystem:
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.tickets_dir = self.data_dir / "tickets"
        self.tickets_file = self.tickets_dir / "tickets.json"
        self.ensure_ticket_file()
    
    def ensure_ticket_file(self):
        """Crear archivo de tickets si no existe"""
        self.tickets_dir.mkdir(exist_ok=True)
        if not self.tickets_file.exists():
            with open(self.tickets_file, 'w', encoding='utf-8') as f:
                json.dump([], f)
    
    def load_tickets(self):
        """Cargar tickets desde archivo"""
        try:
            with open(self.tickets_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_tickets(self, tickets):
        """Guardar tickets en archivo"""
        with open(self.tickets_file, 'w', encoding='utf-8') as f:
            json.dump(tickets, f, indent=2, ensure_ascii=False)
    
    def generate_ticket_id(self):
        """Generar ID único para ticket"""
        tickets = self.load_tickets()
        if not tickets:
            return "TKT-001"
        
        max_id = 0
        for ticket in tickets:
            ticket_num = int(ticket['id'].split('-')[1])
            if ticket_num > max_id:
                max_id = ticket_num
        
        return f"TKT-{max_id + 1:03d}"
    
    def menu(self):
        """Menú del sistema de tickets"""
        while True:
            print("\n" + "-"*40)
            print("SISTEMA DE TICKETS")
            print("-"*40)
            print("1. Crear nuevo ticket")
            print("2. Listar todos los tickets")
            print("3. Buscar ticket")
            print("4. Actualizar estado de ticket")
            print("5. Ver detalles de ticket")
            print("6. Eliminar ticket")
            print("7. Estadísticas")
            print("8. Volver al menú principal")
            print("-"*40)
            
            try:
                option = input("Seleccione una opción (1-8): ").strip()
                
                if option == "1":
                    self.create_ticket()
                elif option == "2":
                    self.list_tickets()
                elif option == "3":
                    self.search_ticket()
                elif option == "4":
                    self.update_ticket_status()
                elif option == "5":
                    self.view_ticket_details()
                elif option == "6":
                    self.delete_ticket()
                elif option == "7":
                    self.show_statistics()
                elif option == "8":
                    break
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"Error: {e}")
    
    def create_ticket(self):
        """Crear un nuevo ticket"""
        print("\n" + "="*30)
        print("CREAR NUEVO TICKET")
        print("="*30)
        
        try:
            title = input("Título del problema: ").strip()
            if not title:
                print("El título es obligatorio.")
                return
            
            description = input("Descripción detallada: ").strip()
            if not description:
                print("La descripción es obligatoria.")
                return
            
            priority = input("Prioridad (baja/media/alta): ").strip().lower()
            if priority not in ['baja', 'media', 'alta']:
                print("Prioridad no válida. Use: baja, media o alta.")
                return
            
            requester = input("Solicitante: ").strip()
            if not requester:
                requester = "Anónimo"
            
            ticket = {
                'id': self.generate_ticket_id(),
                'title': title,
                'description': description,
                'priority': priority,
                'status': 'abierto',
                'requester': requester,
                'created_at': datetime.datetime.now().isoformat(),
                'updated_at': datetime.datetime.now().isoformat(),
                'assigned_to': None,
                'comments': []
            }
            
            tickets = self.load_tickets()
            tickets.append(ticket)
            self.save_tickets(tickets)
            
            print(f"\n✓ Ticket creado exitosamente!")
            print(f"ID del ticket: {ticket['id']}")
            
        except Exception as e:
            print(f"Error al crear ticket: {e}")
    
    def list_tickets(self, filter_status=None):
        """Listar tickets con filtro opcional"""
        tickets = self.load_tickets()
        
        if filter_status:
            tickets = [t for t in tickets if t['status'] == filter_status]
        
        if not tickets:
            print("No hay tickets para mostrar.")
            return
        
        print(f"\n{'ID':<10} {'Título':<25} {'Estado':<10} {'Prioridad':<10} {'Fecha':<12}")
        print("-"*70)
        
        for ticket in sorted(tickets, key=lambda x: x['created_at'], reverse=True):
            created_date = datetime.datetime.fromisoformat(ticket['created_at']).strftime('%Y-%m-%d')
            title_short = ticket['title'][:22] + "..." if len(ticket['title']) > 22 else ticket['title']
            print(f"{ticket['id']:<10} {title_short:<25} {ticket['status']:<10} {ticket['priority']:<10} {created_date:<12}")
    
    def search_ticket(self):
        """Buscar ticket por ID o palabra clave"""
        search_term = input("Ingrese ID del ticket o palabra clave: ").strip().lower()
        
        if not search_term:
            print("Debe ingresar un término de búsqueda.")
            return
        
        tickets = self.load_tickets()
        found_tickets = []
        
        for ticket in tickets:
            if (search_term in ticket['id'].lower() or 
                search_term in ticket['title'].lower() or 
                search_term in ticket['description'].lower()):
                found_tickets.append(ticket)
        
        if not found_tickets:
            print("No se encontraron tickets.")
            return
        
        print(f"\nSe encontraron {len(found_tickets)} tickets:")
        print("-"*70)
        
        for ticket in found_tickets:
            created_date = datetime.datetime.fromisoformat(ticket['created_at']).strftime('%Y-%m-%d')
            print(f"ID: {ticket['id']}")
            print(f"Título: {ticket['title']}")
            print(f"Estado: {ticket['status']} | Prioridad: {ticket['priority']}")
            print(f"Fecha: {created_date}")
            print("-"*40)
    
    def update_ticket_status(self):
        """Actualizar estado de un ticket"""
        ticket_id = input("Ingrese ID del ticket: ").strip().upper()
        
        tickets = self.load_tickets()
        ticket = None
        
        for t in tickets:
            if t['id'] == ticket_id:
                ticket = t
                break
        
        if not ticket:
            print("Ticket no encontrado.")
            return
        
        print(f"\nTicket actual: {ticket['title']}")
        print(f"Estado actual: {ticket['status']}")
        
        print("\nEstados disponibles:")
        print("1. abierto")
        print("2. en_progreso")
        print("3. resuelto")
        print("4. cerrado")
        
        status_map = {
            '1': 'abierto',
            '2': 'en_progreso',
            '3': 'resuelto',
            '4': 'cerrado'
        }
        
        choice = input("Seleccione nuevo estado (1-4): ").strip()
        
        if choice not in status_map:
            print("Opción no válida.")
            return
        
        old_status = ticket['status']
        ticket['status'] = status_map[choice]
        ticket['updated_at'] = datetime.datetime.now().isoformat()
        
        # Agregar comentario automático
        comment = f"Estado cambiado de '{old_status}' a '{ticket['status']}'"
        ticket['comments'].append({
            'timestamp': datetime.datetime.now().isoformat(),
            'comment': comment,
            'author': 'Sistema'
        })
        
        self.save_tickets(tickets)
        print(f"✓ Estado del ticket {ticket_id} actualizado a '{ticket['status']}'")
    
    def view_ticket_details(self):
        """Ver detalles completos de un ticket"""
        ticket_id = input("Ingrese ID del ticket: ").strip().upper()
        
        tickets = self.load_tickets()
        
        for ticket in tickets:
            if ticket['id'] == ticket_id:
                print("\n" + "="*50)
                print(f"DETALLES DEL TICKET {ticket['id']}")
                print("="*50)
                print(f"Título: {ticket['title']}")
                print(f"Solicitante: {ticket['requester']}")
                print(f"Prioridad: {ticket['priority'].upper()}")
                print(f"Estado: {ticket['status'].replace('_', ' ').title()}")
                print(f"Asignado a: {ticket.get('assigned_to', 'Sin asignar')}")
                print(f"Creado: {datetime.datetime.fromisoformat(ticket['created_at']).strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Actualizado: {datetime.datetime.fromisoformat(ticket['updated_at']).strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"\nDescripción:")
                print("-"*30)
                print(ticket['description'])
                
                if ticket['comments']:
                    print(f"\nComentarios ({len(ticket['comments'])}):")
                    print("-"*30)
                    for comment in ticket['comments']:
                        timestamp = datetime.datetime.fromisoformat(comment['timestamp']).strftime('%Y-%m-%d %H:%M')
                        print(f"[{timestamp}] {comment['author']}: {comment['comment']}")
                
                print("="*50)
                return
        
        print("Ticket no encontrado.")
    
    def delete_ticket(self):
        """Eliminar un ticket"""
        ticket_id = input("Ingrese ID del ticket a eliminar: ").strip().upper()
        
        tickets = self.load_tickets()
        
        for i, ticket in enumerate(tickets):
            if ticket['id'] == ticket_id:
                print(f"\nTicket a eliminar: {ticket['title']}")
                confirm = input("¿Está seguro? (s/n): ").strip().lower()
                
                if confirm == 's':
                    del tickets[i]
                    self.save_tickets(tickets)
                    print(f"✓ Ticket {ticket_id} eliminado.")
                else:
                    print("Operación cancelada.")
                return
        
        print("Ticket no encontrado.")
    
    def show_statistics(self):
        """Mostrar estadísticas de tickets"""
        tickets = self.load_tickets()
        
        if not tickets:
            print("No hay tickets para mostrar estadísticas.")
            return
        
        total = len(tickets)
        status_counts = {}
        priority_counts = {}
        
        for ticket in tickets:
            # Contar por estado
            status = ticket['status']
            status_counts[status] = status_counts.get(status, 0) + 1
            
            # Contar por prioridad
            priority = ticket['priority']
            priority_counts[priority] = priority_counts.get(priority, 0) + 1
        
        print("\n" + "="*40)
        print("ESTADÍSTICAS DE TICKETS")
        print("="*40)
        print(f"Total de tickets: {total}")
        
        print(f"\nPor estado:")
        for status, count in status_counts.items():
            percentage = (count / total) * 100
            print(f"  {status.replace('_', ' ').title()}: {count} ({percentage:.1f}%)")
        
        print(f"\nPor prioridad:")
        for priority, count in priority_counts.items():
            percentage = (count / total) * 100
            print(f"  {priority.title()}: {count} ({percentage:.1f}%)")
        
        # Tickets recientes
        recent_tickets = sorted(tickets, key=lambda x: x['created_at'], reverse=True)[:5]
        print(f"\nÚltimos 5 tickets:")
        for ticket in recent_tickets:
            created_date = datetime.datetime.fromisoformat(ticket['created_at']).strftime('%Y-%m-%d')
            print(f"  {ticket['id']} - {ticket['title']} ({created_date})")
        
        print("="*40)
