import os
from colorama import init , Style,Fore

Color = {
      "cyan": Style.NORMAL+Fore.CYAN,
      "cyanBold": Style.BRIGHT+Fore.CYAN,
      "blue": Fore.BLUE,
      "blueBold": Style.BRIGHT+Fore.BLUE,
      "red": Style.NORMAL+Fore.RED,
      "redBold": Style.BRIGHT+Fore.RED,
      "green": Style.NORMAL+Fore.GREEN,
      "greenBold": Style.BRIGHT+Fore.GREEN,
      "white": Style.NORMAL+Fore.WHITE,
      "whiteBold": Style.BRIGHT+Fore.WHITE,
      "yellow": Style.NORMAL+Fore.YELLOW,
      "yellowBold": Style.BRIGHT+Fore.YELLOW
}

print("\033[H\033[J")
print(banner.Color['redBold'])
os.system("cat banner/banner.txt")
print("")
print("\t" + banner.Color['redBold'] + "Geolocation Spy" + banner.Color['white'] + " by " + banner.Color['whiteBold'] + "Entynetproject" + banner.Color['white'] + "" + banner.Color['blue'] + "" + banner.Color['white'] + "" + banner.Color['white'])
print("\t" + "-------------------------------------------------")
print("\t" + "|" + banner.Color['green'] + " People tracker on internet for OSINT research " + banner.Color['white'] + "|" + banner.Color['white'])
print("\t" + "-------------------------------------------------")
print("\t" + "| " + banner.Color['white'] + "v" + banner.Color['redBold'] + "2.0" + banner.Color['white'] + " |")    
print("\t" + "--------" + "\n")
