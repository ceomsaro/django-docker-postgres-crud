
```md
# 📚 Books CRUD — Django + Docker + PostgreSQL

Aplicación CRUD desarrollada con **Django**, containerizada con **Docker** y orquestada con **Docker Compose**.  
La aplicación utiliza **PostgreSQL** como base de datos, con persistencia de datos mediante volúmenes y configuración desacoplada usando variables de entorno.

Este proyecto fue construido con enfoque **DevOps**, priorizando reproducibilidad, separación de responsabilidades y automatización.

---

## 🚀 Tecnologías utilizadas

- Python / Django
- PostgreSQL
- Docker
- Docker Compose

---

## 🧱 Arquitectura

El proyecto está compuesto por dos servicios principales:

- **web**: aplicación Django
- **db**: base de datos PostgreSQL

Características clave:
- Contenedores efímeros
- Base de datos desacoplada de la aplicación
- Persistencia de datos mediante volúmenes Docker
- Migraciones automáticas al arranque
- Configuración mediante variables de entorno

---

## 🗂️ Diagrama de arquitectura

```

┌───────────────┐
│   Navegador   │
│   (Usuario)   │
└───────┬───────┘
│ HTTP
▼
┌────────────────────────┐
│   Django Application   │
│   (Docker Container)  │
│                        │
│  - Views               │
│  - Models              │
│  - Migrations          │
└──────────┬─────────────┘
│
│ PostgreSQL connection
▼
┌────────────────────────┐
│      PostgreSQL        │
│   (Docker Container)  │
│                        │
│  Persistent Volume     │
│  /var/lib/postgresql   │
└────────────────────────┘

````

La aplicación Django se comunica con PostgreSQL a través de una red interna de Docker.  
La base de datos utiliza un volumen para garantizar la persistencia de los datos, independientemente del ciclo de vida de los contenedores.

---

## ⚙️ Requisitos

- Docker
- Docker Compose

(No es necesario tener Python ni PostgreSQL instalados localmente)

---

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd books-crud-django
````

---

### 2️⃣ Crear archivo de variables de entorno

Copiar el archivo de ejemplo:

```bash
cp .env.example .env
```

El archivo `.env` contiene la configuración de la base de datos.

---

### 3️⃣ Levantar la aplicación

```bash
docker compose up --build
```

Docker se encargará automáticamente de:

* Construir las imágenes
* Levantar PostgreSQL
* Aplicar migraciones
* Iniciar el servidor Django

---

## 🌐 Accesos

* Aplicación:
  [http://localhost:8000](http://localhost:8000)

* Panel de administración:
  [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🧠 Características DevOps implementadas

* Uso de Docker para entornos reproducibles
* Separación entre aplicación y base de datos
* Persistencia de datos con volúmenes Docker
* Migraciones automáticas al iniciar el contenedor
* Configuración desacoplada del código mediante `.env`
* Proyecto ejecutable con un solo comando

---

## 📌 Aprendizajes clave

* Diferencia entre imagen y contenedor
* Manejo de estado en aplicaciones containerizadas
* Orquestación de servicios con Docker Compose
* Buenas prácticas para proyectos listos para producción

---

## 📈 Posibles mejoras

* Implementar CI/CD
* Separar configuración por entornos (dev / prod)
* Despliegue en la nube
* Autenticación y permisos avanzados
