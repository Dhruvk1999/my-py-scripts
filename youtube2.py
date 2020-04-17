import bs4,webbrowser,requests,time,re
from selenium import webdriver
browser=webdriver.Firefox()
    # Get address from command line.
#address = ' '.join(sys.argv[1:])
print("What song you wanna download from YouTube in mp4 format?")
address=input()
print(address)
res=requests.get("https://www.youtube.com/results?search_query="+address)
print("Downloading...")
#webbrowser.open("https://www.youtube.com/results?search_query="+search)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"lxml")
urls=soup.find_all("a")
links=[]
for ele in urls:
    link=ele.get("href")
    links.append(link)
lis=[]
watch=re.compile(r'/watch(.*)')
for item in links:
    a=watch.search(item)
    try:
        lis.append(a.group())
    except:
        pass
#webbrowser.open("http://www.youtube.com"+lis[0])
browser.get("https://www.youtubepp.com"+lis[0])
time.sleep(3)
elet=browser.find_elements_by_partial_link_text("Download")
#for i in range(0,7):
elet[2].click()
time.sleep(10)
new=browser.find_element_by_css_selector(".btn-file")
#new.click()
new.click()
print("Done!!")