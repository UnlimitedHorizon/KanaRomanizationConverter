import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit

from Ui import Ui_Form
from Converter import str_kana_to_roman_list as str_kana_to_roman


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.textEdit.textChanged.connect(self.__convert)
        self.ui.textEdit.selectionChanged.connect(self.__select_text)
        self.ui.textEdit.setAcceptRichText(False)

        self.__text_list_convert = list()
        self.__text_list_show = list()

        self.show()


    def __show_convert_text(self):
        s = "".join(self.__text_list_show)
        s = s.replace("\n", "<br>")
        self.ui.textBrowser.setHtml(s)

    def __convert(self):
        text = self.ui.textEdit.toPlainText()
        self.__text_list_convert = str_kana_to_roman(text)
        self.__text_list_show = self.__text_list_convert.copy()
        self.__show_convert_text()

    def __change_style(self, start, end):
        if start >= end:
            self.__text_list_show = self.__text_list_convert.copy()
        else:
            style_left = ["<font style='background-color:blue; color:white;'>"]
            style_right = ["</font>"]
            self.__text_list_show = (
                                        self.__text_list_convert[0:start] 
                                        + style_left 
                                        + self.__text_list_convert[start:end] 
                                        + style_right 
                                        + self.__text_list_convert[end:]
            )

    def __select_text(self):
        cursor = self.ui.textEdit.textCursor()
        self.__change_style(cursor.selectionStart(), cursor.selectionEnd())
        self.__show_convert_text()


def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
