import requests
from bs4 import BeautifulSoup
import re
import os
import zipfile

#Função para fazer o download do arquivo recebendo a url e o nome
def download_file(pdf_url, filename):
    pdf_response = requests.get(pdf_url)
    if pdf_response.status_code == 200:
        with open(filename, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)


#Função para zipar os arquivos, recebendo o nome do arquivo zip e uma lista dos caminhos dos arquivos a serem zipados
def zip_file(zip_filename, downloaded_files):
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        for file in downloaded_files:
            zip_file.write(file, os.path.basename(file))

#Url que desejo fazer o web scraping
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

#Fazendo uma requisição http do tipo get na url
response = requests.get(url)

output_folder = 'downloands'

#verificar se existe a pasta downloads, senão, criar uma
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Lista que ficarão os nomes dos arquivos a serem baixados
downloaded_files = []

#Se a requisição foi um sucesso
if response.status_code == 200:
    #utilizando o beautifulSoup para  analisar o html da página
    soup = BeautifulSoup(response.text, 'html.parser')

    #Extraindo links de PDF que contém a palavra "anexo"
    links_pdfs = soup.find_all('a', href=re.compile(r'Anexo.*\.pdf$'))


    for link in links_pdfs:
        pdf_url = link.get('href')

        #Extrair o nome do arquivo do url
        filename = os.path.join(output_folder, os.path.basename(pdf_url))

        #chamando função de download
        download_file(pdf_url, filename)
        
        downloaded_files.append(filename)
    #Criar um zip com os arquivos baixados
    zip_filename = 'arquivos_pdfs.zip'
    zip_file(zip_filename, downloaded_files)
    
else:
    print("Erro ao acessar apágina", response.status_code)