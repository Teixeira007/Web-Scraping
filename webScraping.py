import requests
from bs4 import BeautifulSoup, SoupStrainer
import re
import os
import zipfile

# Constantes explícitas
BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
OUTPUT_FOLDER = 'downloads'
ZIP_FILENAME = 'arquivos_pdfs.zip'

#Função para fazer o download do arquivo recebendo a url e o nome
def download_file(pdf_url, filename):
    pdf_response = requests.get(pdf_url, stream=True)
    if pdf_response.status_code == 200:
        with open(filename, 'wb') as pdf_file:
            for chunk in pdf_response.iter_content(chunk_size=8192):
                if chunk:
                    pdf_file.write(chunk)


#Função para zipar os arquivos, recebendo o nome do arquivo zip e uma lista dos caminhos dos arquivos a serem zipados
def zip_file(zip_filename, downloaded_files):
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        for file in downloaded_files:
            zip_file.write(file, os.path.basename(file))


def main():
    #Fazendo uma requisição http do tipo get na url
    response = requests.get(BASE_URL)


    #verificar se existe a pasta downloads, senão, criar uma
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    #Lista que ficarão os nomes dos arquivos a serem baixados
    downloaded_files = []

    #Se a requisição foi um sucesso
    if response.status_code == 200:
        # Definindo o filtro para extrair apenas os links relevantes, aqueles que tem a palavra "Anexo" e são PDFs
        link_filter = SoupStrainer('a', href=re.compile(r'Anexo.*\.pdf$'))

        #Utilizando o beautifulSoup para  analisar o html com filtro 
        links_pdfs = BeautifulSoup(response.text, 'html.parser', parse_only=link_filter)
        
        for link in links_pdfs:
            pdf_url = link.get('href')

            #Extrair o nome do arquivo do url
            filename = os.path.join(OUTPUT_FOLDER, os.path.basename(pdf_url))

            #chamando função de download
            download_file(pdf_url, filename)
            
            downloaded_files.append(filename)
        #Criar um zip com os arquivos baixados
        zip_file(ZIP_FILENAME, downloaded_files)
        
    else:
        print("Erro ao acessar apágina", response.status_code)


if __name__ == '__main__':
    main()