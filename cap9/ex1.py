import fila
from collections import deque

# Crio a fila
queue = deque()

while(True):        
    option_selected = int(input("Selecione a opção: \n[1]: Consultar\n[2]: Incluir\n[3]: Atender\n[4]: Sair\n-----> "))
    fila.clear_screen()
    match option_selected:
        case 1:
            fila.verify_queue_is_empty(queue)
        case 2:
           fila.append_client(queue)
        case 3:
            fila.call_client(queue)
        case 4:
            break

print("Programa finalizado pelo usuário")