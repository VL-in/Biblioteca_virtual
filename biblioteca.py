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

#Listando a biblioteca virtual (OK)
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
    elif ordernar_por == '2':
        for titulo, valor in sorted(Biblioteca_virtual.items(), key=lambda item: item[1]['data_publicacao']):
            print(titulo,valor)
    elif ordernar_por == '3':
        for titulo, valor in sorted(Biblioteca_virtual.items(), key=lambda item: item[1]['tipo']):
            print(titulo,valor)
    else:
        print('Entrada invalida.')

    
# listar documentos do diretorio (OK)
def listar_dir():
    ''' Esta função lista somente os documentos do diretório fornecido pelo usuário e ignora as pastas dentro do diretório.
        Ela retorna uma lista com os arquivos existentes no diretório.'''
    #Pedindo para o usuário passar o diretório via teclado
    diretorio = input(r'Forneça a pasta que contém os arquivos: ')
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


#Ordernar documentos (OK)
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

    #organizando as listas
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
            print(f'Os documentos no formato de {chave} são: ')   
            for titulo in valor:
                print(f'{titulo}')         
        elif chave == 'diverso':
            print(f"Os arquivos em outros tipos de formato neste diretório são: ")
            for titulo in valor:
                print(f'{titulo}')  
    return biblioteca

#Definir chave-valor da Biblioteca_virtual via input:
def titulo_biblioteca_input():
    #Trazendo a biblioteca virtual
    global Biblioteca_virtual
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
        print("Digite as informações solicitadas.")
        titulo_biblioteca_input()
        resposta = input('Deseja inserir mais um título? (s/n): ')  #define se o loop continua
        if resposta == 'n':
            visualizar = input('Deseja visualizar a lista atualizada? (s/n): ') #Pergunta se o usuário quer visualizar a lista atualizada
            if visualizar == 's':
                for titulo, valor in sorted(Biblioteca_virtual.items()):
                    print(titulo, valor)
            elif visualizar == 'n':
                None
            else:
                print("Resposta invalida.")   
            print(f"A adição do(s) título(s) na lista da biblioteca foi concluída") 
            break #Finaliza o loop
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
            titulo_biblioteca_dir(arquivo)
        else:
            print('Ocorreu um erro.')
            break
    visualizar = input(f'Gostaria de visualizar a biblioteca virtual atualizada? (s/n): ')
    if visualizar == 's':
        for titulo, valor in sorted(Biblioteca_virtual.items()):
            print(titulo, valor)
    elif visualizar == 'n':
        None
    else:
        print("Resposta invalida. Finalizando a adição dos documentos.")

    return Biblioteca_virtual

#Renomear documento do diretório
def renomear_doc_dir():
    '''Este código permite o usuário renomear um documento do diretório.'''
    arq_renomear = (input(r'Digite o diretório a ser renomeado: '))
    novo_nome = (input(r'Digite o novo nome do arquivo: '))
    os.rename(arq_renomear, novo_nome)
    print(f'O arquivo {arq_renomear} foi renomeado com sucesso para {novo_nome}.')

#Remover documento do diretório
def remover_doc_dir():
    '''Este código permite o usuário remover um documento do diretório.'''
    arquivo_del = (input(r'Digite o diretório a ser removido: '))
    if os.path.exists(arquivo_del): #Se o arquivo existir, será deletado.
        os.remove(arquivo_del)
        print(f'O arquivo {arquivo_del} foi removido da pasta.')
    else:
        print(f'O diretório indicado não existe')

#Renomear documento na lista biblioteca
def renomear_doc_lista():
    '''Este código permite o usuário renomear um título da biblioteca_virtual e retorna a biblioteca atualizada.'''
    global Biblioteca_virtual
    titulo_existente = (input(r'Digite o título a ser renomeado: '))
    novo_nome = (input(r'Digite um novo nome: '))
    if titulo_existente in Biblioteca_virtual:
        Biblioteca_virtual[novo_nome] = Biblioteca_virtual.pop(titulo_existente)
        print(f'O título {titulo_existente} foi renomeado para {novo_nome}.')
    else:
        print(f'O título inserido {titulo_existente} não consta na lista da biblioteca.')
    return Biblioteca_virtual

#Remover documento da lista biblioteca
def remover_doc_lista():
    '''Este código permite o usuário remover um título da biblioteca_virtual e retorna a biblioteca atualizado.'''
    global Biblioteca_virtual
    titulo_existente = (input(r'Digite o título a ser removido: '))
    if titulo_existente in Biblioteca_virtual:
        Biblioteca_virtual.pop(titulo_existente)
        print(f'O título {titulo_existente} foi removido da biblioteca.')
    else:
        print(f'O título inserido {titulo_existente} não consta na lista da biblioteca.')
    return Biblioteca_virtual

#Definindo função para voltar ao menu principal
def voltar_menu_principal(menu):
    '''Esta função permite que usuário voltar para o menu principal.'''
    menu_continuar = input('Gostaria de voltar para o menu principal? (s/n): ')
    if menu_continuar == 's':
        menu = True
    elif menu_continuar == 'n':
        menu = False

#Definindo a interface do usuário
def interface_biblioteca():
    menu = True
    while menu == True:
        print('Bem vindo à biblioteca virtual!')
        print('Escolha uma das seguintes opções para continuar')
        print(' Se deseja visualizar arquivos presentes dentro de uma pasta, digite "1"')
        print(' Se deseja visualizar a biblioteca atual, digite "2"')
        print(' Se deseja adicionar um novo documento à biblioteca, digite "3"')
        print(' Se deseja renomear um documento existente, digite "4"')
        print(' Se deseja remover um documento existente, digite "5"')
        print(' Se deseja sair, digite "6"')
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            listar_doc_dir_org()
            voltar_menu_principal(menu)

        elif opcao == '2':
            print(f'Os documentos na biblioteca são: ')
            for titulo, valor in sorted(Biblioteca_virtual.items()):
                print(titulo, valor)
            voltar_menu_principal(menu)
            
        elif opcao == '3':
            print('Gostaria de adicionar um novo documento de qual forma?')
            print('  Via diretório, digite "1"')
            print('  Via teclado, digite "2"')
            opcao_adicionar = input('Digite a opção desejada: ')
            if opcao_adicionar == '1':
                adicionar_doc_via_dir()
            elif opcao_adicionar == '2':
                adicionar_doc_na_lista()
            else:
                print('Opção inválida. Tente novamente.')
            voltar_menu_principal(menu)
        elif opcao == '4':
            print('Como gostaria de renomear um documento?')
            print('  Documento existente no diretório, digite "1"')
            print('  Documento existente na biblioteca, digite "2"')
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
            print('  Documento existente no diretório, digite "1"')
            print('  Título existente na biblioteca, digite "2"')
            opcao_remover = input('Digite a opção desejada: ')
            if opcao_remover == '1':
                remover_doc_dir()
            elif opcao_remover == '2':
                remover_doc_lista()
            else:
                print('Opção inválida. Tente novamente.')
            voltar_menu_principal(menu)

        elif opcao == '6':
            print('Obrigado por usar a biblioteca virtual!')
            menu == False
            break
    else:
        print('Opção inválida. Tente novamente.')
        voltar_menu_principal(menu)
    return Biblioteca_virtual



#Código principal
#Aqui encontra-se a interface de interação com o usuário
interface_biblioteca()


