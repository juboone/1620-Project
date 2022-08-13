from controller import *
"""Constructor for the gui application"""
def main():
    app= QApplication([])
    window = controller()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()