# 👁️ | Tsi.py

![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-f5b5ca.svg)
![Status](https://img.shields.io/badge/Status-Concluído-abf285.svg)

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Aprendizagens](#aprendizagens)
- [Como acessar o projeto?](#como-acessar-o-projeto)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Licença](#licença)

## Sobre o projeto

O Tsi.py, projeto que terá como base a linguagem de programação Python, será um programa com objetivo de auxiliar pessoas no processo de leitura de imagens com texto. A finalidade, nesse sentido, é, a partir de técnicas de visão computacional e machine learning (aprendizado de máquina), melhorar a experiência do usuário quando ele se depara com imagens com conteúdo textual. Para um melhor contato, haverá a presença de uma interface gráfica, o que determina, portanto, o projeto como software GUI (Graphical User Interface). 

O público alvo está associado, inicialmente, à questão da acessibilidade. Nesse sentido, pessoas com algum grau de deficiência — e que, portanto, não conseguem ler o que está escrito em imagens — ou que possuem certa dificuldade de leitura integram, tal pauta. Além disso, a aplicação também é útil aos estudantes que, em algum momento, desejam compartilhar o que escreveram manualmente para outras pessoas, bem como aos indivíduos que precisam lidar com textos advindos de imagens (copiar, alterar, adicionar a um projeto ou mesmo encaminhar por mensagem para alguém).

**As funcionalidades do projeto são:**
- _Acesso ao Guia_
  - Clicar no botão "Acessar o Guia e ter um panorama geral de como funciona o software;
  - Clicar na seta no canto superior esquerdo para retornar ao menu inicial.

- _Realização de uma nova leitura_
  - Selecionar a opção de arquivo que se deseja efetuar a leitura, por meio de uma relação de dois botões, cujos nomes são "Imagem" e "Vídeo";
  - Trazer o arquivo a ser lido ao programa por meio do botão "Upload";
  - Trazer o arquivo a ser lido ao programa através de um campo para inserção de um link;
  - Efetuar a leitura da imagem ao clicar no botão "Realizar leitura";
  - Verificar a imagem ou o vídeo que foi trazido através do visor, localizado no lado direito da tela;
  - Realizar leitura do texto extraído;
  - Copiar o texto para a área de transferência através do botão de nome "Copiar texto";
  - Fazer download do texto em formato .pdf e recebê-lo na página de Downloads do computador, a partir do botão "Download";
  - Clicar na seta no canto superior esquerdo para retornar ao menu inicial.

## Aprendizagens
- Criação de interfaces gráficas tendo como base a linguagem de programação Python;
- Algortitmos de reconhecimento de caracteres;
- Funções e classes;
- Como lidar com ambientes virtuais.

## Como acessar o projeto?

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

## Tecnologias utilizadas
- [Python](https://docs.python.org/3/): Linguagem de programação;
- [Kivy](https://kivy.org/): Framework Python de desenvolvimento de aplicativos multiplataforma com interfaces gráficas;
- [FPDF](https://pypi.org/project/fpdf/): Biblioteca de geração de arquivos PDF;
- [PathLib](https://docs.python.org/3/library/pathlib.html): Módulo de manipulação de caminhos de arquivo e diretório;
- [OpenCV-Python](https://pypi.org/project/opencv-python/): Biblioteca de processamento de imagens e visão computacional;
- [PyTesseract](https://pypi.org/project/pytesseract/): Biblioteca de reconhecimento óptico de caracteres (OCR);
- [NumPy](https://numpy.org/doc/stable/): Biblioteca de manipulação de arrays multidimensionais e cálculos numéricos;
- [Requests](https://pypi.org/project/requests/): Biblioteca de realizar requisições HTTP de forma simples e intuitiva.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Consulte o arquivo `LICENSE` para obter mais informações sobre os termos de licenciamento.

---

✨ Feito com carinho por [Andrieli Gonçalves](https://github.com/strawndri).
