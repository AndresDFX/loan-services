
# Loan Services

Loan Services es una aplicación Django que proporciona un sistema de gestión de préstamos, pagos y clientes. Este proyecto está dockerizado para facilitar su despliegue y desarrollo. Incorpora patrones de diseño como Repository, Service, y Specification para organizar la lógica de negocio de manera modular y mantenible. También incluye documentación API con Swagger.

## Características

- Gestión de clientes, préstamos y pagos.
- Arquitectura basada en patrones de diseño para un código limpio y mantenible.
- Dockerizado para fácil despliegue y desarrollo.
- Documentación API con Swagger.

## Tecnologías Utilizadas

- Django y Django REST Framework para el backend.
- PostgreSQL como sistema de gestión de base de datos.
- Docker para contenerización y orquestación.
- Swagger para documentación API.

## Patrones de Diseño Utilizados

- **Repository**: Abstrae la lógica de acceso a datos del dominio de la aplicación, permitiendo que el código de negocio sea independiente de la capa de acceso a datos.
  - Referencia: [Repository pattern](https://martinfowler.com/eaaCatalog/repository.html)

- **Service**: Define una capa de lógica de negocio que abstrae y encapsula toda la lógica de aplicación, coordinando las operaciones de los objetos del dominio.
  - Referencia: [Service layer pattern](https://www.martinfowler.com/eaaCatalog/serviceLayer.html)

- **Specification**: Permite la encapsulación de la lógica de selección en objetos específicos, lo que facilita la reutilización de la lógica de consulta.
  - Referencia: [Specification pattern](http://www.codinghelmet.com/?path=howto/specification-pattern)

## Puesta en Marcha

1. **Clonar el repositorio**

```bash
git clone https://AndresDFX/loan-services.git
cd loan-services
```

2. **Construir y levantar los contenedores con Docker**

```bash
docker-compose up --build
```

3. **Ejecutar migraciones**

```bash
docker-compose exec web python manage.py migrate
```

4. **Crear un superusuario (opcional)**

```bash
docker-compose exec web python manage.py createsuperuser
```

5. **Acceder a la documentación de la API**

Navega a `http://localhost:8000/swagger/` para ver la documentación Swagger de la API.

## Ejecución de Tests

Para ejecutar los tests, utiliza el comando:

```bash
docker-compose exec web pytest
```

## Servicios Implementados

- **Gestión de Clientes**: Permite el registro, actualización y consulta de clientes.
- **Gestión de Préstamos**: Permite la creación de préstamos asociados a clientes, así como su consulta y actualización.
- **Gestión de Pagos**: Permite registrar pagos realizados por los clientes, distribuyendo el monto entre los préstamos activos.


