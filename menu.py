from usuario import Usuario
from usuario_DAO import usuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1.Listar usuario')
    print('2.Agregar usuario')
    print('3.Modificar usuario')
    print('4.Eliminar usuario')
    print('5.Salir')

    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        usuarios = usuarioDAO.selecccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion == 2:
        username_var = input('Escribe el username: ')
        password_var = input('Escribe la contraseña: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = usuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe la nueva contraseña: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = usuarioDAO.actualizar(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar'))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuario_eliminados = usuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuario_eliminados}')
else:
    log.info('Salimos de la aplicacion...')