import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
import cv2

import os
import numpy as np
import requests

images = [0]

# compara os histogramas formados a partir dos frames
def compareHistograms(position):
    hist2 = createHistogram(f"data\\image_{position}.jpg")
    for i in range(0, position):
        
        try:
            hist1 = createHistogram(f"data\\image_{i}.jpg")
            result = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)

            # caso haja muita semelhança entre os histogramas, o arquivo é excluído da pasta
            if (result <= 10.0e-03):
                os.remove(f"data\\image_{position}.jpg")
                break
        except:
            i += 1

# cria um histograma
def createHistogram(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hist = cv2.calcHist([img], [0, 1], None, [8, 8], [0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()

    return hist

# faz a leitura das imagens (cada categoria recebe um tratamento específico)
def read_image(image_file, is_url=False):
    min_conf = 10
    text = ''

    # leitura de caminho da internet
    if is_url:
        # faz um request e recebe como resposta a imagem a ser lida
        resp = requests.get(image_file, stream=True).raw
        image = np.asarray(bytearray(resp.read()),dtype="uint8")
        image = cv2.imdecode(image,cv2.IMREAD_COLOR)
    else:
        image = cv2.imread(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # dicionário de dados, que é criado a partir da imagem
    result = pt.image_to_data(image, output_type=pt.Output.DICT, lang='por')
    
    # verifica a confiança com relação ao texto lido e descarta leituras com baixa acurácia
    for i in range(0, len(result['text'])): 
        confidence = int(result['conf'][i]) 
        if confidence >= min_conf: 
            text += f'{result["text"][i]} '  

    return text  

# realiza uma leitura prévia do arquivo em formato de vídeo
def read_video(filename):
    video = cv2.VideoCapture(filename)
    success, image = video.read()
    i = 0
    success = True

    # criação dos histogramas para cada frame do vídeo
    while success:
        cv2.imwrite("data\\image_%d.jpg" % i, image)
        if (i > 0):
            compareHistograms(i)
        i += 1
        success, image = video.read() 

    texts = []
    text = ''

    # para cada arquivo com textos diferentes ocorre a adição daquele na pasta 'data'
    os.chdir('data')
    for file in os.listdir():
        if os.path.isfile(file):
            text_list = read_image(file)
            text_list = text_list.split('\n')
            for phrase in text_list:
                if phrase not in texts:
                    texts.append(phrase)
    for phrase in texts:
        text += f'{phrase}\n\n'
    
    return text
    



    