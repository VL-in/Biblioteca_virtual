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
    diretorio = input(r'Forneça o diretório em que deseja listar os documentos: ')
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

#Adicionar documento no diretório (duas formas)
def adicionar_doc_na_lista():
    '''Esta função define uma das formas de adicionar arquivo à lista Biblioteca_virtual global: incluindo chave-valor via input.'''
    #Chamando o dicionário global para dentro da função
    global Biblioteca_virtual
    resposta = 's'
    #Permite adicionar mais de um título (chave-valor) no mesmo loop.
    while resposta == 's':
        print("Digite as informações solicitadas.")
        titulo_doc = (input(f'Digite o título do documento: '))
        data_publicacao = (input(f'Digite o ano de publicação do documento: '))
        tipo_arq = (input('Digite o formato do documento (pdf/epub/doc/docx/txt) em letra minúscula: '))
        #Adicionando o chave-valor obtido via input ao biblioteca global
        (Biblioteca_virtual).update({
            titulo_doc:{
            'data_publicacao': data_publicacao,
            'tipo': ('.'+ tipo_arq)
        }})
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
    
#def adicionar_doc_via_dir():
    '''Esta função permite adicionar um documento à dicionário "Biblioteca_virtual" global através do diretório'''
    

        
    
#Renomear documento do diretório

#Remover documento do diretório

#Renomear documento na lista biblioteca

#Remover documento da lista biblioteca





#Código principal
#Aqui encontra-se a interface de interação com o usuário
#diretorio_desejado = input(r'Digite o diretório da biblioteca em que deseja trabalhar: ')
#adicionar_doc_na_lista(Biblioteca_virtual)

listar_doc_dir_org()


