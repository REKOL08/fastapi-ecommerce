# 🛒 FastAPI E-Commerce API

API REST completa con autenticación JWT, gestión de usuarios y productos. Construida con Python + FastAPI + MySQL.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat&logo=fastapi)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?style=flat&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=flat&logo=jsonwebtokens)
![Railway](https://img.shields.io/badge/Deploy-Railway-0B0D0E?style=flat&logo=railway)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🌐 Demo en vivo

**➡️ [https://fastapi-ecommerce-production-3f77.up.railway.app/docs](https://fastapi-ecommerce-production-3f77.up.railway.app/docs)**

> Puedes probar todos los endpoints directamente desde el navegador sin instalar nada.

---

## ✨ Features

✅ Registro y login con JWT Bearer Token
✅ Roles: `admin` y `customer` con control de acceso por endpoint
✅ CRUD completo de usuarios y productos
✅ Validaciones con Pydantic v2
✅ Documentación interactiva en `/docs` (Swagger UI)
✅ Tests unitarios con pytest usando SQLite en memoria
✅ Arquitectura por capas: models → schemas → services → endpoints

---

## 🏗️ Estructura del proyecto

```
fastapi-ecommerce/
├── app/
│   ├── api/v1/
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   └── products.py
│   │   └── router.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── deps.py
│   ├── db/
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   └── product.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── product.py
│   └── services/
│       ├── user_service.py
│       └── product_service.py
├── tests/
│   └── test_auth.py
├── main.py
├── requirements.txt
└── .env.example

---

## 🚀 Instalación y uso

### 1. Clonar y crear entorno virtual

```bash
git clone https://github.com/REKOL08/fastapi-ecommerce.git
cd fastapi-ecommerce
python -m venv .venv
source .venv/bin/activate
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env
```

### 3. Crear la base de datos en MySQL

```sql
CREATE DATABASE ecommerce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Levantar el servidor

```bash
uvicorn main:app --reload
```

Abre http://localhost:8000/docs para explorar la API.

---

## 🔑 Endpoints principales

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/api/v1/auth/register` | ❌ | Registrar usuario |
| POST | `/api/v1/auth/login` | ❌ | Login → obtiene JWT |
| GET | `/api/v1/users/me` | ✅ | Perfil actual |
| GET | `/api/v1/users/` | 🔐 Admin | Listar usuarios |
| GET | `/api/v1/products/` | ❌ | Listar productos |
| POST | `/api/v1/products/` | 🔐 Admin | Crear producto |
| PATCH | `/api/v1/products/{id}` | ✅ | Actualizar producto |
| DELETE | `/api/v1/products/{id}` | ✅ | Eliminar producto |

---

## 🧪 Tests

```bash
pytest tests/ -v
```

Los tests usan SQLite en memoria, no requieren MySQL.

---

## 🛠️ Stack tecnológico

| Herramienta | Uso |
|-------------|-----|
| FastAPI | Framework web async |
| SQLAlchemy 2.0 | ORM |
| PyMySQL | Driver MySQL |
| python-jose | Generación/validación JWT |
| passlib + bcrypt | Hash de contraseñas |
| Pydantic v2 | Validación y serialización |
| pytest + httpx | Testing |
| Railway | Deploy en la nube |

---

## 📄 Licencia

MIT © 2026 
