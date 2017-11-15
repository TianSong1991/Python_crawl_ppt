from selenium import webdriver

driver = webdriver.Chrome()

for i in range(1,10):
    driver.get('http://www.1ppt.com/moban/')
    sleep(3)
    driver.find_element_by_xpath(('/html/body/div[5]/dl/dd/ul/li[{0}]/a/img').format(i)).click()
    sleep(2)

    # 获得当前窗口
    nowhandle = driver.current_window_handle
    # 获得所有窗口
    allhandles = driver.window_handles
    # 循环判断窗口是否为当前窗口
    for handle in allhandles:
        if handle == nowhandle:
            driver.close()
            print ('now register window!')
    for handle in allhandles:
        if handle != nowhandle:
            driver.switch_to_window(handle)
            print ('register window!')

    driver.find_element_by_xpath('/html/body/div[6]/div[1]/dl/dd/ul[1]/li/a').click()
    sleep(3)