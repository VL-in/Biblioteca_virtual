#Este código permite a organização e visualização dos documentos eletrônicos de uma biblioteca.

#Importando bibliotecas
import os
import shutil

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
        'tipo': 'ePUB'
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

#Listar documentos
def listar_doc_dir(diretorio):
    '''Este código lista todos os documentos eletrônicos disponíveis no diretório da biblioteca de forma organizado.'''
    #Mensagem de inicialização de organização de arquivos
    print(f"Listando os documentos do diretório solicitado...")

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
    for arquivo in os.listdir(diretorio):
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
    
    #printando o diretório da biblioteca
    for chave, valor in biblioteca.items():
        if chave !=  'diverso':
            print(f"Os arquivos em formato {chave} são: {valor}")
        else:
            print(f"Os arquivos em outros tipos de formato neste diretório são: {valor}.")
    return biblioteca

#Adicionar documento no diretório

#Renomear documento do diretório

#Remover documento do diretório

#Adicionar documento na lista biblioteca

#Renomear documento na lista biblioteca

#Remover documento da lista biblioteca





#Código principal
#Aqui encontra-se a interface de interação com o usuário
diretorio_desejado = input(r'Digite o diretório da biblioteca em que deseja trabalhar: ')
listar_doc_dir(diretorio_desejado)


