from PyPDF2 import PdfFileMerger
import shutil, os


def pega_arqs(*args) -> tuple:
    l = []
    for item in args:
        for p, _, files in os.walk(os.path.abspath(item)):
            for file in files:
                if file.find(".pdf") != -1:
                    l.append((p, file))

    print(l)
    return l


def arqs_lista(*args) -> list:
    arqs = []
    for elemento in args:
        for item in elemento:
            try:
                arqs.append(item[0]+ "\\" + item[1])
            except FileNotFoundError:
                print("Algum arquivo contém erros, saindo ...")
                break
    print(len(arqs)," arquivos." )
    return arqs


def mescla(listaPdfs):
    if lista != []:
        merger = PdfFileMerger()
        for pdf in listaPdfs:
            merger.append(pdf)

        nome_arquivo = "Instrumento Geral"
        merger.write(f"{nome_arquivo}.pdf")
        merger.close()
        caminho_atual = os.getcwd()
        shutil.move(f"{caminho_atual}\\{nome_arquivo}.pdf",caminho)
        print("Os arquivos foram mesclados com sucesso!")
    else:
        print("Esta pasta está vazia ou não contém nenhum PDF!")


caminho = input("Digite o caminho da pasta onde está os pdfs: ")
pdfs = arqs_lista(pega_arqs(caminho))
mescla(pdfs)
