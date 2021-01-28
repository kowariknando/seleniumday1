#tutorial 4
'''from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5) #esto espera 5 segundos y luego empieza a ejecutar lo de abajo, es mas simple que la otra forma de hacer Wait

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1,-1,-1)]


actions = ActionChains(driver)

actions.click(cookie)

for i in range(10000000000):
    actions.perform()
    count = int(cookie_count.text.split(' ')[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

'''
    #print(count)










## TUTORIAL 3
#
'''

#import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains   # Esto es para hacer acciones dentro de la web
from selenium.webdriver.common.keys import Keys #this allow us to enter keys like hit enter and search

#this is for the WAIT:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#The 3 above are for the WAIT

import time
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')  #Esto abre una web
#driver.get('http://s18u0036.pri.hp.com:8001/seswinlite/home.action') #SESWINLITE
print(driver.title) #te da el t'itulo de la web
#driver.close() #esto cierra un tab
#driver.quit() #esto cierra to-do el browser


link = driver.find_element_by_link_text('Python Programming') #Busca un link en la web que se llame Python Programing, como cuando hacers ctr f
link.click() #hace click en el elemento link en este caso en el link que se llama Python Programming
driver.back() #go back
driver.forward() #go forward
#queremos que la pagina esté totalmente cargada para asegurarnos que el link está, vamos a hacer un wait
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.LINK_TEXT, 'Beginner Python Tutorials')) #By.LINK TEXT coge el texto de la web como CTR F
    )
    element.click()
finally:
    driver.quit()
'''

#Tutorial2
#Buscar en el Searcher
#y hacer una lista con elementos que se pueden recorrer con un for
'''search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)


#WAIT for serelenium that a specific thing to exist on the page before we start to look for it.
#what does it make? #we are gonna wait until the presence of this ID is located on the page before we decide to move on to the next part of the script
try:
    main = WebDriverWait(driver, 10).until(  #My elemento se llama
        EC.presence_of_element_located((By.ID, "main")) #el by.ID se puede cambiar a by.name or class or lo que sea
    )

    articles = main.find_elements_by_tag_name('article') #te hace una lista con las cosas que se llamen article en este caso el nombre de los art'iculos
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)
finally:
    driver.quit()
'''



################################ MI PROGRAMAAAAAAAAAAAA funcionando ######################################33
''' 
search1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div[2]/form/div/div[3]/div[1]/form/fieldset/div[1]/span')
#driver.implicitly_wait(10)
#search1.clear() #NO LO HE TESTEADO!!! pero esto deber'ia limpiar cualquier texto que haya en el sitio para escribir
ActionChains(driver).move_to_element(search1).send_keys('fernando').perform()
ActionChains(driver).move_to_element(search1).send_keys(Keys.TAB).perform()
ActionChains(driver).move_to_element(search1).send_keys('kowarik2016').perform()
ActionChains(driver).move_to_element(search1).send_keys(Keys.RETURN).perform()'''


#-------------------------------ESTUDIANDO PARA SESWINLITE+==========================================================================================================================
'''search1 = driver.find_element_by_class_name('grommetux-form-field__contents') #esto es una variable que va a store lo que ha encontrado en el elemento


#grommetux-form-field__contents es el nombre de la clase donde pongo mi nombre de usuario para login

#  'tlicensenumber' es la pestania By License/product para buscar por EONs
#searchFilterDTO.licenseNumber este es el serach para License Number



search1.send_keys("fernando") #test que le meto al search para buscar algo
search2 = driver.find_elements_by_class_name('grommetux-form-field__contents')
search2.send_keys('kowarik2016')
search2.send_keys(Keys.RETURN) #aqu'i le decimos que hit el enter el enter= Return'''



