from bs4 import BeautifulSoup
import requests
from request_header import headers

class Convert_to_currency:

    def __init__(self, to_currency, from_currency, value):
      self.to_currency = to_currency.lower()
      self.from_currency = from_currency.lower()
      self.value = value

    def get_currency_convert(self):
        url = f"https://www.forbes.com/advisor/money-transfer/currency-converter/{self.from_currency}-{self.to_currency}/?amount={self.value}"
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")

        result_box = soup.find('div', attrs={ 'class': 'result-box' } )
        To = result_box.find('h2', 'result-box-conversion').find('span', 'amount').get_text() #span for converted currency

        return f"FROM: {self.value} {self.from_currency} TO: {To} {self.to_currency}"