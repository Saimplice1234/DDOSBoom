import requests
import sys
import bs4
import time
import subprocess
import random

subprocess.call('cls',shell=True)

t_start=time.time()

def init_banner():
    file_banner=open("banner/banner.txt")
    print(file_banner.read())
    print("\n")
pass

init_banner()

def scraping_user_agent(browser):

   target_url="http://www.useragentstring.com/pages/useragentstring.php?name={}"
   print("[+] Checking your request..")

   request_http=requests.get(target_url.format(browser))
   soup_parser = bs4.BeautifulSoup(request_http.text,'html.parser')
   
   for link in soup_parser.find_all('a'):
        if browser in link.get_text():
            output_uas="[+] {}"
            print(output_uas.format(link.get_text()))
pass

try:
    print("[+] Welcome agent fast an user agent provider")
    print("[+] All browser service")
    print("\n")
    print("[1] Chrome    [2] Firefox")
    print("[3] Edge      [4] Lunascape")
    print("[5] Mozilla   [6] Shiira")
    print("[7] Lobo      [8] Galaxy")
    print("[9] Arora     [10] Chimera")
    print("\n")

    pass_case=False
    get_number=input("[+] Choose the browser :")

    list_number=[1,2,3,4,5,6,7,8,9,10]
    
    list_browser=[
        "Chrome","Firefox","Edge",
        "Lunascape","Mozilla","Shiira",
        "Lobo","Galaxy","Arora","Chimera"
        ]

    for index_target in range(0,len(list_number)):
        list_number[index_target]=str(list_number[index_target])
    pass

    if get_number not in list_number:
        print("[-] Verify your entered information")
        while pass_case == False:
            get_number=input("[+] Choose the browser :")
            if get_number not in list_number:
                pass_case=False
            else:
                pass_case =True
                if  get_number  == '1':

                    scraping_user_agent(list_browser[0])

                elif get_number == '2':

                    scraping_user_agent(list_browser[1])

                elif get_number == '3':

                    scraping_user_agent(list_browser[2])

                elif get_number == '4':

                    scraping_user_agent(list_browser[3])

                elif get_number == '5':

                    scraping_user_agent(list_browser[4])

                elif get_number == '6':

                    scraping_user_agent(list_browser[5])

                elif get_number == '7':

                    scraping_user_agent(list_browser[6])

                elif get_number == '8':

                    scraping_user_agent(list_browser[7])

                elif get_number == '9':

                    scraping_user_agent(list_browser[8])
                elif get_number == '10':

                    scraping_user_agent(list_browser[9])
                    
        pass
    else:
        pass_case=True
        if  get_number  == '1':

            scraping_user_agent(list_browser[0])

        elif get_number == '2':

            scraping_user_agent(list_browser[1])

        elif get_number == '3':

            scraping_user_agent(list_browser[2])

        elif get_number == '4':

            scraping_user_agent(list_browser[3])

        elif get_number == '5':

            scraping_user_agent(list_browser[4])

        elif get_number == '6':

            scraping_user_agent(list_browser[5])

        elif get_number == '7':

            scraping_user_agent(list_browser[6])

        elif get_number == '8':

            scraping_user_agent(list_browser[7])

        elif get_number == '9':

            scraping_user_agent(list_browser[8])

        elif get_number == '10':

            scraping_user_agent(list_browser[8])
                      

except KeyboardInterrupt:
    print("[-] Ctrl + C")
    print("[-] Exit program")
    sys.exit(0)

t_end=time.time()- t_start
print("[+] Process finished in {} secondes".format(t_end))