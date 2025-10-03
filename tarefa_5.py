print ("--- Minha Lista de Tarefas ---")
try:
 with open ("tarefas .txt ", "r") as arquivo_tarefas:
    numero_tarefa = 1
    for tarefa in arquivo_tarefas :

        print( f"{ numero_tarefa }. { tarefa.strip ()}")
        numero_tarefa += 1 
 numero_tarefa + 1
except FileNotFoundError :
    print("Arquivo 'tarefas .txt ' não encontrado.Rode o exercicio 4 primeiro .")