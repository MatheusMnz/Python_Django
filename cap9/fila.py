def clear_screen()->None:
    print('\n' * 100)


def verify_queue_is_empty(queue_a, flag=1) -> bool:
    empty_flag = False
    
    if queue_a and flag:
        print(queue_a)
        flag = False
    elif queue_a and not flag:
        flag = False

    if not queue_a:
        empty_flag = True

    if empty_flag and flag:
        print("Nenhum cliente a atender.")

    return empty_flag



def append_client(queue_a)->None:
    clear_screen()
    nome_client = str(input("Insira o nome: "))
    rg_client = str(input("Insira o rg: "))
    queue_a.appendleft({nome_client:rg_client})
    input("Tecle enter para retornar ao menu. ")



def call_client(queue_a)->None:
    clear_screen()
    if  not verify_queue_is_empty(queue_a, 0):
        user_actual = queue_a.popleft()
        print(f"Atendendo o cliente {user_actual}")
        print(f"Restam {len(queue_a)} clientes na fila")
        input("Tecle enter para retornar ao menu. ")
    else:
        print("Nenhum cliente na fila. ")    
        input("Tecle enter para retornar ao menu. ")
