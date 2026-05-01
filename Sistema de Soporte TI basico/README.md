# Sistema de Soporte TI Básico

Un sistema simple de soporte técnico desarrollado en Python que permite organizar archivos, gestionar tickets de soporte y leer archivos de log.

## Características

### 📁 Organización de Archivos
- Listar archivos disponibles con información de tamaño y fecha
- Organizar archivos automáticamente por tipo (documentos, imágenes, videos, etc.)
- Organizar archivos por fecha de modificación
- Organizar archivos por tamaño (pequeños, medianos, grandes)
- Mover archivos manualmente a carpetas específicas

### 🎫 Sistema de Tickets
- Crear tickets de soporte con título, descripción, prioridad y solicitante
- Listar todos los tickets con filtros
- Buscar tickets por ID o palabra clave
- Actualizar estado de tickets (abierto, en_progreso, resuelto, cerrado)
- Ver detalles completos de tickets con historial de comentarios
- Eliminar tickets
- Ver estadísticas del sistema de tickets

### 📋 Lector de Logs
- Listar archivos de log disponibles
- Ver contenido completo de archivos de log
- Buscar texto específico en todos los logs
- Filtrar logs por nivel de error (ERROR, WARNING, INFO, DEBUG, CRITICAL)
- Ver últimas líneas de archivos de log
- Analizar patrones comunes (IPs, fechas, URLs, emails)
- Crear logs de ejemplo para pruebas

## Requisitos

- Python 3.6 o superior
- No se requieren dependencias externas (usa solo módulos estándar)

## Instalación

1. Clonar o descargar el proyecto
2. Navegar al directorio del proyecto
3. Ejecutar el sistema:

```bash
python main.py
```

## Estructura del Proyecto

```
Sistema de Soporte TI basico/
├── main.py                 # Archivo principal del sistema
├── modules/
│   ├── __init__.py
│   ├── file_organizer.py   # Módulo de organización de archivos
│   ├── ticket_system.py    # Módulo de gestión de tickets
│   └── log_reader.py       # Módulo de lectura de logs
├── data/                   # Directorio de datos (creado automáticamente)
│   ├── files/             # Archivos para organizar
│   ├── tickets/           # Base de datos de tickets
│   ├── logs/              # Archivos de log
│   └── organized/         # Archivos organizados
├── requirements.txt        # Dependencias (mínimas)
└── README.md              # Este archivo
```

## Uso

### Inicio
Al ejecutar `main.py`, verás el menú principal:

```
==================================================
SISTEMA DE SOPORTE TI BÁSICO
==================================================
1. Organizar archivos
2. Gestionar tickets
3. Leer logs
4. Salir
==================================================
```

### Organizar Archivos
1. Coloca los archivos que quieres organizar en `data/files/`
2. Selecciona la opción 1 del menú principal
3. Elige el método de organización:
   - Por tipo: agrupa por extensión (.pdf, .jpg, etc.)
   - Por fecha: agrupa por mes de modificación
   - Por tamaño: agrupa en pequeños (<1MB), medianos (<10MB), grandes (>=10MB)

### Gestionar Tickets
1. Selecciona la opción 2 del menú principal
2. Crea nuevos tickets con información detallada
3. Actualiza estados y realiza seguimiento
4. Consulta estadísticas del sistema

### Leer Logs
1. Coloca tus archivos de log en `data/logs/`
2. Selecciona la opción 3 del menú principal
3. Usa las herramientas de búsqueda y filtrado
4. Analiza patrones y encuentra información relevante

## Características Técnicas

- **Base de datos**: Los tickets se almacenan en formato JSON
- **Manejo de archivos**: Usa pathlib para compatibilidad multiplataforma
- **Codificación**: UTF-8 para soporte de caracteres especiales
- **Manejo de errores**: Captura de excepciones para mayor robustez
- **Interfaz**: Consola interactiva con menús intuitivos

## Extensiones Futuras

El sistema está diseñado para ser extensible. Algunas ideas para futuras versiones:

- Interfaz web usando Flask o FastAPI
- Base de datos SQL (SQLite, PostgreSQL)
- Sistema de notificaciones por email
- Integración con sistemas de monitoreo
- Dashboard con gráficos y estadísticas
- Sistema de usuarios y permisos
- API REST para integración con otros sistemas

## Contribuciones

¡Las contribuciones son bienvenidas! Algunas áreas para mejorar:

- Optimización de algoritmos de búsqueda
- Mejora de la interfaz de usuario
- Agregar más patrones de análisis de logs
- Internacionalización (i18n)
- Pruebas unitarias

## Licencia

Este proyecto es de código abierto y disponible bajo la Licencia MIT.

## Soporte

Para reportar problemas o solicitar características, por favor abre un issue en el repositorio del proyecto.

---

**Nota**: Este es un sistema básico diseñado para pequeñas organizaciones o como punto de partida para sistemas más complejos.
