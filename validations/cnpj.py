from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, document):
        if self.is_valid(document):
            self.cnpj = document
        else:
            raise ValueError("Invalid CNPJ")

    def is_valid(self, document):
        if len(document) != 14:
            raise ValueError("CNPJ must have 14 digits")
        cnpj = CNPJ()
        return cnpj.validate(document)

    def __str__(self):
        return self.format()

    def format(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)