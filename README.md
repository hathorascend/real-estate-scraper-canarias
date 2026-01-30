# 🏠 Real Estate Scraper Canarias

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Aplicación web profesional de scraping inmobiliario para las Islas Canarias con diseño moderno, integración con Google Sheets y detección automática de anuncios de particulares.**

## ✨ Características

- 🎨 **Diseño moderno** con Glassmorphism y gradientes
- 🏝️ **Cobertura completa** de las 7 Islas Canarias
- 🌐 **Multi-portal**: Idealista, Fotocasa (extensible)
- 👤 **Detección inteligente** de particulares vs agencias
- ☁️ **Sincronización** automática con Google Sheets
- 📊 **Dashboard interactivo** con métricas en tiempo real
- 🔍 **Filtros avanzados** por isla, precio, tipo de anuncio
- 📱 **Responsive** y optimizado para móviles

## 🚀 Demo

**URL de la app**: `https://real-estate-scraper-canarias.streamlit.app`  
*(Configurar después del deploy)*

## 📋 Requisitos Previos

1. **Cuenta de Google Cloud** con Service Account configurado
2. **Google Sheet** creada y compartida con el Service Account
3. **Cuenta de GitHub** para el repositorio
4. **Cuenta de Streamlit Cloud** para el despliegue

## 🛠️ Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/hathorascend/real-estate-scraper-canarias.git
cd real-estate-scraper-canarias
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar Google Cloud

1. Ir a [Google Cloud Console](https://console.cloud.google.com)
2. Crear un proyecto nuevo o usar uno existente
3. Habilitar las APIs:
   - Google Sheets API
   - Google Drive API
4. Crear Service Account:
   - IAM & Admin → Service Accounts → Create Service Account
   - Descargar el archivo JSON de credenciales

### 4. Configurar Google Sheets

1. Crear una Google Sheet con el nombre: `Real Estate Scraper - Canarias`
2. Crear una pestaña llamada `Inmuebles`
3. Agregar los siguientes encabezados en la primera fila:
   ```
   id | portal | isla | municipios | tipo_anuncio | titulo | precio | m2 | precio_m2 | piso_numero | habitaciones | banos | ascensor | anuncio_link | contacto_nombre | contacto_telefono | contacto_email | es_particular | fecha_captura
   ```
4. Compartir la hoja con el email del Service Account (encontrado en el JSON) con permisos de **Editor**

### 5. Configurar Secrets (Local)

Crear archivo `.streamlit/secrets.toml`:

```toml
[gcp_service_account]
type = \"service_account\"
project_id = \"tu-proyecto-id\"
private_key_id = \"tu-private-key-id\"
private_key = \"-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n\"
client_email = \"tu-service-account@tu-proyecto.iam.gserviceaccount.com\"
client_id = \"123456789\"
auth_uri = \"https://accounts.google.com/o/oauth2/auth\"
token_uri = \"https://oauth2.googleapis.com/token\"
auth_provider_x509_cert_url = \"https://www.googleapis.com/oauth2/v1/certs\"
client_x509_cert_url = \"https://www.googleapis.com/robot/v1/metadata/x509/...\"

gsheet_id = \"tu-google-sheet-id-aqui\"
```

## 🌐 Desplegar en Streamlit Cloud

1. Ir a [share.streamlit.io](https://share.streamlit.io)
2. Conectar tu cuenta de GitHub
3. Seleccionar el repositorio `real-estate-scraper-canarias`
4. En **Advanced settings → Secrets**, pegar el contenido del archivo `secrets.toml`
5. Hacer clic en **Deploy**

## 📊 Uso

### Interfaz Principal

1. **Sidebar** (izquierda):
   - Seleccionar islas a escanear
   - Elegir portales (Idealista, Fotocasa)
   - Filtrar por tipo (Particulares/Agencias/Todos)
   - Rango de precios
   - Opciones adicionales

2. **Dashboard** (centro):
   - Métricas en tiempo real
   - Tabla de resultados
   - Opciones de exportación

### API de Scraping

Los scrapers están en modo DEMO. Para implementación real:

```python
# Usar Selenium con rotating proxies
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_idealista_real(isla, municipio):
    # Implementar lógica real de scraping
    # con manejo de anti-bot
    pass
```

## 📁 Estructura del Proyecto

```
real-estate-scraper-canarias/
│
├── app.py                    # Aplicación principal
├── requirements.txt          # Dependencias
├── README.md                # Este archivo
├── .streamlit/
│   └── secrets.toml         # Configuración (no subir a Git)
├── scrapers/                # Módulos de scraping (futuro)
│   ├── idealista.py
│   └── fotocasa.py
└── utils/                   # Utilidades (futuro)
    ├── sheets.py
    └── filters.py
```

## 🎨 Diseño y CSS

La aplicación utiliza un diseño moderno con:

- **Glassmorphism**: Efectos de vidrio esmerilado en tarjetas
- **Gradientes**: Fondos con degradados púrpura-azul
- **Animaciones suaves**: Transiciones en hover
- **Responsive**: Adaptable a móviles y tablets

## ⚠️ Consideraciones Legales

Este proyecto es **educativo**. El scraping de sitios web puede violar los términos de servicio. Antes de usar:

1. Revisar los `robots.txt` de cada portal
2. Consultar términos de servicio
3. Implementar rate limiting
4. Usar proxies rotativos
5. Considerar APIs oficiales cuando estén disponibles

## 🔐 Seguridad

- **Nunca** subir el archivo `secrets.toml` a Git
- Agregar `.streamlit/secrets.toml` al `.gitignore`
- Rotar credenciales periódicamente
- Usar variables de entorno en producción

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crear una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abrir un Pull Request

## 📝 TODO

- [ ] Implementar scrapers reales con Selenium
- [ ] Agregar más portales (Habitaclia, Pisos.com)
- [ ] Sistema de notificaciones por email
- [ ] Exportar a Excel/PDF
- [ ] Análisis de precios con gráficos
- [ ] Integración con WhatsApp API

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Hathor Ascend**  
📧 Email: info@hathorascend.com  
🌐 Web: https://hathorascend.com

---

⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!
"
