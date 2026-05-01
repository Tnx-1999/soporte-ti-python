# Guía de Instalación y Uso

## Requisitos Previos

1. **Python 3.6 o superior**
   - Descargar desde: https://python.org
   - Durante la instalación, marcar la opción "Add Python to PATH"

## Instalación Rápida

### Opción 1: Usando el archivo batch (Windows)

1. Double-click en `ejecutar.bat`
2. El sistema verificará si Python está instalado y ejecutará el programa

### Opción 2: Manualmente

1. Abrir una terminal/consola
2. Navegar al directorio del proyecto:
   ```bash
   cd "c:/Users/santa/OneDrive/Escritorio/GitHub/Sistema de Soporte TI basico"
   ```
3. Ejecutar el sistema:
   ```bash
   python main.py
   ```
   o si tienes Python 3:
   ```bash
   python3 main.py
   ```

## Verificación del Sistema

Para verificar que todo funciona correctamente:

```bash
python test_system.py
```

Este script ejecutará pruebas básicas para asegurar que:
- Todos los módulos se importen correctamente
- Los directorios necesarios se creen
- Las funcionalidades básicas operen

## Estructura de Directorios

El sistema creará automáticamente la siguiente estructura:

```
data/
├── files/          # Coloca aquí los archivos que quieres organizar
├── tickets/        # Base de datos de tickets (JSON)
├── logs/           # Coloca aquí tus archivos de log
└── organized/      # Archivos organizados automáticamente
```

## Primeros Pasos

### 1. Organizar Archivos
- Coloca archivos en `data/files/`
- Usa la opción 1 del menú principal
- Elige el método de organización

### 2. Crear Tickets
- Usa la opción 2 del menú principal
- Crea tickets con descripción detallada
- Asigna prioridades appropriate

### 3. Analizar Logs
- Coloca archivos `.log` en `data/logs/`
- Usa la opción 3 del menú principal
- Busca, filtra y analiza patrones

## Solución de Problemas

### Python no encontrado
- Asegúrate de haber marcado "Add Python to PATH" durante la instalación
- Reinicia tu terminal después de instalar Python
- Verifica la instalación con: `python --version`

### Error de permisos
- Ejecuta como administrador si es necesario
- Asegúrate de tener permisos de escritura en el directorio

### Archivos no encontrados
- Verifica que los directorios `data/files/` y `data/logs/` existan
- Coloca los archivos en los directorios correctos

## Características Adicionales

### Atajos de Teclado
- `Ctrl+C`: Salir del programa
- `Enter`: Confirmar selección

### Formatos Soportados
- **Archivos**: Todos los formatos
- **Logs**: `.log`, `.txt`
- **Tickets**: Almacenamiento en JSON

## Soporte

Si encuentras problemas:
1. Ejecuta `test_system.py` para diagnóstico
2. Revisa este archivo de instalación
3. Verifica que Python esté correctamente instalado

---

**Nota**: Este sistema está diseñado para ser ligero y no requiere dependencias externas.
