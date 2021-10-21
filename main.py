while driver.find_element_by_tag_name('div'):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs=driver.find_element_by_tag_name('div').text
    if 'End of Results' in Divs:
        print 'end'
        break
    else:
        continue