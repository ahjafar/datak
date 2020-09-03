import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import bs4
from datetime import date,datetime


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        global GBAction,dayAction
        GBAction=menu.addAction("GB")
        dayAction=menu.addAction(" Days")
        refreshAction=menu.addAction("Refresh")
        exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)
        exitAction.triggered.connect(self.exit)
        refreshAction.triggered.connect(self.refresh)

    def exit(self):
        QtCore.QCoreApplication.exit()
    def refresh(self):
        v=get_data()
        d=get_time()
        print(v)
        GBAction.setText(str(v)+"GB")
        dayAction.setText(str(d)+"Days")
        if condition(v,d)==1:
            #SystemTrayIcon(QtGui.QIcon(r"C:\\Users\\98930\Desktop\\favicon-red.png"), w)# ADD PATH OF YOUR ICON HERE .png works
            #trayIcon.setToolTip("وضع خوبه")
            #trayIcon.show()
            self.setIcon(QtGui.QIcon(r"favicon-red.png"))
            self.setToolTip("ریحانه داره اینترنتو می خوره")
        else:
            #SystemTrayIcon(QtGui.QIcon(r"C:\\Users\\98930\Desktop\\favicon-green.png"), w)# ADD PATH OF YOUR ICON HERE .png work
            #trayIcon.setToolTip("ریحانه داره اینترنتو می خوره")
            #trayIcon.show()
            self.setIcon(QtGui.QIcon(r"favicon-green.png"))
            self.setToolTip("وضع خوبه")
def main(image):
    global w,trayIcon,app
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon(image), w)
    trayIcon.refresh()
    trayIcon.show()
    sys.exit(app.exec_())

def get_data():
    i=0
    site=requests.get("http://datak.ir/mydatak/service_profile?detail_id=profile.show&oid=81336487")
    soup=bs4.BeautifulSoup(site.content.decode("UTF-8"), 'html.parser')
    for link in soup.findAll("span"):
        if(i==1):   
            i=0
            return float(link.string)
        if(link.string=="صفحه اصلی"):
            i=1

def get_time():
    f_date = date(2020, 6, 6)
    l_date = datetime.now().date()
    return (l_date - f_date).days

def condition(v,d):
    if((100-v)/d>3.33):
        #print("ریحانه داره اینترنتو میخوره")
        return 1
    else:
        #print("وضع خوبه")
        return 0
if __name__ == '__main__':
    on=r"favicon.png"# ADD PATH OF YOUR ICON HERE .png works       
    main(on)
    