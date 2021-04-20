class URLExtractor:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        if not self.url:
            raise ValueError("URL is empty")

    def get_url_base(self):
        question_index = self.url.find("?")
        return self.url[0:question_index]

    def get_url_params(self):
        question_index = self.url.find("?")
        return self.url[question_index + 1 :]

    def get_param_value(self, param):
        url_params = self.get_url_params()
        params_list = url_params.split("&")

        found = False

        for list_param in params_list:
            if param in list_param:
                found = True
                splitted_param = list_param.split("=")
                return splitted_param[1]

        if not found:
            raise ValueError("Param not found")
