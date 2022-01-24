import os

pasta = str(input('Copie e cole aqui o caminho da pasta que deseja organizar:'))
os.chdir(pasta)
extens = []
pastas = []
for c in os.listdir():
    if os.path.isdir(pasta + '\\' + c):
        pastas.append(c)
for c in os.listdir():
    if os.path.isfile(pasta + '\\' + c):
        name = c.split('.')
        ext = name[-1].lower()
        if ext not in extens:
            extens.append(ext)
            nomepasta = 'Arquivos ' + ext
            if nomepasta not in pastas:
                pastas.append(nomepasta)
                os.mkdir(os.path.join(pasta, nomepasta))
        os.rename(c, pasta + '\\' + 'Arquivos ' + ext + '\\' + c)
#    os.rename(c, pastapara +'\\' + c)
