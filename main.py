from selenium import webdriver
from selenium.webdriver.common.by import By
#
# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# url1="https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=pd_rhf_d_ee_s_pd_sbs_rvi_sccl_1_1/135-0460176-6142851?pd_rd_w=ajYm2&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=DXMH2P11MG8EBAPZ060P&pd_rd_wg=ODUOg&pd_rd_r=4efb55e1-73cd-402a-8f9f-cd8ae7ccb159&pd_rd_i=B06Y1MP2PY&th=1"
# url2="https://python.org"

# driver.get(url1)
# price = driver.find_element(By.ID, "corePrice_feature_div")
# print(price.text)

# # closes one tab
# driver.close()
#
# # closes all tabs
# driver.quit()







# driver.get(url2)
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo)
# print(logo.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# submit_bug_button = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug_button.text)




# driver.get(url2)
# upcoming_events_array = [row.text for row in driver.find_element(By.CLASS_NAME, "event-widget").find_element(By.CLASS_NAME, "menu").find_elements(By.TAG_NAME, "li")]
# upcoming_events = {}
#
# counter = 0
# for event in upcoming_events_array:
#     time = event.split("\n")[0]
#     name = event.split(("\n"))[1]
#
#     upcoming_events[counter] = {"time" : time, "name" : name}
#     counter += 1
#
# print(upcoming_events)






# import interaction






# import gmailV2





import cookie_clicker
