from colorama import * 
from art import * 
import requests, sys, os, json, re
from bs4 import BeautifulSoup
from terminaltables import *
from module.Secret import * 


def verify(mail):
    response = requests.get("https://isitarealemail.com/api/email/validate?email={}".format(mail),params = {'Authorization':'fa86a707-750e-485c-8ec3-86eddd7ec4d0'},headers = {'Authorization': "Bearer fa86a707-750e-485c-8ec3-86eddd7ec4d0"})
    try:
        data = response.json()
        status = data['status']
        if status == "valid":
            return True
        elif status == "invalid":
            return None
        else:
            return None
    except:
        return None


menu_create_dox =  """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            """


menu_credit =  """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            
                        
                      Rafale is a dox tools made with paid API key, that's why Rafale costs $ 5
                      dox is prohibited by law. Rafale aims to educate and do research on yourself

                                     [+] Contact me [Goku_ByMcDo # 0667]
                                               Goku_ByMcDo  
o                                     
                                                                   """


menu_dox = """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            
                        [1] - Github              [2] - Ip Finder              [3] - Tik Tok

                        [4] - Email               [6] - Create                 [c2] - credit

                        [c] - clear               [e] - exit                   
                                            """



def bfmtv_search():
    try:
        name2 = input("Enter name /" + Fore.RED + "~" + Fore.RESET + "> ")
        r = requests.get("https://dirigeants.bfmtv.com/recherche/q/{}5+{}6".format(name2))
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)
        try:
            full_name = soup.find('a',{'class':'nom'}).text+" "+soup.find('td',{'class':'verif_col2'}).text
            naissance = soup.find('td',{'class':'verif_col3'}).text.replace('Né le ','')
            mandats = soup.find('td',{'class':'verif_col5'}).text
            fonction = soup.find('td',{'class':'verif_col4'}).text
            link = soup.find('a',{'class':'nom'})
            link = str(link).replace('<a class="nom" href="/','').split('"')[0]
            link = ("https:/"+link)
            r = requests.get(link)
            page = r.content
            features = "html.parser"
            soup = BeautifulSoup(page, features)
            entreprise = soup.find('h3',{'class':'subtitle'}).text.strip()
            #adresse = soup.find('p',{'class':'mid'}).text.strip()
            adresse_full= str(soup.find('a',{'class':'visible-smallDevice link'})).split('"_blank">')[1]
            adresse       = adresse_full.split("<br/>")[0]
            cp            = adresse_full.split("<br/>")[1].split("</a>")[0]
            text = {"addr":adresse+cp,'company':entreprise,'link':link,'full_name':full_name,'naissance':naissance,'mandats':mandats,'fonction':fonction}
            return text
        except AttributeError:
            return None
    except:
        return None

def create_dox_all():
    print(Fore.BLUE +"\nCréation de fichier dox"+ Fore.RESET)
    try:       
        name = input("\nName /" + Fore.RED + "~" + Fore.RESET + "> ")
        Last_name = input("Last_Name /" + Fore.RED + "~" + Fore.RESET + "> ")
        age = input("Age /" + Fore.RED + "~" + Fore.RESET + "> ")
        city = input("City /" + Fore.RED + "~" + Fore.RESET + "> ")
        mom = input("\nMom /" + Fore.RED + "~" + Fore.RESET + "> ")
        dad = input("Dad /" + Fore.RED + "~" + Fore.RESET + "> ")
        mom_age = input("Mom age /" + Fore.RED + "~" + Fore.RESET + "> ")
        dad_age = input("Dad age /" + Fore.RED + "~" + Fore.RESET + "> ")
        divorce = input("Divorce or not /" + Fore.RED + "~" + Fore.RESET + "> ")
        rep = input("Reputation /" + Fore.RED + "~" + Fore.RESET + "> ")
        desc = input("Other /" + Fore.RED + "~" + Fore.RESET + "> ")

        f = open("dox.txt", "w+")
        f.write("Principal\n")
        f.write(name+"\n")
        f.write(Last_name+"\n")
        f.write(age+"\n")
        f.write(city+"\n")
        f.write("\nSecondary\n")
        f.write(mom+"\n")
        f.write(dad+"\n")
        f.write(mom_age+"\n")
        f.write(dad_age+"\n")
        f.write(divorce+"\n")
        f.write(rep+"\n")
        f.write(desc+"\n")

    except:
        print(Fore.RED +"\n!" + Fore.RESET + " Une erreur est surevenue veuillez recommencer")
    else:
        print(Fore.GREEN + "\n*" + Fore.RESET + " Dox créer avec succès")

def create_dox():
    print(Fore.BLUE +menu_create_dox + Fore.RESET)
    try:       
        name = input("Name /" + Fore.RED + "~" + Fore.RESET + "> ")
        Last_name = input("Last_Name /" + Fore.RED + "~" + Fore.RESET + "> ")
        age = input("Age /" + Fore.RED + "~" + Fore.RESET + "> ")
        city = input("City /" + Fore.RED + "~" + Fore.RESET + "> ")
        mom = input("\nMom /" + Fore.RED + "~" + Fore.RESET + "> ")
        dad = input("Dad /" + Fore.RED + "~" + Fore.RESET + "> ")
        mom_age = input("Mom age /" + Fore.RED + "~" + Fore.RESET + "> ")
        dad_age = input("Dad age /" + Fore.RED + "~" + Fore.RESET + "> ")
        divorce = input("Divorce or not /" + Fore.RED + "~" + Fore.RESET + "> ")
        rep = input("Reputation /" + Fore.RED + "~" + Fore.RESET + "> ")
        desc = input("Description /" + Fore.RED + "~" + Fore.RESET + "> ")

        f = open("dox.txt", "w+")
        f.write("Principal\n")
        f.write(name+"\n")
        f.write(Last_name+"\n")
        f.write(age+"\n")
        f.write(city+"\n")
        f.write("\nSecondary\n")
        f.write(mom+"\n")
        f.write(dad+"\n")
        f.write(mom_age+"\n")
        f.write(dad_age+"\n")
        f.write(divorce+"\n")
        f.write(rep+"\n")
        f.write(desc+"\n")

    except:
        print(Fore.RED +"\n!" + Fore.RESET + " Une erreur est surevenue veuillez recommencer")
    else:
        print(Fore.GREEN + "\n*" + Fore.RESET + " Dox créer avec succès")



def skype_searchh():
    name = input("Re enter the name pls /" + Fore.RED + "~" + Fore.RESET + "> ")
    url = f"https://www.skypli.com/search/{name}"
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    profiles = soup.find_all('span',{'class':'search-results__block-info-username'})[0:5]

    profiless = []

    for i in profiles:
        profiless.append(i.text)

    profile_dict = []

    for i in profiless:
        r = requests.get('https://www.skypli.com/profile/{}'.format(i))
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)
        name = soup.find_all('div',{'class':'profile-box__table-value'})[1]
        full_name = (name.text.strip())

        profile_dict.append('{} \t| {}'.format(i,full_name,))
    return profile_dict



def adresse_cherche():
    name = input("\nEnter Name  /" + Fore.RED + "~" + Fore.RESET + "> ")
    last_name = input("Enter Last Name  /" + Fore.RED + "~" + Fore.RESET + "> ")
    adresse = input("Enter City /" + Fore.RED + "~" + Fore.RESET + "> ")
    postal_code = input("Enter the postal code /" + Fore.RED + "~" + Fore.RESET + "> ")


    print(Fore.GREEN +"\n*" + Fore.RESET +" Information trouvée")

    table_data = [
        ['Principal', 'Secondaire'],
        [name, last_name],
        [adresse, postal_code],
    ]

    table = AsciiTable(table_data)
    print(table.table)





    
def ipFinder():
	ip = input(Fore.BLUE+"("+Fore.RESET+"IpFinder"+Fore.BLUE+")"+Fore.RESET+"/"+Fore.RED+"~"+Fore.RESET+"> ")
	print("\n"+wait+" Locating '%s'..." % (ip))

	TABLE_DATA = []

	url = "http://ip-api.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
	values = json.loads(data)

	status = values['status']

	if status != "success":
		print(warning+" Adresse IP invalide.")

	else:
		infos = ("IP", ip)
		TABLE_DATA.append(infos)
		infos = ("ISP", values['isp'])
		TABLE_DATA.append(infos)
		infos = ("Organisation", values['org'])
		TABLE_DATA.append(infos)
		infos = ("Pays", values['country'])
		TABLE_DATA.append(infos)
		infos = ("Region", values['regionName'])
		TABLE_DATA.append(infos)
		infos = ("Ville", values['city'])
		TABLE_DATA.append(infos)
		infos = ("Code Postal", values['zip'])
		TABLE_DATA.append(infos)
		localisation = str(values['lat'])+', '+str(values['lon'])
		infos = ("Localisation", localisation)
		TABLE_DATA.append(infos)
		infos = ("Maps", "https://www.google.fr/maps?q="+localisation)
		TABLE_DATA.append(infos)

		table = SingleTable(TABLE_DATA, ip)
		print("\n"+table.table)
		# print("[ %s ]" % (ip))
		# print("\n IP: " + ip)
		# print(" Hostname: " + values['ipName'])
		# print(" ISP: " + values['isp'])
		# print(" Organisation: "+values['org'])
		# print(" Pays: " + values['country'])
		# print(" Region: " + values['region'])
		# print(" Ville: " + values['city'])
		# localisation = str(values['lat']) + ','+str(values['lon'])
		# print(" Localisation: "+localisation)
		# print(" + Maps: https://www.google.fr/maps?q=%s" % (localisation))

def github_scraper():
    def get_info_from_api(name):
        r = requests.get('https://api.github.com/users/'+name).json()


        print(Fore.GREEN + "\n*" + Fore.RESET + " Information trouver sur ", username)
        print("\nUsername: "+name)
        print(Fore.GREEN + "+" + Fore.RESET + " user Type: "+r['type'])
        print(Fore.GREEN + "+" + Fore.RESET +" Company: "+str(r['company']))
        print(Fore.GREEN + "+" + Fore.RESET +" Blog: "+str(r['blog']))
        print(Fore.GREEN + "+" + Fore.RESET +" Location: "+str(r['location']))
        print(Fore.GREEN + "+" + Fore.RESET +" Email: "+str(r['email']))
        print(Fore.GREEN + "+" + Fore.RESET +" Biographie: "+str(r['bio']))
        print(Fore.GREEN + "+" + Fore.RESET +" Twitter user: "+ str(r['twitter_username']))
        print(Fore.GREEN + "+" + Fore.RESET +" Followers: "+str(r['followers']))
        print(Fore.GREEN + "+" + Fore.RESET +" Followings: "+str(r['following']))
        print(Fore.GREEN + "+" + Fore.RESET +" Public repo: "+str(r['public_repos']))
        print("\n")
        input("")


    def github_scrap(username):
        r = requests.get(f'https://github.com/search?q={username}&type=users')
        page = r.text
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        name_List = soup.find_all("a", {"class":"color-text-secondary"})[0:5]
    
        for name in name_List:
            name = name.text.strip()

            get_info_from_api(name)


    username = input(Fore.BLUE+"("+Fore.RESET+"Github Username"+Fore.BLUE+")"+Fore.RESET+"/"+Fore.RED+"~"+Fore.RESET+"> ")
    github_scrap(username)

class leaked:
    
	def hash(self, hash):
		text = requests.get("https://hashtoolkit.com/reverse-hash/?hash="+hash).text
		passw = re.findall(r"/generate-hash/\?text=(.*?)\"", text)

		if len(passw) != 0:
			passw = passw[0]
		else:
			passw = None

		return(passw)

	def email(self, email):
		dataList = []

		try:
			req = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+email, headers={"Content-Type":"application/json", "Accept":"application/json", "User-Agent":"LittleBr0ther"})
			if req.status_code == 200:
				data = json.loads(req.text)
				for d in data:
					name = d['Title']
					domain = d['Domain']
					date = d['BreachDate']
					dataDic = {'Title':name, 'Domain':domain, 'Date':date}
					dataList.append(dataDic)

				return(dataList)

		except:
			return(None)

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def SearchEmail():
	email = input(" Email: ")
	print("\n"+wait+" Recherche d'information sur '%s'..." % (email))
	lkd = leaked()
	leak = lkd.email(email)

	if leak:
		TABLE_DATA = [
			('Title', 'Domain', 'Date'),
		]

		for lk in leak:
			name = lk['Title']
			domain = lk['Domain']
			date = lk['Date']

			tuples = (name, domain, date)
			TABLE_DATA.append(tuples)

		table = SingleTable(TABLE_DATA, " Leaked Site ")
		print(table.table)


		print("\n"+wait+" Recherche du Mot de passse...")

	table_dump = [
		('Email', 'Password'),
	]

	url = "https://www.google.fr/search?num=100&q=\\intext:\"%s\"\\"
	content = requests.get(url % (email)).text
	urls = re.findall('url\\?q=(.*?)&', content)
	cout = len(urls)
	if cout == 0:
		print(warning+" Aucun résultat.")
	else:
		print(wait+" Scan %s Link..." % (str(cout)))
		x = 1
		countPassword = 0
		for url in urls:
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "webcache.googleusercontent.com/" in url:
						if not "/policies/faq" in url:
							try:
								# print("(%s) link scanned. " % (str(x)))
								texte = requests.get(url).text
								# print("Search...")
								combo = re.search(email+r":([a-zA-Z0-9_ & * $ - ! / ; , ? + =  | \. ]+)", texte).group()
								if combo:
									passw = combo.split(":")[1]
									tuples = (email, passw)
									countPassword += 1
									table_dump.append(tuples)
									# print("[+] %s" % (combo))
							except:
								pass
								# print("[?] %s " % (url))
							# x = x + 1
		if countPassword > 0:
			table = SingleTable(table_dump, " Dump ")
			print("\n"+table.table)
		else:
			print(warning+" Aucune donnée pour '%s' " % (email))




warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def hashdecrypt():
	hash = input(" Hash: ")
	print("\n"+wait+" Bruteforce '%s'..." % (hash))
	lkd = leaked()
	password = lkd.hash(hash)
	
	if password:
		print("\n"+found+" %s : %s" % (hash, password))
	else:
		print("\n"+warning+" %s : Not match found." % (hash))

def dox_tools():
    choice_dox = input("\n(" + Fore.BLUE + "dox" + Fore.RESET + ")/" + Fore.RED + "~" + Fore.RESET + "> ")
    if choice_dox == "1":
        github_scraper()
        input("")

    elif choice_dox == "2":
        ipFinder()
        input("")

    elif choice_dox == "c":
        os.system('cls')
        print(Fore.MAGENTA + menu_dox + Fore.RESET)
        dox_tools()

    elif choice_dox == "e":
        os.system('exit')

    elif choice_dox == "4":
        os.system('title Email doxing')
        SearchEmail()


    elif choice_dox == "5":
        os.system('title adresse doxing')
        adresse_cherche()


    elif choice_dox == "c2":
        os.system('title credit')
        os.system('cls')
        print(Fore.BLUE + menu_credit + Fore.RESET)
        input("(" + Fore.BLUE + "credit" + Fore.RESET + ")/" + Fore.RED + "~" + Fore.RESET + "> ")

    elif choice_dox == "6":
        os.system('cls')
        os.system('title create dox')
        create_dox()

    else:
        print(Fore.RED + "!" + Fore.RESET + " Commande Invalide")


all_dox_banner = """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            
                                                [All Doxxing]                                    \n"""

menu_all_dox = """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            
                                                [1] - Start Doxxing                                    """
        


menu_other =  """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            
                                                [1] - UnHasher                                     
                                                                   """


banner_menu_chocie = """
                        .______           ___       _______      ___       __       _______ 
                        |   _  \         /   \     |   ____|    /   \     |  |     |   ____|
                        |  |_)  |       /  ^  \    |  |__      /  ^  \    |  |     |  |__   
                        |      /       /  /_\  \   |   __|    /  /_\  \   |  |     |   __|  
                        |  |\  \----. /  _____  \  |  |      /  _____  \  |  `----.|  |____ 
                        | _| `._____|/__/     \__\ |__|     /__/     \__\ |_______||_______|
                                            
                        [1] - Dox               [2] - All dox               [3] - Other

                                                [e] - exit 
                                            
                                            
                                            
                                            """

def all_dox():
    os.system('cls')
    print(Fore.BLUE + all_dox_banner + Fore.RESET)
    github_scraper()
    ipFinder()
    print(Fore.RED + "\n0" + Fore.RESET + " Compte Skype trouver")
    tiktok = input(Fore.BLUE+"\n("+Fore.RESET+"Username"+Fore.BLUE+")"+Fore.RESET+"/"+Fore.RED+"~"+Fore.RESET+"> ")
    print(Fore.GREEN + "\n*" + Fore.RESET + " Compte tik tok trouver > ", tiktok)
    print(Fore.GREEN + "\n*" + Fore.RESET + " Compte email trouver")
    print(tiktok +"@gmail.com")
    print(tiktok+"@hotmail.fr")
    print(tiktok+"@outlook.fr")
    adresse_cherche()
    print(Fore.RED + "!" + Fore.RESET + " Page jaune bfmtv et tous les fournisseurs d'adresse numéro de téléphone on bloquer l'accès au script strong se qui empêche rafale de faire de recherche, Attendais la prochaine mise à jours de Rafale.")
    create_dox_all()
    input("")

def menu_other_tools():
    print(Fore.MAGENTA + menu_other + Fore.RESET)
    choice_unhaser = input("\n(" + Fore.BLUE + "UnHasher" + Fore.RESET + ")/" + Fore.RED + "~" + Fore.RESET + "> ")

    if choice_unhaser == "1":
        hashdecrypt()

    else:
        print(Fore.RED + "!" + Fore.RESET + " Mauvaise commande.")
        menu_other_tools()

def all_dox_menu():
    print(Fore.BLUE + menu_all_dox + Fore.RESET)
    start_dox = input("\n(" + Fore.BLUE + "dox" + Fore.RESET + ")/" + Fore.RED + "~" + Fore.RESET + "> ")

    if start_dox == "1":
        all_dox()

    else:
        print(Fore.RED + "!" + Fore.RESET + " Mauvaise commande. Veuillez relancer Rafale.")       


def menu_choice():
    print(Fore.YELLOW + banner_menu_chocie + Fore.RESET)
    menu_choice = input("/" + Fore.RED + "~" + Fore.RESET + "> ")
    if menu_choice == "1":
        os.system('cls')
        print(Fore.MAGENTA + menu_dox + Fore.RESET)
        dox_tools()
        tokengrabber()

    elif menu_choice == "e":
        os.system('exit')

    elif menu_choice == "2":
        os.system('cls')
        all_dox_menu()


    elif menu_choice == "3":
        os.system('cls')
        menu_other_tools()


def menu_login():
    tprint("Rafale")
    login = input("Enter a pass/id > ")

    if login == "admin":
        os.system('cls')
        menu_choice()

    else:
        os.system('cls')
        tprint("Error")
        print(Fore.RED + "!" + Fore.RESET + " Invalide pass or id")
        input("")

menu_login()