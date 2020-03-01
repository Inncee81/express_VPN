from pywinauto.application import Application
from time import sleep

def main():
    not_connected = True
    while not_connected:
        try:
            Application(backend="uia").start("ExpressVPN",timeout=10)
            app = Application(backend="uia").connect(path="ExpressVPN",timeout=10)

            main_dlg=app.window(title='ExpressVPN')

            i=0
            not_connected = main_dlg.Static0.window_text() in ['Not connected', 'Unable to Connect']

            while not_connected: 
                if i==1:
                    # switch to smart/recent location
                    main_dlg.CancelButton.click()
                    sleep(2)
                    main_dlg.Button6.click()
                elif i==2:
                    # switch to smart/recent location
                    main_dlg.CancelButton.click()
                    sleep(2)
                    main_dlg.Button7.click()
                    i=1
                elif i==0: 
                    main_dlg.Button4.click()
                
                sleep(5)

                # check if connecting
                while main_dlg.Static.window_text() == 'Connecting': 
                    sleep(1)
                
                i+=1
        except Exception as err:
            print(err)



if __name__ == '__main__':
    main()
