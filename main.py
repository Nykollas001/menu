import os  # Módulo para interagir com o sistema operacional
import random  # Módulo para gerar números aleatórios, usado no menu de cartas

# Dicionário de usuários cadastrados com exemplo inicial
usuarios = {"Host Nykollas": "Rockandsoul16+"}
usuario_logado = None  # Variável para armazenar o usuário logado no sistema
diario = []  # Lista para armazenar entradas do diário
armazenamento_senhas = {}  # Dicionário para guardar senhas (como um cofre virtual)
tier_list = []  # Lista para armazenar itens de uma tier list (classificações)
tier_list_name = None  # Nome da tier list ativa
notas = {}  # Dicionário para armazenar as notas de alunos
tarefas = []  # Lista para armazenar tarefas (to-do list)
lembretes = []  # Lista para armazenar lembretes
metas = []  # Lista para armazenar metas e objetivos
notas_rapidas = []  # Lista para armazenar notas rápidas

def limpar_tela():
    """
    Limpa o terminal para facilitar a leitura.
    É como apagar um quadro branco antes de escrever algo novo.
    """
    os.system("cls" if os.name == "nt" else "clear")  # 'cls' no Windows, 'clear' no Linux/Mac

def iniciar_programa():
    """
    Exibe o menu inicial do programa.
    É como a recepção de um prédio, onde você escolhe onde quer ir.
    """
    global usuario_logado  # Permite alterar a variável global de usuário logado
    while True:  # Loop infinito para o menu inicial
        limpar_tela()  # Organiza a saída do terminal
        print("=== BEM-VINDO AO SISTEMA ===")
        print("1. Fazer login")
        print("2. Cadastrar-se")
        print("3. Ver usuários cadastrados")
        print("4. Sair")

        # Lê a escolha do usuário
        opcao = obter_input("Escolha uma opção: ")
        if opcao == "4":  # Opção de sair
            print("Saindo do programa... Até logo!")
            break
        elif opcao == "1":  # Opção de login
            if fazer_login():  # Tenta fazer login
                input(f"\nOlá, {usuario_logado}! Pressione Enter para continuar.")  # Mensagem de boas-vindas
                main()  # Vai para o menu principal
        elif opcao == "2":  # Opção de cadastro
            cadastrar_usuario()
        elif opcao == "3":  # Exibe os usuários cadastrados
            visualizar_usuarios()
        else:
            print("Opção inválida. Tente novamente.")  # Tratamento de erro

def fazer_login():
    """
    Permite o usuário logar no sistema.
    É como usar uma chave para abrir a porta certa.
    """
    global usuarios, usuario_logado
    tentativas_restantes = 3  # Limita o número de tentativas
    while tentativas_restantes > 0:
        limpar_tela()
        print("=== LOGIN ===")
        print(f"Tentativas restantes: {tentativas_restantes}")

        # Entrada do nome de usuário e senha
        usuario = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()

        # Verifica se a combinação usuário/senha está correta
        if usuarios.get(usuario) == senha:
            usuario_logado = usuario
            print("Login realizado com sucesso!")  # Confirmação
            return True  # Login bem-sucedido
        else:
            tentativas_restantes -= 1  # Reduz as tentativas restantes
            print("Usuário ou senha incorretos.")
    print("Número de tentativas excedido. Retornando ao menu inicial.")
    return False  # Login falhou

def cadastrar_usuario():
    """
    Adiciona um novo usuário ao sistema.
    É como criar um crachá novo para um visitante.
    """
    global usuarios
    while True:
        limpar_tela()
        print("=== CADASTRO ===")
        usuario = input("Escolha um nome de usuário: ").strip()  # Novo nome de usuário
        if usuario in usuarios:
            print("Usuário já existe. Escolha outro nome.")  # Evita duplicatas
        else:
            senha = input("Escolha uma senha: ").strip()
            usuarios[usuario] = senha  # Adiciona ao dicionário de usuários
            print("Usuário cadastrado com sucesso!")
            break

def visualizar_usuarios():
    """
    Mostra todos os usuários cadastrados.
    É como abrir um livro de registros para consulta.
    """
    limpar_tela()
    print("=== USUÁRIOS CADASTRADOS ===")
    for i, usuario in enumerate(usuarios.keys(), 1):  # Enumera os usuários
        print(f"{i}. {usuario}")
    input("\nPressione Enter para voltar ao menu.")

def main():
    """
    Menu principal do programa.
    É como a praça de alimentação de um shopping: várias opções para explorar.
    """
    while True:
        limpar_tela()
        print("=== MENU PRINCIPAL ===")
        print("1. Menu Tier List")
        print("2. Menu Diário")
        print("3. Armazenamento de Senhas")
        print("4. Menu de Notas")
        print("5. Menu de Cartas")
        print("6. Menu de Tarefas")
        print("7. Menu de Lembretes")
        print("8. Menu de Metas")
        print("9. Calculadora Financeira")
        print("10. Notas Rápidas")
        print("11. Sair")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "11":
            print("Saindo do programa... Até logo!")
            break
        elif opcao == "1":
            menu_tier_list()
        elif opcao == "2":
            menu_diario()
        elif opcao == "3":
            menu_armazenamento_senhas()
        elif opcao == "4":
            menu_notas()
        elif opcao == "5":
            menu_cartas()
        elif opcao == "6":
            menu_tarefas()
        elif opcao == "7":
            menu_lembretes()
        elif opcao == "8":
            menu_metas()
        elif opcao == "9":
            calculadora_financeira()
        elif opcao == "10":
            menu_notas_rapidas()
        else:
            print("Opção inválida. Tente novamente.")

def menu_cartas():
    """
    Permite o usuário sortear e ler cartas com mensagens específicas.
    É como tirar um papelzinho da sorte em uma caixa mágica.
    """
    while True:
        limpar_tela()
        print("=== MENU DE CARTAS ===")
        print("1. Sortear uma carta")
        print("2. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "2":
            break
        elif opcao == "1":
            carta = random.randint(1, 5)  # Sorteia um número de 1 a 5
            print(f"Você tirou a carta de número {carta}.")

            # Interpretação da carta
            if carta == 1:
                print("Carta 1: Aspecto masculino - lição atual.")
            elif carta == 2:
                print("Carta 2: Aspecto feminino - lição atual.")
            elif carta == 3:
                print("Carta 3: Desafio do aspecto masculino.")
            elif carta == 4:
                print("Carta 4: Desafio do aspecto feminino.")
            elif carta == 5:
                print("Carta 5: Assistência dos ancestrais.")
            input("\nPressione Enter para voltar.")
        else:
            print("Opção inválida. Tente novamente.")

def menu_notas():
    """
    Gerencia as notas dos alunos.
    É como o boletim de uma escola: você registra e consulta as notas.
    """
    global notas
    while True:
        limpar_tela()
        print("=== MENU DE NOTAS ===")
        print("1. Adicionar uma nota")
        print("2. Visualizar notas")
        print("3. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "3":
            break
        elif opcao == "1":  # Adicionar uma nova nota
            aluno = obter_input("Digite o nome do aluno: ")
            try:
                nota = float(obter_input(f"Digite a nota para {aluno}: "))
                notas[aluno] = nota  # Registra a nota
                print("Nota cadastrada com sucesso!")
            except ValueError:  # Valida entradas numéricas
                print("Por favor, insira um valor numérico.")
        elif opcao == "2":  # Exibir notas cadastradas
            if notas:
                print("=== NOTAS CADASTRADAS ===")
                for aluno, nota in notas.items():
                    print(f"{aluno}: {nota}")
            else:
                print("Nenhuma nota cadastrada.")
            input("\nPressione Enter para voltar.")
        else:
            print("Opção inválida. Tente novamente.")

def obter_input(mensagem):
    """
    Obtém entrada do usuário e verifica comandos especiais como "/sair".
    É como um atendente que ouve o pedido e direciona você.
    """
    entrada = input(mensagem).strip()
    if entrada == "/sair":
        print("Saindo do programa... Até logo!")
        exit()
    return entrada

def menu_tarefas():
    """
    Gerencia uma lista de tarefas com prioridades.
    Permite adicionar, remover e marcar tarefas como concluídas.
    """
    while True:
        limpar_tela()
        print("=== MENU DE TAREFAS ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "5":
            break
        elif opcao == "1":
            titulo = obter_input("Digite o título da tarefa: ")
            prioridade = obter_input("Digite a prioridade (Alta/Média/Baixa): ")
            tarefas.append({"titulo": titulo, "prioridade": prioridade, "concluida": False})
            print("Tarefa adicionada com sucesso!")
        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    status = "✓" if tarefa["concluida"] else " "
                    print(f"{i}. [{status}] {tarefa['titulo']} (Prioridade: {tarefa['prioridade']})")
        elif opcao == "3":
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    status = "✓" if tarefa["concluida"] else " "
                    print(f"{i}. [{status}] {tarefa['titulo']}")
                num = int(obter_input("Digite o número da tarefa a ser marcada como concluída: "))
                if 1 <= num <= len(tarefas):
                    tarefas[num-1]["concluida"] = True
                    print("Tarefa marcada como concluída!")
        elif opcao == "4":
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa['titulo']}")
                num = int(obter_input("Digite o número da tarefa a ser removida: "))
                if 1 <= num <= len(tarefas):
                    del tarefas[num-1]
                    print("Tarefa removida com sucesso!")
        input("\nPressione Enter para continuar...")

def menu_lembretes():
    """
    Gerencia lembretes com data e hora.
    """
    while True:
        limpar_tela()
        print("=== MENU DE LEMBRETES ===")
        print("1. Adicionar Lembrete")
        print("2. Listar Lembretes")
        print("3. Remover Lembrete")
        print("4. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "4":
            break
        elif opcao == "1":
            titulo = obter_input("Digite o título do lembrete: ")
            data = obter_input("Digite a data (DD/MM/AAAA): ")
            hora = obter_input("Digite a hora (HH:MM): ")
            lembretes.append({"titulo": titulo, "data": data, "hora": hora})
            print("Lembrete adicionado com sucesso!")
        elif opcao == "2":
            if not lembretes:
                print("Nenhum lembrete cadastrado.")
            else:
                for i, lembrete in enumerate(lembretes, 1):
                    print(f"{i}. {lembrete['titulo']} - {lembrete['data']} às {lembrete['hora']}")
        elif opcao == "3":
            if not lembretes:
                print("Nenhum lembrete cadastrado.")
            else:
                for i, lembrete in enumerate(lembretes, 1):
                    print(f"{i}. {lembrete['titulo']}")
                num = int(obter_input("Digite o número do lembrete a ser removido: "))
                if 1 <= num <= len(lembretes):
                    del lembretes[num-1]
                    print("Lembrete removido com sucesso!")
        input("\nPressione Enter para continuar...")

def menu_metas():
    """
    Gerencia metas e objetivos com prazo e progresso.
    """
    while True:
        limpar_tela()
        print("=== MENU DE METAS ===")
        print("1. Adicionar Meta")
        print("2. Listar Metas")
        print("3. Atualizar Progresso")
        print("4. Remover Meta")
        print("5. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "5":
            break
        elif opcao == "1":
            titulo = obter_input("Digite o título da meta: ")
            prazo = obter_input("Digite o prazo (DD/MM/AAAA): ")
            metas.append({"titulo": titulo, "prazo": prazo, "progresso": 0})
            print("Meta adicionada com sucesso!")
        elif opcao == "2":
            if not metas:
                print("Nenhuma meta cadastrada.")
            else:
                for i, meta in enumerate(metas, 1):
                    print(f"{i}. {meta['titulo']} - Prazo: {meta['prazo']} - Progresso: {meta['progresso']}%")
        elif opcao == "3":
            if not metas:
                print("Nenhuma meta cadastrada.")
            else:
                for i, meta in enumerate(metas, 1):
                    print(f"{i}. {meta['titulo']} - Progresso atual: {meta['progresso']}%")
                num = int(obter_input("Digite o número da meta a ser atualizada: "))
                if 1 <= num <= len(metas):
                    novo_progresso = int(obter_input("Digite o novo progresso (0-100): "))
                    if 0 <= novo_progresso <= 100:
                        metas[num-1]["progresso"] = novo_progresso
                        print("Progresso atualizado com sucesso!")
        elif opcao == "4":
            if not metas:
                print("Nenhuma meta cadastrada.")
            else:
                for i, meta in enumerate(metas, 1):
                    print(f"{i}. {meta['titulo']}")
                num = int(obter_input("Digite o número da meta a ser removida: "))
                if 1 <= num <= len(metas):
                    del metas[num-1]
                    print("Meta removida com sucesso!")
        input("\nPressione Enter para continuar...")

def calculadora_financeira():
    """
    Calculadora financeira com várias funcionalidades.
    """
    while True:
        limpar_tela()
        print("=== CALCULADORA FINANCEIRA ===")
        print("1. Calcular Juros Compostos")
        print("2. Calcular Parcelas")
        print("3. Calcular Retorno sobre Investimento")
        print("4. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "4":
            break
        elif opcao == "1":
            principal = float(obter_input("Digite o valor principal: "))
            taxa = float(obter_input("Digite a taxa de juros anual (%): "))
            tempo = float(obter_input("Digite o tempo em anos: "))
            montante = principal * (1 + taxa/100) ** tempo
            print(f"\nMontante final: R$ {montante:.2f}")
        elif opcao == "2":
            valor = float(obter_input("Digite o valor total: "))
            num_parcelas = int(obter_input("Digite o número de parcelas: "))
            valor_parcela = valor / num_parcelas
            print(f"\nValor de cada parcela: R$ {valor_parcela:.2f}")
        elif opcao == "3":
            investimento = float(obter_input("Digite o valor do investimento: "))
            retorno = float(obter_input("Digite o valor do retorno: "))
            roi = ((retorno - investimento) / investimento) * 100
            print(f"\nROI: {roi:.2f}%")
        input("\nPressione Enter para continuar...")

def menu_notas_rapidas():
    """
    Sistema de notas rápidas para anotações temporárias.
    """
    while True:
        limpar_tela()
        print("=== NOTAS RÁPIDAS ===")
        print("1. Adicionar Nota")
        print("2. Listar Notas")
        print("3. Remover Nota")
        print("4. Voltar ao Menu Principal")

        opcao = obter_input("Escolha uma opção: ")
        if opcao == "4":
            break
        elif opcao == "1":
            nota = obter_input("Digite sua nota: ")
            notas_rapidas.append(nota)
            print("Nota adicionada com sucesso!")
        elif opcao == "2":
            if not notas_rapidas:
                print("Nenhuma nota cadastrada.")
            else:
                for i, nota in enumerate(notas_rapidas, 1):
                    print(f"{i}. {nota}")
        elif opcao == "3":
            if not notas_rapidas:
                print("Nenhuma nota cadastrada.")
            else:
                for i, nota in enumerate(notas_rapidas, 1):
                    print(f"{i}. {nota}")
                num = int(obter_input("Digite o número da nota a ser removida: "))
                if 1 <= num <= len(notas_rapidas):
                    del notas_rapidas[num-1]
                    print("Nota removida com sucesso!")
        input("\nPressione Enter para continuar...")

# Início do programa
if __name__ == "__main__":
    iniciar_programa()
