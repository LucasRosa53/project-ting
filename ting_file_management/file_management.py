import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('.txt'):
        return sys.stderr.write('Formato inválido')

    try:

        with open(path_file, 'r') as file:
            lines = file.read().split('\n')

            return lines

    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
