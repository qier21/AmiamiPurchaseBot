import sys
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

def checkProduct(driver, productLink, credentials, debug):

    driver.get(productLink)
    cart = []

    while len(cart) == 0:
        
        try:
            driver.implicitly_wait(5)
        except:
            print("timed out")
            pass
        try:
            elements = WebDriverWait(driver, 3).until(
                lambda d: [elem for elem in d.find_elements(By.CLASS_NAME, "btn-cart")
                          if elem.get_attribute("data-kanshi") == "productDetailAddCart9"]
            )
            print("element is:",elements)
            cart = list(filter(lambda element: element is not None and 
                element.get_attribute("style") == "", elements))

            for ele in elements:
                print("style is ", ele.get_attribute("style"))

            # check cart button
            if cart:
                print("cart button available")
            else:
                print("cart button unavailable")
                # some times, the button may be disabled for a brief period before it becomes available.
                # It might be because you have a good network quality.
                time.sleep(0.5)
                cart = list(filter(lambda element: element is not None and 
                    element.get_attribute("style") == "", elements))
                if cart:
                    print("cart button available after delay")

        except:
            print("out time, ",cart)
            pass

        # refreshing
        if len(cart) == 0: 
            time.sleep(2)
            print("refreshing")
            driver.refresh()
        else:
           pass
    # add to cart        
    cart[0].click()
    print("added to cart successfully")

    # proceed to checkout
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_btn")))
    elem_list = driver.find_elements(By.CLASS_NAME, "cart_btn")
    elem_list[0].click()
    print("proceed to checkout successfully")

    # log in
    email = driver.find_element(By.NAME, "email")
    email.send_keys(credentials["email"])

    passwd = driver.find_element(By.NAME, "password")
    passwd.send_keys(credentials["password"])

    submitButton = driver.find_element(By.CLASS_NAME, 'btn.btn-submit.btn-mini')
    submitButton.click()

    # continue checkout
    print("click continue")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-submit')))
    submitButton2 = driver.find_element(By.CLASS_NAME, 'btn-submit')
    print(submitButton2.get_attribute("data-kanshi"))
    # driver.find_element(By.CLASS_NAME, 'btn-submit').click()

    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/section/div[4]/button[2]').click()
    # driver.execute_script("document.getElementsByClassName('btn-submit')[0].click()")
    print("click continue fin")
    # Payment & shipping
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'shipping-method19')))

    driver.execute_script("document.getElementById('shipping-method19').click()")
    # unionpay
    driver.execute_script("document.getElementById('payment-method11').click()")
    driver.find_element(By.CLASS_NAME, "btn-submit").click()

    # review
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'section-title'), "Confirm your order"))
    confirm = driver.find_element(By.CLASS_NAME, "btn-submit")
    print("find the subimt button:", confirm.text)
    if not debug:
        confirm.click() 

        # if confirm.click() not available, try this 
        # driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/section/div[3]/form/button').click()

if __name__ == '__main__':


    # argument
    if len(sys.argv) < 2:
        print("usage: amiamiBot.py config_path [debug]")
        exit(1)

    # configFile = "config.json"
    debug = False
    configFile = sys.argv[1]
    if len(sys.argv) >= 3 and sys.argv[2] == "debug":
        debug = True

    with open(configFile) as cfg:
        # load configuration files
        config = json.load(cfg)
        credentials = config["credentials"]
        driverPath = config["driverPath"]
        link = config["itemLink"]
        userData = config["chromeUserData"]
        print("item link: ",link)
        # print("config: ",config)

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("detach", True)
        options.add_argument("user-data-dir="+userData)
        options.add_argument("--ignore-certificate-errors")

        service = Service(driverPath)
        driver = webdriver.Chrome(options=options,
                                  service=Service(driverPath))

        checkProduct(driver, link, credentials, debug)

        print("Completed")
