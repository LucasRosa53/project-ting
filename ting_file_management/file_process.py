from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys

queueModel = Queue()  # instância


def process(path_file, instance: Queue):
    file = txt_importer(path_file)

    for element in instance.itens:
        if path_file in element["nome_do_arquivo"]:

            return

    dictionary = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(dictionary)
    print(dictionary)


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        print("Não há elementos")

    else:
        remove_file = instance.dequeue()
        print(f"Arquivo {remove_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


process("statics/nome_pedro.txt", queueModel)
process("statics/arquivo_teste.txt", queueModel)
print(queueModel.itens)