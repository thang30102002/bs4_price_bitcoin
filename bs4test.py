import bs4
import requests
import io
response=requests.get('https://crypto.com/price/vi/bitcoin')
html_doc=response.text

soup= bs4.BeautifulSoup(html_doc,'html.parser')

# Tìm phần tử chứa giá Bitcoin
price_element = soup.find('div', {'class': 'chakra-stack css-a9porv'})
# Lấy giá Bitcoin từ phần tử đã tìm thấy
price = price_element.text.strip()

# In ra giá Bitcoin
print('Giá Bitcoin hiện tại là:', price)