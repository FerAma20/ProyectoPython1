clientes  = 'pablo, ricardo, '


def create_client(cliente_name):
    global clientes
    
    if cliente_name  not in clientes:
        clientes +=cliente_name
        _add_comma()
    else:
        print('Cliente ya esta en la lista de clientes ')   


def list_clientes():
    global clientes
    print(clientes)


def update_client(cliente_name, update_client_name):
    global clientes
    if cliente_name in clientes:
        clientes = clientes.replace(cliente_name + ",", update_client_name +",")
    else:
        print("Cliente no existente en la lista ")


def _add_comma():
    global clientes

    clientes +=", "


def _print_welcome():
    print("Bienvenidos a L I O N ventas")
    print("*" * 50)
    print("Que decea hacer hoy? ")
    print("[C]reate clients")
    print("[U]pdate clients")
    print("[D]elete clients")


def _get_client_name():
    return input("Cual es el nombre del cliente? ")


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()


    if command == "C":
        cliente_name = _get_client_name()
        create_client(cliente_name)
        list_clientes()


    elif command == "D":
        pass
    elif command == "U":
        cliente_name = _get_client_name()
        update_client_name = input("Cual es el nombre del nuevo cliente? ")
        update_client(cliente_name, update_client_name)
        list_clientes()
    else:
        print('Comando es invalido')

