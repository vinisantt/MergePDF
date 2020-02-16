from PyPDF2 import PdfFileMerger
import os


def pega_arqs(*args) -> tuple:
    l = []
    for item in args:
        for p, _, files in os.walk(os.path.abspath(item)):
            for file in files:
                if file.find(".pdf") != -1:
                    l.append((p, file))
    return l


def arqs_lista(*args) -> list:
    arqs = []
    for elemento in args:
        for item in elemento:
            arqs.append(item[1])
    return arqs


def mescla(lista):
    if lista != []:
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)

        nome_arquivo = input("Digite o nome para o arquivo mesclado: ")
        merger.write(f"{nome_arquivo}.pdf")
        merger.close()
        print("Os arquivos foram mesclados com sucesso!")
    else:
        print("Esta pasta está vazia ou não contém nenhum PDF!")


caminho = input("Digite o caminho da pasta onde está os pdfs: ")
pdfs = arqs_lista(pega_arqs(caminho))
mescla(pdfs)
