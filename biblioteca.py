#Este código permite a organização e visualização dos documentos eletrônicos de uma biblioteca.

#Importando bibliotecas
import os
import shutil
import os.path

#Criando a biblioteca com os títulos e informações
Biblioteca_virtual = {
    'A dama das camélias': {
        'data_publicacao': 1848,
        'tipo': '.pdf'
    },
    'Poucas ideias':{
        'data_publicacao': 2025,
        'tipo': '.pdf'
    },
    'TCC - A TAQ polimerase da espécie Mus musculus': {
        'data_publicacao': 2020,
        'tipo': '.docx'
    },
    'Iniciando em bioinformática': {
        'data_publicacao': 2019,
        'tipo': '.ePUB'
    },
    'Dataset - Relatório epidemiológico de dengue em 2024':{
        'data_publicacao': 2025,
        'tipo': '.xlsx'
    },
    'Porão da casa 209':{
        'data_publicacao': 2002,
        'tipo': '.pdf'
    },
    'O Perfume':{
        'data_publicacao': 1992,
        'tipo': '.pdf'
    }
}


#Definindo funções

#Listando a biblioteca virtual 
#Solicitando o tipo de ordenação
def ordernar_lista_biblioteca():
    '''Ordena o dicionário "Biblioteca_virtual" por 3 formas: por título (1), por data de publicação (2) e por tipo de documento (3). 
    Esta função não altera o dicionário global.'''
    #Trazendo o dicionário existente para dentro da função
    global Biblioteca_virtual
    #Solicita o usuário escolher a forma como quer ordernar a lista
    ordernar_por = input(f'Digite "1" para ordernar por título. \nDigite "2" para ordernar por data de publicação\nDigite "3" para ordernar por tipo de arquivo.\nDigite a opção desejada: ')
    if ordernar_por == '1':
        for titulo, valor in sorted(Biblioteca_virtual.items()):
            print(titulo, valor)
        print("-" * 15)
    elif ordernar_por == '2':
        for titulo, valor in sorted(Biblioteca_virtual.items(), key=lambda item: item[1]['data_publicacao']):
            print(titulo,valor)
        print("-" * 15)
    elif ordernar_por == '3':
        for titulo, valor in sorted(Biblioteca_virtual.items(), key=lambda item: item[1]['tipo']):
            print(titulo,valor)
        print("-" * 15)
    else:
        print('Entrada invalida.')

    
# listar documentos do diretorio
def listar_dir():
    ''' Esta função lista somente os documentos do diretório fornecido pelo usuário e ignora as pastas dentro do diretório.
        Ela retorna uma lista com os arquivos existentes no diretório.'''
    #Pedindo para o usuário passar o diretório via teclado
    diretorio = input(r'Forneça a pasta que contém os arquivos: ')
    print('\n')
    acao_listar = True
    #Verifica se o caminho existe. Caso não exista, a ação de listar não ocorrerá.
    if os.path.exists(diretorio):
        None
    else:
        acao_listar = False
    if acao_listar == True:
        lista_diretorio = os.listdir(diretorio)
        lista_arq = []
        for arquivo in lista_diretorio:
            caminho_arq = os.path.join(diretorio, arquivo)
            if os.path.isdir(caminho_arq):
                None
            else:
                lista_arq.append(arquivo)
        return lista_arq
    else:
        print("O diretório fornecido não existe. Verifique e tente novamente.")


#Ordernar documentos
def listar_doc_dir_org():
    ''' Esta função lista todos os documentos eletrônicos disponíveis no diretório da biblioteca e separa pelo tipo de arquivo de forma ordenada.
        A função "listar_dir" é chamada para fornecer a lista do diretório para a função atual.
        A função retorna um dicionário contendo listas de diferentes formato de documento.'''
    
    #Mensagem de inicialização de organização de arquivos
    print(f"Iniciando o processo de ordernação...")

    #Criando listas separando por tipo de arquivo
    biblioteca = {
        'pdf': [], 
        'ePUB': [], 
        'docx': [], 
        'doc': [], 
        'txt': [], 
        'xlsx': [], 
        'xls': [], 
        'pptx': [], 
        'ppt': [], 
        'csv': [], 
        'xml': [], 
        'html': [], 
        'htm': [], 
        'diverso': []
    }
    #Listando documentos e adicionando em respectivas listas
    for arquivo in listar_dir():
        if arquivo.endswith('.pdf'):
            biblioteca['pdf'].append(arquivo)
        elif arquivo.endswith('.epub'):
            biblioteca['ePUB'].append(arquivo)
        elif arquivo.endswith('.docx'):
            biblioteca['docx'].append(arquivo)
        elif arquivo.endswith('.doc'):
            biblioteca['doc'].append(arquivo)
        elif arquivo.endswith('.txt'):
            biblioteca['txt'].append(arquivo)
        elif arquivo.endswith('.xlsx'):
            biblioteca['xlsx'].append(arquivo)
        elif arquivo.endswith('.xls'):
            biblioteca['xls'].append(arquivo)
        elif arquivo.endswith('.pptx'):
            biblioteca['pptx'].append(arquivo)
        elif arquivo.endswith('.ppt'):
            biblioteca['ppt'].append(arquivo)
        elif arquivo.endswith('.csv'):
            biblioteca['csv'].append(arquivo)
        elif arquivo.endswith('.xml'):
            biblioteca['xml'].append(arquivo)
        elif arquivo.endswith('html'):
            biblioteca['html'].append(arquivo)
        elif arquivo.endswith('htm'):
            biblioteca['htm'].append(arquivo)
        else:
            biblioteca['diverso'].append(arquivo)

    #organizando as listas por tipo
    biblioteca['pdf'].sort()
    biblioteca['ePUB'].sort()
    biblioteca['docx'].sort()
    biblioteca['doc'].sort()
    biblioteca['txt'].sort()
    biblioteca['xlsx'].sort()
    biblioteca['xls'].sort()
    biblioteca['pptx'].sort()
    biblioteca['ppt'].sort()
    biblioteca['csv'].sort()
    biblioteca['xml'].sort()
    biblioteca['html'].sort()
    biblioteca['htm'].sort()
    biblioteca['diverso'].sort()
    
    #printando o diretório com os arquivos separados por tipo, ignorando as listas com valores de arquivo vazia.
    for chave, valor in biblioteca.items():
        if not valor: #Listas vazias não são printadas.
            continue
        elif chave !=  'diverso':
            print('\n')
            print(f'Os documentos no formato de {chave} são: ')   
            print('\n')
            for titulo in valor:
                print(f'    {titulo}')         
        elif chave == 'diverso':
            print('\n')
            print(f"Os arquivos em outros tipos de formato neste diretório são: ")
            print('\n')
            for titulo in valor:
                print(f'    {titulo}')  
    return biblioteca

#Definir chave-valor da Biblioteca_virtual via input:
def titulo_biblioteca_input():
    ''' Esta função geralmente será usada em outras funções, uma vez que ela só tem a finalidade de definir as variáveis de titulo, data e tipo de documento
        inserido via input.'''
    #Trazendo a biblioteca virtual
    global Biblioteca_virtual
    #Solicitando entrada de informações via teclado
    titulo_doc = (input(f'Digite o título do documento: '))
    data_publicacao = (input(f'Digite o ano de publicação do documento: '))
    tipo_arq = (input('Digite o formato do documento (pdf/epub/doc/docx/txt) em letra minúscula: '))
    #Adicionando o chave-valor obtido via input ao biblioteca global
    (Biblioteca_virtual).update({
        titulo_doc:{
        'data_publicacao': data_publicacao,
        'tipo': ('.'+ tipo_arq)
    }})

#Definir as informações do título encontrado no diretório via input
def titulo_biblioteca_dir(arquivo):
    '''Esta função possibilita o usuário adicionar múltiplos títulos de arquivos existentes em uma pasta fornecida via teclado.
       As informações de data de publicação e tipo de arquivo é fornecido via teclado.'''
    #Trazendo a biblioteca virtual
    global Biblioteca_virtual
    titulo_doc = arquivo
    data_publicacao = (input(f'Digite o ano de publicação do documento {titulo_doc}: '))
    tipo_arq = (input(f'Digite o formato do documento {titulo_doc} (pdf/epub/doc/docx/txt/outros) em letra minúscula: '))
    #Adicionando o chave-valor obtido via input ao biblioteca global
    (Biblioteca_virtual).update({
        titulo_doc:{
        'data_publicacao': data_publicacao,
        'tipo': ('.'+ tipo_arq)
    }})
    return Biblioteca_virtual

#Adicionar documento no diretório (duas formas)
#Adiciona títulos (valor-chave) à lista via input
def adicionar_doc_na_lista():
    '''Esta função define uma das formas de adicionar arquivo à lista Biblioteca_virtual global: incluindo chave-valor via input.'''
    #Chamando o dicionário global para dentro da função
    global Biblioteca_virtual
    resposta = 's'
    #Permite adicionar mais de um título (chave-valor) no mesmo loop.
    while resposta == 's':
        print("Digite as informações solicitadas:")
        print('\n')
        titulo_biblioteca_input() #chamando a função de input de informações
        print('\n')
        resposta = input('Deseja inserir mais um título? (s/n): ')  #define se o loop continua
        print('\n')
        if resposta == 'n':
            visualizar = input('Deseja visualizar a lista atualizada? (s/n): ') #Pergunta se o usuário quer visualizar a lista atualizada
            print('\n')
            if visualizar == 's':
                for titulo, valor in sorted(Biblioteca_virtual.items()):
                    print(titulo, valor)
            elif visualizar == 'n':
                None
            else:
                print("Resposta invalida.")   
            print(f"A adição do(s) título(s) na lista da biblioteca foi concluída") 
            break #Finaliza o loop
        elif resposta == 's':
            continue
        else:
            print("Entrada invalida.")
            break #finaliza loop com a entrada incorreta.
    return Biblioteca_virtual

#Adiciona títulos ao biblioteca_virtual via diretorio
def adicionar_doc_via_dir():
    '''Esta função permite adicionar múltiplos documentos à dicionário "Biblioteca_virtual" global através do diretório'''
    #Trazendo a biblioteca global
    global Biblioteca_virtual
    #Solicita a entrada do caminho da pasta via input e lista os arquivos do diretório
    for arquivo in listar_dir():
        if arquivo in Biblioteca_virtual.keys():
            continue
        elif not arquivo in Biblioteca_virtual.keys():
            titulo_biblioteca_dir(arquivo) #chamando a função onde o usuário informa o diretório e as informações a serem adicionadas na lista
        else:
            print('Ocorreu um erro.')
            break
    print('\n')
    visualizar = input(f'Gostaria de visualizar a biblioteca virtual atualizada? (s/n): ') #Visualizar a lista atualizada
    print('\n')
    if visualizar == 's':
        for titulo, valor in sorted(Biblioteca_virtual.items()):
            print(titulo, valor)
    elif visualizar == 'n':
        None
    else:
        print('\n')
        print("Resposta invalida. Finalizando a adição dos documentos.")
        print('\n')

    return Biblioteca_virtual

#Renomear documento do diretório
def renomear_doc_dir():
    '''Este código permite o usuário renomear um documento do diretório.'''
    print('\n')
    arq_renomear = (input(r'Digite o diretório a ser renomeado, não inclua aspas: '))
    novo_nome = (input(r'Digite o novo nome do arquivo: '))
    if os.path.exists(arq_renomear): # Verifica se o caminho existe
        os.rename(arq_renomear, os.path.join(os.path.dirname(arq_renomear), novo_nome)) # Modifica o nome do arquivo dentro do diretório
        print(f'O arquivo {arq_renomear} foi renomeado com sucesso para {novo_nome}.')
    else:
        print(f'O diretório indicado não existe')

#Remover documento do diretório
def remover_doc_dir():
    '''Este código permite o usuário remover um documento do diretório.'''
    arquivo_del = (input(r'Digite o arquivo a ser removido: '))
    if os.path.exists(arquivo_del): #Se o arquivo existir, será deletado.
        os.remove(arquivo_del)
        print(f'O arquivo {arquivo_del} foi removido da pasta.')
    else:
        print(f'O diretório indicado não existe')

#Renomear documento na lista biblioteca
def renomear_doc_lista():
    '''Este código permite o usuário renomear um título da biblioteca_virtual e retorna a biblioteca atualizada.'''
    # Chamando a biblioteca global
    global Biblioteca_virtual
    print('\n')
    titulo_existente = (input(r'Digite o título presenta na lista biblioteca a ser renomeado: '))
    print('\n')
    novo_nome = (input(r'Digite um novo nome: '))
    if titulo_existente in Biblioteca_virtual: #Chaca se o título consta na lsita Biblioteca global
        Biblioteca_virtual[novo_nome] = Biblioteca_virtual.pop(titulo_existente)
        print(f'O título {titulo_existente} foi renomeado para {novo_nome}.') #Renomeia o arquivo
    else:
        print(f'O título inserido {titulo_existente} não consta na lista da biblioteca.')
    return Biblioteca_virtual

#Remover documento da lista biblioteca
def remover_doc_lista():
    '''Este código permite o usuário remover um título da biblioteca_virtual e retorna a biblioteca atualizado.'''
    #Trazendo a biblioteca global
    global Biblioteca_virtual
    titulo_existente = (input(r'Digite o título a ser removido: '))
    if titulo_existente in Biblioteca_virtual: #Se o título existe dentro da lista Biblioteca, ele será removido
        Biblioteca_virtual.pop(titulo_existente)
        print(f'O título {titulo_existente} foi removido da biblioteca.')
    else:
        print(f'O título inserido {titulo_existente} não consta na lista da biblioteca.')
    return Biblioteca_virtual

#Definindo função para voltar ao menu principal
def voltar_menu_principal(menu):
    '''Esta função permite que usuário volte para o menu principal.'''
    while True:
        print('\n')
        menu_continuar = input('Digite [1] para voltar ao menu principal: ')
        if menu_continuar == '1':
            return True
        else:
            print('Opção inválida. Por favor, digite [1] para voltar ao menu principal.')
        
        

#Definindo a interface do usuário
def interface_biblioteca():
    '''Função de interação do usuário com o programa, listando todas as funções da biblioteca.'''
    menu = True
    #O usuário usa a interface dentro do loop, ou seja, o programa sai quando o usuário deseja sair (opção 6).
    while menu == True:
        print("-" * 80)
        print('\n')
        print('Bem vindo à biblioteca virtual!')
        print('\n')
        print('Escolha uma das seguintes opções para continuar: ')
        print('\n')
        print('    [1] Visualizar arquivos presentes dentro de uma pasta')
        print('    [2] Visualizar a biblioteca atual')
        print('    [3] Adicionar um novo documento à biblioteca')
        print('    [4] Renomear uma pasta ou documento existente')
        print('    [5] Remover uma documento existente')
        print('\n')
        print('    [6] Sair')
        print('\n')
        print("-" * 80)
        print('\n')
        opcao = input('Digite a opção desejada: ')
        print('\n')

        #As funções são chamadas de acordo com a escolha do usuário
        if opcao == '1':
            listar_doc_dir_org() # Lista arquivos do diretório de forma organizado
            voltar_menu_principal(menu)

        elif opcao == '2':
            ordernar_lista_biblioteca() #Ordena a lista de acordo com a opção que o usuário escolhe
            voltar_menu_principal(menu)
            
        elif opcao == '3':
            print('Gostaria de adicionar um novo documento de qual forma?')
            print('\n')
            print('   [1] Via diretório importanto todos os arquivos para a lista biblioteca') #Adiciona o nome dos documentos como chave 'titulo' na Biblioteca
            print('   [2] Via teclado inserindo título e informações')#Adiciona chave 'titulo' e os valores 'data de publicacao' e 'tipo' via teclado
            print('\n')

            opcao_adicionar = input('Digite a opção desejada: ')
            print('\n')
            if opcao_adicionar == '1':
                adicionar_doc_via_dir()
            elif opcao_adicionar == '2':
                adicionar_doc_na_lista()
            else:
                print('Opção inválida. Tente novamente.')
            voltar_menu_principal(menu)

        elif opcao == '4':
            print('Como gostaria de renomear um documento?')
            print('\n')
            print('    [1] Documento existente no diretório') #Renomeia arquivo do diretório
            print('    [2] Documento existente na lista da biblioteca') #Renomeia título da lista biblioteca
            print('\n')
            opcao_renomear = input('Digite a opção desejada: ')
            if opcao_renomear == '1':
                renomear_doc_dir()
            elif opcao_renomear == '2':
                renomear_doc_lista()
            else:
                print('Opção inválida. Tente novamente.')
            voltar_menu_principal(menu)

        elif opcao == '5':
            print('Onde deseja remover o documento?')
            print('\n')
            print('   [1] Documento existente no diretório') #Remove o documento do diretório
            print('   [2] Título existente na biblioteca') #Remove o chave-valor da Biblioteca
            print('\n')
            opcao_remover = input('Digite a opção desejada: ')
            print('\n')
            if opcao_remover == '1':
                remover_doc_dir()
            elif opcao_remover == '2':
                remover_doc_lista()
            else:
                print('Opção inválida. Tente novamente.')
            voltar_menu_principal(menu)

        elif opcao == '6':
            print('Obrigado por usar a biblioteca virtual!') 
            menu = False
            break #Termina o loop e sai do programa

    else:
        print('Opção inválida. Tente novamente.') #Mensagem para qualquer valor que não seja de 1 a 6.
        voltar_menu_principal(menu)
    return Biblioteca_virtual



#Código principal
#Aqui inicia-se o programa - a interface de interação com o usuário
interface_biblioteca()


