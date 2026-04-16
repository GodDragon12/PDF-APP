# APP PDF EDITOR

Aplicación web para cargar, visualizar, anotar y exportar planos PDF.

## Estructura del proyecto
- Backend: FastAPI
- Frontend: PDF.js + Fabric.js
- Funcionalidades:
  - Subida de PDF
  - Anotación en navegador
  - Exportación de PDF anotado
  - Compresión
  - Conversión a DOCX
  - Conversión a DWG

## Scripts
- install_dependencies.ps1 → instala dependencias
- run_server.ps1 → inicia el servidor FastAPI

## Rutas
- / → interfaz principal
- /upload → subir PDF
