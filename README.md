# Web Scraping, Download de Arquivos PDF e Zipagem de Arquivos

Este script Python foi desenvolvido para realizar web scraping em uma página específica do site do governo brasileiro (www.gov.br/ans). Ele extrai links de arquivos PDF que contêm a palavra "Anexo" em sua URL, faz o download desses arquivos e os compacta em um arquivo ZIP. Abaixo estão detalhes sobre o funcionamento e estrutura do código.

## Requisitos

Python 3.x
Bibliotecas Python: requests, beautifulsoup4
Você pode instalar as bibliotecas necessárias utilizando o seguinte comando:

```bash
pip install requests beautifulsoup4
```

## Como Usar
1. Clone o repositório ou faça o download do script Python.
 ```git
git clone https://github.com/Teixeira007/Web-Scraping.git
```
2. Certifique-se de que o Python e as bibliotecas mencionadas estão instalados.
3. Execute o script Python.

O script realizará o web scraping na URL fornecida, fará o download dos arquivos PDF e os comprimirá em um arquivo ZIP chamado arquivos_pdfs.zip.

```bash
python webScraping.py
```
## Personalização
Se desejar alterar a URL da página alvo, atualize a variável url no início do script.

Modifique o nome do diretório de saída ajustando a variável output_folder.

Personalize a expressão regular em re.compile(r'Anexo.*\.pdf$') conforme necessário, dependendo da estrutura dos links na página.

## Estrutura do Código
### Bibliotecas Utilizadas
```python
import requests
from bs4 import BeautifulSoup
import re
import os
import zipfile
```
### Função para download do arquivo
```python
def download_file(pdf_url, filename):
    # ... código para fazer o download do arquivo ...
```
Esta função recebe a URL do arquivo PDF e o nome do arquivo desejado. Realiza uma requisição HTTP GET para a URL, verifica se a resposta foi bem-sucedida (status code 200) e salva o conteúdo do arquivo no diretório especificado.
### Função para Compactar Arquivos em ZIP
```python
def zip_file(zip_filename, downloaded_files):
    # ... código para criar um arquivo ZIP ...
```
Esta função recebe o nome do arquivo ZIP desejado e uma lista de caminhos dos arquivos a serem compactados. Utiliza a biblioteca zipfile para criar um arquivo ZIP contendo os arquivos fornecidos.

### Main Code
O código principal realiza as seguintes etapas:
1. Faz uma requisição HTTP GET na URL fornecida.
2. Verifica se a pasta de saída downloads existe. Se não existir, cria-a.
3. Utiliza o BeautifulSoup para analisar o HTML da página.
4. Extrai links de PDF que contenham a palavra "Anexo" em sua URL.
5. Para cada link, extrai o nome do arquivo do URL, realiza o download e armazena o caminho do arquivo na lista downloaded_files.
6. Cria um arquivo ZIP (arquivos_pdfs.zip) contendo os arquivos baixados.

Se a execução for bem-sucedida, os arquivos PDF serão baixados para a pasta downloads e posteriormente compactados no arquivo arquivos_pdfs.zip. Em caso de erro na requisição HTTP, uma mensagem correspondente será exibida.
