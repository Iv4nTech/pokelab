# 🔴 PokéLab: Team Builder & Analyzer

> **Una aplicación Full Stack para la gestión y análisis de equipos competitivos de Pokémon.**

## 📖 Descripción

**PokéLab** es una herramienta diseñada para entrenadores que necesitan organizar sus estrategias. Permite crear equipos, asignar Pokémon con relaciones complejas (tipos elementales, estadísticas) y analizar la composición del equipo en tiempo real.

Este proyecto fue desarrollado como un **reto técnico de 3 días (Hackathon Personal)** para demostrar dominio sobre la arquitectura MVT de Django, bases de datos relacionales y manipulación del DOM sin frameworks externos.

## 🚀 Características Técnicas

Este proyecto no es solo una Pokédex, es una demostración de arquitectura de software:

### Backend (Django)
- **Modelado de Datos Complejo:**
  - Relaciones **Many-to-Many** (Muchos a Muchos) para los Tipos Elementales.
  - Relaciones **Foreign Key** (Uno a Muchos) para la asignación de Equipos.
- **Class Based Views (CBV):** Uso extensivo de vistas genéricas (`ListView`, `DetailView`, `CreateView`) para un código limpio y mantenible.
- **ORM Optimization:** Uso de `annotate` y `prefetch_related` para evitar el problema de consultas N+1.

### Frontend (HTML/JS)
- **Interfaz Interactiva:** Manipulación del **DOM** en tiempo real con Vanilla JavaScript.
- **Cálculos en Cliente:** Barras de estadísticas y validaciones de equipo (máx 6) sin recargar la página.
- **Diseño Responsive:** CSS Grid y Flexbox para una visualización de tarjetas limpia.

## 🛠️ Stack Tecnológico

* **Backend:** Python, Django Framework.
* **Base de Datos:** SQLite (Dev).
* **Frontend:** HTML5, CSS3, JavaScript (ES6+).