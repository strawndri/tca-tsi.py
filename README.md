<h1 align="center">Tsi.py</h1>

<p align="center">
  <img src="https://i.imgur.com/qMB7p7p.png" alt='Banner. Imagem com fundo verde com uma borda cinza escuro em seu entorno. Ao centro, há um retângulo cinza escuro com o texto: "Trabalho de Conclusão de Ano (TCA) Linguagem de Programação - 2022". Ao lado esquerdo desse retângulo, há um ícone da linguagem de programação Python, com a representação de duas cobras com sentidos verticais opostos. Ao lado direito do retângulo, há a ilustração de uma cobra verde, com a língua para fora e cor olhos amarelos. Abaixo do retângulo cinza, há um retângulo menor verde, nele está escrito "Tsi.py".' />
</p>

<p align="center">
    <img src='https://img.shields.io/badge/License-MIT-f2a2b7?style=for-the-badge&logo=appveyor' alt='Badge. Retângulo dividido em duas partes: no lado esquerdo, o retângulo possui a cor cinza, um círculo azul com vazados e o texto "LICENSE"; no lado direito, o retângulo é cor-de-rosa e contém o texto "MIT".'>
    <img src='https://img.shields.io/badge/Status-Em construção-F1E05A?style=for-the-badge&logo=appveyor' alt='Badge. Retângulo dividido em duas partes: no lado esquerdo, o retângulo possui a cor cinza, um círculo azul com vazados e o texto "STATUS"; no lado direito, o retângulo é amarelo e contém o texto "Em construção".'>
</p>


### Tópicos 

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto)

:small_blue_diamond: [Funcionalidades](#funcionalidades)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

:small_blue_diamond: [Tecnologias](#tecnologias)

---

## Descrição do projeto 

<p align="justify">
  O Tsi.py, projeto que terá como base a linguagem de programação Python, será um programa com objetivo de auxiliar pessoas no processo de leitura de imagens com texto. A finalidade, nesse sentido, é, a partir de técnicas de visão computacional e machine learning (aprendizado de máquina), melhorar a experiência do usuário quando ele se depara com imagens com conteúdo textual. Para um melhor contato, haverá a presença de uma interface gráfica, o que determina, portanto, o projeto como software GUI (Graphical User Interface). 

  O público alvo está associado, inicialmente, à questão da acessibilidade. Nesse sentido, pessoas com algum grau de deficiência — e que, portanto, não conseguem ler o que está escrito em imagens — ou que possuem certa dificuldade de leitura integram, tal pauta. Além disso, a aplicação também é útil aos estudantes que, em algum momento, desejam compartilhar o que escreveram manualmente para outras pessoas, bem como aos indivíduos que precisam lidar com textos advindos de imagens (copiar, alterar, adicionar a um projeto ou mesmo encaminhar por mensagem para alguém).
</p>

## Funcionalidades
### Acesso ao Guia
- Clicar no botão “Acessar o Guia” e ter um panorama geral de como funciona o software;
- Clicar na seta no canto superior esquerdo para retornar ao menu inicial.

### Realização de uma nova leitura
- Selecionar a opção de arquivo que se deseja efetuar a leitura, por meio de uma relação de dois botões, cujos nomes são “Imagem” e “Vídeo”;
- Trazer o arquivo a ser lido ao programa por meio do botão “Upload”;
- Trazer o arquivo a ser lido ao programa através de um campo para inserção de um link;
- Efetuar a leitura da imagem ao clicar no botão “Realizar leitura”;
- Verificar a imagem ou o vídeo que foi trazido através do visor, localizado no lado direito da tela;
- Realizar leitura do texto extraído;
- Copiar o texto para a área de transferência através do botão de nome “Copiar texto”;
- Fazer download do texto em formato .pdf e recebê-lo na página de Downloads do computador, a partir do botão “Download”;
- Clicar na seta no canto superior esquerdo para retornar ao menu inicial.

## Como rodar a aplicação :arrow_forward:

### Clonando o repositório remoto
Em seu terminal, digite o seguinte trecho de código:
```
git clone https://github.com/strawndri/tca-tsi.py.git
```

### Baixando a versão mais atual do projeto
1. Clique na última versão presente em "release";
2. Clique na primeira opção, que diz "Source code (zip)";
3. Extraia o arquivo compactado.

### Download do pytesseract
Para o funcionamento do programa, você precisará fazer o download do Pytesseract em sua máquina. 
- [Repositório do Pytesseract para download](https://github.com/tesseract-ocr/tesseract/wiki/Downloads)

Depois disso, você precisará executar em seu terminal os seguintes comandos:
```
pip install kivy
pip install fpdf
pip install pathlib
pip install opencv-python
pip install pytesseract
pip install requests
```

## Tecnologias
- [X] [Kivy](https://kivy.org/)
- [X] [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [X] [FPDF](https://pypi.org/project/fpdf/)
- [X] [PathLib](https://docs.python.org/3/library/pathlib.html)
- [X] [OpenCV-Python](https://pypi.org/project/opencv-python/)
- [X] [PyTesseract](https://pypi.org/project/pytesseract/)
- [X] [NumPy](https://numpy.org/doc/stable/)
- [X] [Requests](https://pypi.org/project/requests/)

## Feito com carinho por

| [<img src="https://avatars.githubusercontent.com/u/62841828?v=4" width=115><br><sub>Andrieli Luci Gonçalves</sub>](https://github.com/strawndri) |
| :---: |

## Licença 
MIT License - Copyright :copyright: 2022 - Andrieli
