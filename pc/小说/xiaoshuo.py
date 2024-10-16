from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--no-proxy-server')
options.add_argument('--proxy-server="DIRECT"')
driver = webdriver.Chrome(options=options)

