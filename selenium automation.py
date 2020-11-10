from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random

op = Options()
op.add_argument("--headless")
driver = webdriver.Firefox(executable_path=".\geckodriver.exe", options=op)

while True:

    print("-----SEARCHING-----")

    driver.get("https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain")

    content = tuple(driver.find_element_by_xpath("/html/body/pre").text.splitlines())

    random_word = random.choice(content)

    go_daddy_website_url = f"https://in.godaddy.com/domainsearch/find?checkAvail=1&tmskey=1dom_03_godaddyb&domainToCheck={random_word}"
    driver.get(go_daddy_website_url)
    time.sleep(1)
    go_daddy = driver.find_element_by_class_name("domain-name-text").text

    if go_daddy.count("is available") > 0:
        print(f"Yay! Be fast {random_word}.com is available")
    else:
        print(f"{random_word}.com is taken")

    print("-----OPTIONS-----")
    print("1) Go to site")
    print("2) Search again")
    print("3) Exit")

    inp = int(input("Enter the option - \t"))

    if inp == 1:
        print(f"https://in.godaddy.com/domainsearch/find?checkAvail=1&tmskey=1dom_03_godaddyb&domainToCheck={random_word}")
        break

    if inp == 2:
        pass

    if inp == 3:
        break
