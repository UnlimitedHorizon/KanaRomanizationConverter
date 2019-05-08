import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit

from Ui import Ui_Form
from Transfer import str_kana_to_roman as str_kana_to_roman


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.textEdit.textChanged.connect(self.__transfer)
        self.ui.textEdit.selectionChanged.connect(self.__select_text)
        self.ui.textEdit.setAcceptRichText(False)

        self.__text_list_transfer = list()
        self.__text_list_show = list()

        self.show()


    def __show_transfer_text(self):
        s = "".join(self.__text_list_show)
        s = s.replace("\n", "<br>")
        self.ui.textBrowser.setHtml(s)

    def __transfer(self):
        text = self.ui.textEdit.toPlainText()
        self.__text_list_transfer = str_kana_to_roman(text)
        self.__text_list_show = self.__text_list_transfer.copy()
        self.__show_transfer_text()

    def __change_style(self, start, end):
        if start >= end:
            self.__text_list_show = self.__text_list_transfer.copy()
        else:
            style_left = ["<font style='background-color:blue; color:white;'>"]
            style_right = ["</font>"]
            self.__text_list_show = (
                                        self.__text_list_transfer[0:start] 
                                        + style_left 
                                        + self.__text_list_transfer[start:end] 
                                        + style_right 
                                        + self.__text_list_transfer[end:]
            )

    def __select_text(self):
        cursor = self.ui.textEdit.textCursor()
        self.__change_style(cursor.selectionStart(), cursor.selectionEnd())
        self.__show_transfer_text()


def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
