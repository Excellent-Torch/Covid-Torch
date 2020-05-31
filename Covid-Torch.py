import requests
import re
from pyfiglet import figlet_format
from difflib import get_close_matches as gcm
from termcolor import cprint

covid19_api = requests.get('https://api.kawalcorona.com/').text
countries = re.findall('"Country_Region":"(.*?)"', covid19_api)

print '\n\x1b[0;37m========================================================\x1b[0;37m'

cprint(figlet_format("Covid-Torch", font = "doom"),"blue")

print '\n\x1b[0;37m[ --__-- ]===>[\x1b[40;32mForged By Excellent_Torch\x1b[0;37m]<===[ --__-- ]'
print '\n\x1b[0;37m========================================================\x1b[0;37m'


ask = raw_input('\n\x1b[44;37m=>[ \x1b[1;32mEnter Your Country \x1b[0;37m] := ')

cry = ('').join(gcm(ask, countries, n=1, cutoff=0))

info = '{"OBJECTID":.*?,"Country_Region":"' + cry + '","Last_Update":.*?,"Lat":.*?,"Long_":.*?,"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}'

results = re.search(info, covid19_api)

print ('\n\n\x1b[0;37m[ + ]============[\x1b[1;32m{}\x1b[0;37m] [\x1b[1;32mStatus\x1b[0;37m]=======[ + ]').format(cry)
print ('\n             [ \x1b[1;32mInfected \x1b[0;37m] : [\x1b[1;32m{}\x1b[0;37m]\n             \x1b[0;37m[ \x1b[1;32mDeaths \x1b[0;37m] : [\x1b[1;32m{}\x1b[0;37m]\n             \x1b[0;37m[ \x1b[1;32mRecovered \x1b[0;37m] : [\x1b[1;32m{}\x1b[0;37m]\n             \x1b[0;37m[ \x1b[1;32mActive \x1b[0;37m] : [\x1b[1;32m{}\x1b[0;37m]\n').format(results.group(1), results.group(2), results.group(3), results.group(4))
print '\x1b[0;37m[ + ]======================================[ + ]\x1b[0;37m'





