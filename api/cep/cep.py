import requests
import re


class Cep:
    api_url = "https://viacep.com.br/ws/{}/json/"

    def __init__(self, cep):
        sanitized_cep = self.sanitize(cep)
        if self.valid(sanitized_cep):
            self.data = self.getCepData(sanitized_cep).json()
            self.cep = sanitized_cep
        else:
            raise ValueError("Invalid CEP")

    def getCepData(self, cep):
        return requests.get(self.api_url.format(cep))

    def format(self):
        regex = re.search("([0-9]{2})([0-9]{3})([0-9]{3})", self.cep)
        return f"{regex.group(1)}{regex.group(2)}-{regex.group(3)}"

    def __str__(self):
        return self.format()

    def sanitize(self, cep):
        digits = re.findall("[0-9]+", cep)
        return "".join(digits)

    def valid(self, cep):
        return len(cep) == 8


cep = Cep("30.850-630")
print(cep)
print(cep.data)
