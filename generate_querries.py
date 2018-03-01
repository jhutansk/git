import tkinter
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def run():
    Username = entUsername.get()
    Password = entPassword.get()
    URL=entURL.get()
    driver = webdriver.Chrome();
    driver.get(URL);
    time.sleep(2)
    username = driver.find_element_by_id("jazz_app_internal_LoginWidget_0_userId");
    password = driver.find_element_by_id("jazz_app_internal_LoginWidget_0_password");
    username.send_keys(Username);
    password.send_keys(Password);
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']");
    login_attempt.submit();
    time.sleep(2)

#    driver.get(URL)
#    time.sleep(2)

    driver.find_element_by_css_selector("[title*='Edit Current Query']").click()
    time.sleep(2)

    #ids = driver.find_elements_by_xpath('//*[@aria-label]')
    #for i in ids:
            #print(i.get_attribute('aria-label'))

    ids = driver.find_elements_by_xpath("//*[starts-with(@aria-label,'Sample')]")

    for i in ids:
        outputName = i.get_attribute('aria-label')
        if not (outputName == "Sample State (sample)" or outputName == "Sample State (sample_state)"):
            output = str(i.get_attribute('aria-label'))+" "+str(i.get_attribute('entryid'))
            with open('querries.txt','r') as f:
                newlines = []
                for line in f.readlines():
                    newlines.append(line.replace('_hashvalue_',str(i.get_attribute('entryid'))))
                f.close()
            with open('querries_temp.txt', 'a') as f:
                for line in newlines:
                    f.write(line)
                f.close()
            with open('querries_temp.txt','r') as f:
                newlines = []
                for line in f.readlines():
                    newlines.append(line.replace('_Sample_ID_',str(i.get_attribute('aria-label'))))
                f.close()
            with open('querries_out.txt', 'a') as f:
                for line in newlines:
                    f.write(line)
                f.close()
            os.remove('querries_temp.txt')
    time.sleep(2)
    driver.quit()

window = tkinter.Tk()
window.title("Query Generator")
window.geometry("480x80")
window.resizable(False, False)
lblURL = tkinter.Label(window, text="URL")
entURL = tkinter.Entry(window)
lblURL.pack()
lblURL.place(x=5, y=5)
entURL.pack()
entURL.place(x=75, y=5, width=398)
lblUsername = tkinter.Label(window, text="Username")
entUsername = tkinter.Entry()
lblUsername.pack()
lblUsername.place(x=5, y=30)
entUsername.pack()
entUsername.place(x=75, y=30)
lblPassword = tkinter.Label(window, text="Password")
entPassword = tkinter.Entry()
lblPassword.pack()
lblPassword.place(x=5, y=55)
entPassword.pack()
entPassword.place(x=75, y=55)
btnRun = tkinter.Button(window, text="Generate", height = 2, width = 30 ,command=run)
btnRun.pack()
btnRun.place(x=230, y=32)

window.mainloop()
