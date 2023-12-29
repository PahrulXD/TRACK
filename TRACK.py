import requests, os, json

def masuk():
	os.system ("clear")
	print("\033[1;97m[1] track ip address")
	print ("\033[1;97m[2] track number phone")
	tanya = input ("\n\033[1;97m[+] choice : ")
	if tanya =="1":
		x()
	elif tanya =="2":
		xx()
	else:
		exit()
	
	
	
def x():
	target = input ("\n\033[1;97m- masukkan ip target : ")
	data = requests.get (f"http://ip-api.com/json/{target}").json()
	print("\n- country :",data["country"])
	print("- countryCode :",data["countryCode"])
	print("- region :",data["region"])
	print("- regionName :",data["regionName"])
	print("- city : ",data["city"])
	print("- lat :",data["lat"])
	print("- lon :",data["lon"])
	print("- timezone :",data["timezone"])
	print("- isp :",data["isp"])
	print("- as :",data["as"])
	print("- query :",data["query"])
	print("")
	
def xx():
	number =  input ("\n\033[1;97m- masukkan number phone : ")
	output = requests.get(f'http://phone-number-api.com/json/?number={number}').text
	data = json.loads(output)
	print("\n- query :",data["query"])
	print("- numberCountryCode :",data["numberCountryCode"])
	print("- formatE164 :",data["formatE164"])
	print("- formatNational :",data["formatNational"])
	print("- formatInternational :",data["formatInternational"])
	print("- dialFromCountryCode :",data["dialFromCountryCode"])
	print("- carrier :",data["carrier"])
	print("- continent :",data["continent"])
	print("- continentCode :",data["continentCode"])
	print("- country :",data["country"])
	print("- countryName :",data["countryName"])
	print("- lat :",data["lat"])
	print("- lon :",data["lon"])
	print("- timezone :",data["timezone"])
	print("- currency :",data["currency"])
	print("")
	
	
masuk()