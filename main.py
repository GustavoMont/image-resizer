import os 
from PIL import Image

try:
    os.mkdir('results')
except:
    os.system('cls')

def is_imagem(item):
    if item.endswith('jpg') or item.endswith('png'):
        return True
    return False

def reduzir_imagem(input_dir, output_dir):    
    proporcao = int(input('Quer a imagem quantas vezes menor:\nDigite aqui o valor: '))
    todos_arquivos = os.listdir(input_dir)
    for item in todos_arquivos:
        if is_imagem(item):
            imagem = Image.open(os.path.join(input_dir, item))
            tamanho = (int(imagem.size[0]/proporcao), int(imagem.size[1]/proporcao))
            nova_imagem = imagem.resize(tamanho)
            nova_imagem.save(os.path.join(output_dir, item))
    

while True:
    input_dir = input('Digite o caminho de onde estão as imagens: ')
    reduzir_imagem(input_dir, './results')
    opc = input('Deseja redimensionar mais imagens?[yes/no]\nDigite aqui: ')
    if opc.lower() == 'nao' or opc.lower() == 'no':
        print('Okay! ;)')
        break;

