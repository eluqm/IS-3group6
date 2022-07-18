# Ingenieria de Software III - Grupo 06

---

## Integrantes

- Angel Tomas Concha Layme
- Huayllasco Carlos, Edward
- Aquise Santos, Angela Margarita
- Kate Itati, Olazabal Chavez
- Jorge Alfredo, Tito Ccahuaya

---

# WorldCare

![ScreenShot](/img/wordcare.png)

### 1. Introducción

#### 1.1. Propósito

Crear un sitio web que permita a un usuario realizar cálculos y consultas sobre su huella de carbono, así como descubrir noticias positivas y recomendaciones positivas relacionadas con el cuidado del medio ambiente y de esta manera impulsar la mejora medioambiental mediante el reconocimiento de cada aporte brindado por las personas.

#### 1.2. Ámbito del sistema

Este proyecto está dirigido al público en general, que estén interesados en el cuidado del medio ambiente, los cuales tendrán la posibilidad de ver su huella de carbono de manera descriptiva, entendiendo el impacto positivo que consiguieron con sus aportes.

### 2. Recursos Humanos

La división de cada integrante para que aporte en un ámbito en específico es muy importante ya que de esta manera podemos distribuir el trabajo de una manera mucho más fácil y equitativa, por eso usando la metodología Scrum decidimos distribuir el grupo de la siguiente manera:

#### 2.1. Scrum Master

El Scrum Master de nuestro equipo es Kate Itati Olazabal Chavez ya que fue quien nos dio la idea de realizar este proyecto, por eso desempeña este cargo ya que podr guiarnos y al mismo tiempo resolver cualquier problema que surja.

#### 2.2. Product Owner

El Product Owner de nuestro equipo es Angel Concha Layme, él será la voz del cliente, en otras palabras, será el enlace entre un cliente y nuestro equipo de desarrollo. Él lleva la visión del producto y lo que se necesita desarrollar, además de gestionar los comentarios de los usuarios.

#### 2.3. Scrum Team

El Scrum Team estara compuesto por Angela Aquise Santos, Edward Luis Huayllasco Carlos, Jorge Alfredo Tito, quienes serán los encargados de convertir World Care en un software entregable. En este caso decidimos dividir el trabajo de cada uno de nosotros en dos partes.

- Diseñador:

La encargada de generar el diseño del sistema es Angela Aquise Santos, quien va a generar el diseño arquitectonico y el diseño detallado del sistema con base en los requisitos.

- Programadores:

Los encargados son Edward Luis Huayllasco y Jorge Alfredo Tito, que tienen la capacidad de convertir los requisitos del sistema en código fuente ejecutable utilizando uno o más lenguajes de programación, así como herramientas de apoyo.

### 3. Descripción General

#### 3.1. Perspectiva del producto

WorldCare es una alternativa amigable en comparción a las calculadoras de huella de carbono, que si bien son de fácil acceso y distribución, WorldCare presenta las contribuciones de los usuarios como impactos positivos hacia el planeta, lo que pretende mostrar el valor que tiene cada aporte hecho por los usuarios y estos se mantengan motivados ha realizar más aportes en un futuro.

#### 3.2. Funciones del producto

#### 3.3. Caráteristicas del usuario

### 4. Requesitos Específicos

#### 4.1. Requisitos Funcionales

- RF-001: Autenticación de Usuario
  Los usuarios registrados deberán identificarse para poder llevar un perfil de usuario.
- RF-002: Registro de Usuario
  El sistema permitirá a los usuarios registrarse. El usuario debe suministrar datos como: Nombre, Apellido, E-mail, Usuario y Password
- RF-003: Consultar tema de interés
  El sistema permitirá a los usuarios realizar busquedas relacionadas al tema de su interés
- RF-004: Consultar huella de carbono
  El sistema permitirá a los usuarios realizar el cálculo de su huella de carbono
- RF-005: Registro de Aportes
  El sistema permitirá a los usuarios llevar un registro de sus aportes
- RF-006: Compartir Aportes
  El sistema permitirá a los usuarios compartir sus logros
- RF-007: Cálculo por categorías
  El sistema permitirá a los usuarios realizar el cálculo de su huella de carbono por categorías
- RF-008: Brindar Información
  El sistema ofrecerá al usuario información general acerca del cuidado ambiental (tips de cuidado ambiental, noticias favorables al medio ambiente, calendario de eventos)
- RF-009: Publicación de Usuarios
  El sistema permitirá a los usuarios hacer una solicitud para publicar sus logros, ideas, tips, avances, etc.
- RF-010: Calificación de publicaciones
  El sistema permitirá a los usuarios calificar los tips de otros usuarios.
- RF-011: Revisión de solicitudes
  El sistema permitirá al administrador revisar las solicitudes del usuario y aprobarlas o desaprobarlas.
- RF-012: Gestión de información
  El sistema permitirá al administrador modificar la base de datos, ver registro general, realizar consultas, añadir información, etc.
- RF-013: Gestión de Usuarios
  El sistema permitirá al administrador visualizar los datos de los usuarios.

#### 4.2. Requisitos No funcionales

- RNF-001:
  El sistema debe tener una interfaz de uso intuitivo y sencillo
- RNF-002:
  El sistema debe contar con manuales de usuario estructurados adecuadamente.
- RNF-003:
  La aplicación web debe poseer un diseño “Responsive” a fin de garantizar la adecuada visualización en múltiples computadores personales, dispositivos tablets y teléfonos inteligentes.
- RNF-004:
  Toda funcionalidad del sistema debe responder en un tiempo razonable.
- RNF-005:
  Los permisos de acceso al sistema podrán ser cambiados solamente por el administrador de acceso a datos.
- RNF-006:
  El despliegue del software

### 5. Prerequisitos

_Mysql Workbench_

```
create database huella_carbono;
```

_Dependencias_

```
pip install Flask
pip install PyMySQL
pip install Flask-SQLAlchemy
pip install Flask_User
```

### 6. Mockups

link: https://app.moqups.com/MCtx2luPEu6uTzCcZyKaxHwRoK6f3Dw2/view/page/ae973f342

### 6. Trello

link: https://trello.com/b/3FwjQZeS/worldcare
