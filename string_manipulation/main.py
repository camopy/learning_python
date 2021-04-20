url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

question_index = url.find("?")

url_base = url[0:question_index]
url_params = url[question_index + 1 :]

print(url_base)
print(url_params)

print(url_params.split("&"))