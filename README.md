# WorldCare

***

<p align="center">
  <img src='./img/logo.png' width='500px' />
</p>

## Introducción

***

### Propósito

Crear un sitio web que permita a un usuario realizar cálculos y consultas sobre su huella de carbono, así como descubrir noticias positivas y recomendaciones positivas relacionadas con el cuidado del medio ambiente y de esta manera impulsar la mejora medioambiental mediante el reconocimiento de cada aporte brindado por las personas.

### 1.2. Ámbito del sistema

Este proyecto está dirigido al público en general, que estén interesados en el cuidado del medio ambiente, los cuales tendrán la posibilidad de ver su huella de carbono de manera descriptiva, entendiendo el impacto positivo que consiguieron con sus aportes.

## Recursos Humanos

***

La división de cada integrante en un ámbito en específico, para así poder distribuir el trabajo de una manera mucho más fácil y equitativa, utilizando la metodología Scrum, decidimos dar los siguientes cargos a cada integrante:

### Scrum Master

El Scrum Master de nuestro equipo es Kate Itati Olazabal Chavez ya que fue quien tuvo la idea sobre este proyecto, ella será la encargada de guiarnos y resolver las dudas que nos puedan surgir en el desarrollo del proyecto.

### Product Owner

El Product Owner de nuestro equipo es Angel Concha Layme, él será la voz del cliente, en otras palabras, será el enlace entre un cliente y nuestro equipo de desarrollo. Él lleva la visión del producto y lo que se necesita desarrollar, además de gestionar los comentarios de los usuarios.

### Scrum Team

El Scrum Team estará compuesto por Angela Aquise Santos, Edward Luis Huayllasco Carlos, Jorge Alfredo Tito, quienes serán los encargados de convertir World Care en un software entregable. En este caso decidimos dividir el trabajo de cada uno de nosotros en dos partes.

#### Diseñadores

Quien se encargara de generar el diseño arquitectonico y el diseño detallado del sistema será Angela Aquise Santos, basandose en los requisitos.

#### Programadores

Los encargados son Edward Luis Huayllasco y Jorge Alfredo Tito, convertiran los requisitos del sistema en código fuente ejecutable utilizando uno o más lenguajes de programación, así como herramientas de apoyo.

## Descripción General

***

### Perspectiva del producto

WorldCare es una alternativa amigable en comparción a las calculadoras de huella de carbono, que si bien son de fácil acceso y distribución, WorldCare presenta las contribuciones de los usuarios como impactos positivos hacia el planeta, lo que pretende mostrar el valor que tiene cada aporte hecho por los usuarios y estos se mantengan motivados ha realizar más aportes en un futuro.

## Requesitos Específicos

***

### Requisitos Funcionales

* RF-001: Autenticación de Usuario
  Los usuarios registrados deberán identificarse para poder llevar un perfil de usuario.
* RF-002: Registro de Usuario
  El sistema permitirá a los usuarios registrarse. El usuario debe suministrar datos como: Nombre, Apellido, E-mail, Usuario y Password
* RF-003: Consultar tema de interés
  El sistema permitirá a los usuarios realizar busquedas relacionadas al tema de su interés
* RF-004: Consultar huella de carbono
  El sistema permitirá a los usuarios realizar el cálculo de su huella de carbono
* RF-005: Registro de Aportes
  El sistema permitirá a los usuarios llevar un registro de sus aportes
* RF-006: Compartir Aportes
  El sistema permitirá a los usuarios compartir sus logros
* RF-007: Cálculo por categorías
  El sistema permitirá a los usuarios realizar el cálculo de su huella de carbono por categorías
* RF-008: Brindar Información
  El sistema ofrecerá al usuario información general acerca del cuidado ambiental (tips de cuidado ambiental, noticias favorables al medio ambiente, calendario de eventos)
* RF-009: Publicación de Usuarios
  El sistema permitirá a los usuarios hacer una solicitud para publicar sus logros, ideas, tips, avances, etc.
* RF-010: Calificación de publicaciones
  El sistema permitirá a los usuarios calificar los tips de otros usuarios.
* RF-011: Revisión de solicitudes
  El sistema permitirá al administrador revisar las solicitudes del usuario y aprobarlas o desaprobarlas.
* RF-012: Gestión de información
  El sistema permitirá al administrador modificar la base de datos, ver registro general, realizar consultas, añadir información, etc.
* RF-013: Gestión de Usuarios
  El sistema permitirá al administrador visualizar los datos de los usuarios.

### Requisitos No funcionales

* RNF-001:
  El sistema debe tener una interfaz de uso intuitivo y sencillo
* RNF-002:
  El sistema debe contar con manuales de usuario estructurados adecuadamente.
* RNF-003:
  La aplicación web debe poseer un diseño “Responsive” a fin de garantizar la adecuada visualización en múltiples computadores personales, dispositivos tablets y teléfonos inteligentes.
* RNF-004:
  Toda funcionalidad del sistema debe responder en un tiempo razonable.
* RNF-005:
  Los permisos de acceso al sistema podrán ser cambiados solamente por el administrador de acceso a datos.
* RNF-006:
  El despliegue del software

## Guia de uso local

***

### Instalación local en Windows

  1. Descargar el software desde el [Repositorio](https://github.com/eluqm/IS-3group6)
  2. Instalar el software en una carpeta local
  3. Crear entorno virtual con la herramienta [virtualenv](https://virtualenv.pypa.io/en/latest/)
  4. Activar el entorno virtual con la herramienta [activate](https://virtualenv.pypa.io/en/latest/userguide/getting-started.html)
  5. Instalar las dependencias con la herramienta [pip](https://pip.pypa.io/en/latest/installing.html)  

   ```
    pip install Flask
    pip install PyMySQL
    pip install Flask-SQLAlchemy
    pip install Flask_User
  ```

  6. Crear la base de datos: 

```
create database huella_carbono;
```

  7. Iniciar el sistema en el entorno virtual:

  ```
  python3 main.py
  ```

### Instalación local en Linux

  1. Descargar el software desde el [Repositorio](https://github.com/eluqm/IS-3group6)
  2. Instalar el software en una carpeta local
  3. Crear entorno virtual con la herramienta [virtualenv](https://virtualenv.pypa.io/en/latest/)
  4. Activar el entorno virtual con la herramienta [activate](https://virtualenv.pypa.io/en/latest/userguide/getting-started.html)
  5. Instalar las dependencias con la herramienta [pip](https://pip.pypa.io/en/latest/installing.html)  

   ```
    pip install Flask
    pip install PyMySQL
    pip install Flask-SQLAlchemy
    pip install Flask_User
  ```

  6. Crear la base de datos: 

```
create database huella_carbono;
```

  7. Iniciar el sistema en el entorno virtual:

  ```
  python3 main.py
  ```


## Diseño del Sistema

***
El protetipo del producto se realizó en con la herramienta Figma, la cual esta a disposicion en el siguiente enlace:

<https://app.moqups.com/MCtx2luPEu6uTzCcZyKaxHwRoK6f3Dw2/view/page/ae973f342>

## Metodologia de desarrollo

***

<https://trello.com/b/3FwjQZeS/worldcare>
