import os

#listas auxiliares
extens = []
pastas = []

#Direciona o caminho da pasta
pasta = str(input('Copie e cole aqui o caminho da pasta que deseja organizar:'))
os.chdir(pasta)

#Lista todas as pastas na lista 'pastas'
for c in os.listdir():
    if os.path.isdir(pasta + '\\' + c):
        pastas.append(c)

#Cria a pasta se ela ainda não foi criada e coloca o arquivos dentro
for c in os.listdir():
    if os.path.isfile(pasta + '\\' + c):
        name = c.split('.')
        ext = name[-1].lower()
        if ext not in extens: #Verifica se a extensão ja foi listada
            extens.append(ext)
            nomepasta = 'Arquivos ' + ext
            if nomepasta not in pastas: #Verifica a existencia da pasta
                pastas.append(nomepasta)
                os.mkdir(os.path.join(pasta, nomepasta)) #Cria a pasta
        
        os.rename(c, pasta + '\\' + 'Arquivos ' + ext + '\\' + c) #Move o arquivo de acordo com a extensão
