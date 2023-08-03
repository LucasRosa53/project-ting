from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer

def exists_word(word, instance: Queue):
    """Aqui irá sua implementação"""
    result = []
    list = instance.itens
    for element in list:
        ocorrencias = []
        for i, linha in enumerate(element["linhas_do_arquivo"]):
            if word.lower() in linha.lower():
                ocorrencias.append({
                    "linha": i +1
                })
        if ocorrencias:
            result.append({
                "palavra": word,
                "arquivo": element["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
        return result







def search_by_word(word, instance):
    """Aqui irá sua implementação"""
