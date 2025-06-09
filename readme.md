Guia de como usar Git e Github

A seguir, será apresentado uma guia de o que é e como fazer commits, pushes e pull request.



# Usando "commit"
    Para usar de forma adequada a funcionalidade de versionamento do Git, devemos sempre fazer os commits 
    (upload de modificações) através do comando "git commit". 
    
    Um arquivo no git possuem 4 estados:
        Não identificado (Untracked)
        Modificado (Modified)
        Não adicionado à stage (Unstaged)
        Pronto para commit (Staged)
    
    O arquivo não identificado é um arquivo que não foi adicionado ao git. Para alterar este estado, 
    basta usar 'git add nome_arquivo'.
    
    Um arquivo modificado é um arquivo que está no git, e sofreu alterações desde o último commit. 
    Para que estas alterações sejam salvos (commit), ele deve estar adicionado ao stage. 
    Podemos fazer isso através do comando 'git add nome_arquivo' para colocá-lo a lista de stage.
    
    Por fim, quando o arquivo está no estado Staged, ele está pronto para ser commitado, 
    através do comando 'git commit nome_arquivo'.
    
    Ao fazer commits, precisamos adicionar notas sobre o que foi modificado para fim de rastreabilidade. 
    A mensagem é adicionado usando "-m", seguido da mensagem entre aspas. 
    Veja o exemplo abaixo:

        git commit nome_do_arq_para_commit -m "Nesta mensagem deve estar descrito quais foram 
        as alterações deste commit".

    Desta forma, o commit será feito para o branch atual em que se localiza. Podemos verificar usando 
    "git branch", onde o "*" (asterisco) indica o branch atual.
    
    Para mudar de um branch para outro, basta usar "git checkout" + o nome do branch em que deseja mover para.




# Usando "push"
    O git push serve para publicar os commits feitos do seu local (no git) para o repositório do GitHub. 
    Para isso, primeiro é preciso estar com o git logado e conectado a conta do Github.
    
    A forma mais simples de verificar se está logado é digitar "git push", o Git te notificará caso não 
    esteja logado e oferece as opções de logar.
    
    Uma vez logado, ao digitar "git status", na tela mostrará quantos commits estão "defasados" em relação 
    ao branch do repositório do GitHub.
    
    Para publicar, basta digitar "git push" no prompt de comando ou "git push nome_do_repositório nome_do_branch" 
    para selecionar o repositório e branch que deseja salvar.




# Usando "pull resquest"
    O pull request permite que várias pessoas contribuam para um código de repositório compartilhado. 
    Desta forma, o código principal não é comprometido uma vez que o pull request pode ser feita em branchs diferentes.
    
    Para fazer pull request de um repositório, é necessário fazer um fork (cópia do repositório do terceiro 
    para o seu repositório). Isso faz com que você trabalhe em cima da cópia daquele repositório, sem fazer 
    alterações no original.
    
    Uma vez que você fez os seus commits e fez o push deles para o branch do seu repositório, 
    vá até o reporitório de origem do fork e selecione o menu de branch e selecione a que contém os seus commits.
    
    Em seguida, clique em "Comparação e solicitação de pull" para criar uma solicitação de pull 
    para o branch selecionado. Note que duas opções serão apresentadas:
        branch base = branch o qual você deseja mesclar as alterações
        branch de comparação = para escolher o branch do tópico onde você fez alterações
   
    Digite o título e as informações das quais descrevem os commits para pull request.
    
    Dessa forma, você acaba de criar um pull request pronto para revisão.

    ##Cuidado: tome muito cuidado ao fazer push forçado de commits para um pull request, 
    pois isto pode acabar corrompendo os commits que foram feitos por outros colaboradores nos branches do projeto.
