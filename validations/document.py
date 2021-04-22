from cpf import Cpf
from cnpj import Cnpj


class Document:
    @staticmethod
    def init(document):
        if len(document) == 11:
            return Cpf(document)
        elif (len(document)) == 14:
            return Cnpj(document)
        else:
            raise ValueError("Invalid document")