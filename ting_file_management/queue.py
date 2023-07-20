from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.itens = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.itens)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.itens.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if not len(self.itens) == 0:
            return self.itens.pop(0)
        else:
            return None

    def search(self, index):
        """Aqui irá sua implementação"""
        for i, e in enumerate(self.itens):
            if i == index:
                return e
        raise IndexError("Índice Inválido ou Inexistente")
