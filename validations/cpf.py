from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        if self.is_valid(document):
            self.cpf = document
        else:
            raise ValueError("Invalid CPF")

    def is_valid(self, document):
        if len(document) != 11:
            raise ValueError("CPF must have 11 digits")
        cpf = CPF()
        return cpf.validate(document)

    def __str__(self):
        return self.format()

    def format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)