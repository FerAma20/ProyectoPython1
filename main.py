import sys

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


def delete_cliente(cliente_name):
    global clientes
    if cliente_name in clientes:
        clientes =  clientes.replace(cliente_name + ",", "")
    else:
        print("Cliente no existe en la lista de clientes")


def search_client(cliente_name):
    global clientes
    clients_list = clientes.split(",")

    for clientes in clients_list:
        if clientes != cliente_name:
            continue
        else:
            return True


def _add_comma():
    global clientes

    clientes +=", "


def _print_welcome():
    print("Bienvenidos a L I O N ventas")
    print("*" * 50)
    print("Que decea hacer hoy? ")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


def _get_client_name():
    cliente_name = None
    while not cliente_name:
        cliente_name = input("Cual es el nombre del cliente: ")
        if cliente_name == "exit":
            cliente_name = None
            break
    if not cliente_name:
            sys.exit()

    return cliente_name


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()


    if command == "C":
        cliente_name = _get_client_name()
        create_client(cliente_name)
        list_clientes()


    elif command == "L":
        list_clientes()


    elif command == "D":
        cliente_name = _get_client_name()
        delete_cliente(cliente_name)
        list_clientes()

    elif command == "U":
        cliente_name = _get_client_name()
        update_client_name = input("Cual es el nombre del nuevo cliente? ")
        update_client(cliente_name, update_client_name)
        list_clientes()

    elif command == "S":
        cliente_name = _get_client_name()
        found = search_client(cliente_name)

        if found:
            print("El cliente esta en la lista de clientes! ")
        else:
            print("El cliente {} no existe en la lista de clientes".format(cliente_name))

    else:
        print('Comando es invalido')

