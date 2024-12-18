# AlInfo - Repositorio Virtual de Ingeniería Alimentaria

## Este proyecto se creo con las siguientes tecnologías

# backend

- Postgresql
- Django Rest Framework

# fronted

- React JS
- Redux Toolkit
- Tailwind CSS

## Funcionalidades

- Login de usuario - Simple JWT
- Logout de usuario
- Registro de usuarios - Simple JWT
- Actualizar perfil de usuario
- Usuario personalizado con biografía, correo, nombre de usuario y foto de perfil
- Permisos de usuario (para que otros usuarios no borren o editen publicaciones de otros usuarios)
- Crear publicaciones
- Leer publicaciones
- Actualizar publicaciones
- Eliminar publicaciones
- Ver Perfil de otro usuarios
- Leer Todas las publicaciones de un usuario en su perfil
- Crear comentarios
- Borrar comentarios (Solo para usuarios con rol de admin o que sea el dueño del comentario)
- Leer comentarios de otros usuarios
- Buscador con filtros para videos, documentos y herramientas.
- Subir documentos con clasificación y tipo
- Consultar documentos
- Borrar documentos
- Editar documentos
- Subir videos con clasificación
- Consultar videos
- Borrar videos
- Editar videos
- Subir herramientas con clasificación
- Consultar herramientas
- Borrar herramientas
- Editar herramientas
- Generar reportes
- Ver Gráfico
- Enviar quejas y sugerencias

## Roles de Usuario

- Rol de Administrador de la API (admin API) - (Puede acceder al panel de administración de la API.)
- Rol de Administrador (admin) - (Puede hacer todas las funcionalidades del fronted.)
- Rol de Editor (editor)- (Puede hacer todas las funcionalidades, solo puede editar y borrar los elementos que el mismo haya subido)
- Rol de Lector (reader) - (solo puede consultar y subir comentarios o quejas y sugerencias)

## Reportes

- Listado de usuarios
- Listado de documentos
- Listado de videos
- Listado de herramientas
- Listado de quejas y sugerencias
- Listado de tipos de documentos
- Listado de clasificación de documentos
- Listado de clasificación de videos
- Listado de clasificación de herramientas

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más información.
