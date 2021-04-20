from url_extractor import URLExtractor

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url_extractor = URLExtractor(url)
url_base = url_extractor.get_url_base()
url_params = url_extractor.get_url_params()

print(url_base)
print(url_params)

print(url_extractor.get_param_value("moedaOrigem"))
# print(url_extractor.get_param_value("testerror"))

print(url_extractor)

DOLLAR_VALUE = 5.50

from_currency = url_extractor.get_param_value("moedaOrigem")
to_currency = url_extractor.get_param_value("moedaDestino")
quantity = url_extractor.get_param_value("quantidade")


print(int(quantity) * DOLLAR_VALUE)
