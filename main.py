import os 
from PIL import Image

try:
    os.mkdir('results')
    os.system('cls')
except:
    os.system('cls')

def is_imagem(item):
    if item.endswith('jpg') or item.endswith('png'):
        return True
    return False

def reduzir_imagem(input_dir, output_dir):
    nova_width = int(input('Quanto de largura você deseja?\nDigite aqui o número: '))
    todos_arquivos = os.listdir(input_dir)
    for item in todos_arquivos:
        if is_imagem(item):
            imagem = Image.open(os.path.join(input_dir, item))
            widhtImage, heightImage = imagem.size[0], imagem.size[1]
            nova_heigth = round(nova_width*heightImage/widhtImage)
            tamanho = ((nova_width, nova_heigth))
            imagem.thumbnail(tamanho)
            imagem.save(os.path.join(output_dir, item), optimize=True, quality=100)

while True:
    input_dir = input('Digite o caminho de onde estão as imagens: ')
    reduzir_imagem(input_dir, './results')
    opc = input('Deseja redimensionar mais imagens?[yes/no]\nDigite aqui: ')
    if not (opc.lower() == 'yes' or opc.lower() == 'sim'):
        print('Okay! ;)')
        break

