import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, pyqtSignal, QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import bs4 as bs
import urllib.request

class Client(QWebEnginePage):
    toHtmlFinished = pyqtSignal()

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_pageload)
        self.load(QUrl(url))
        self.app.exec()

    def on_pageload(self):
        self.app.quit()

    def store_html(self, html):
        self.html = html
        self.toHtmlFinished.emit()

    def get_html(self):
        self.toHtml(self.store_html)
        loop = QEventLoop()
        self.toHtmlFinished.connect(loop.quit)
        loop.exec_()
        return self.html

url = 'http://www.sinj.df.gov.br/sinj/ResultadoDePesquisa?tipo_pesquisa=norma&all=&ch_tipo_norma=&nm_tipo_norma=&nr_norma=&ano_assinatura=2021&ch_orgao=&ch_hierarquia=&sg_hierarquia_nm_vigencia=&origem_por=toda_a_hierarquia_em_qualquer_epoca1'
client_response = Client(url)
source = client_response.get_html()
# soup = bs.BeautifulSoup(source, 'html')
# jstest = soup.find_all('a')
# print(jstest.text)
x = open('agoravai.txt', 'w')
x.write(source)
x.close