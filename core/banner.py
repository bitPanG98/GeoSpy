import os

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
print(redBold)
os.system("cat banner/banner.txt")
print("")
print("\t" + Color.['redBold'] + "Geolocation Spy" + white + " by " + whiteBold + "Entynetproject" + white + "" + blue + "" + white + "" + white)
print("\t" + "-------------------------------------------------")
print("\t" + "|" + green + " People tracker on internet for OSINT research " + white + "|" + white)
print("\t" + "-------------------------------------------------")
print("\t" + "| " + white + "v" + redBold + "2.0" + white + " |")    
print("\t" + "--------" + "\n")
