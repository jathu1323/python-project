import colorama
from colorama import Back, Fore, Style

#Initialize colorama
colorama.init(autoreset=True)
#Print text using background and font colors
print(Back.RED + Fore.BLUE + "Welcome to LinuxHint")
print()
print(Back.GREEN + "I like programming")
print(Fore.CYAN + 'Welcome to Linuxhint')
print(Back.YELLOW + Style.DIM+ 'Learn Python', end='')
print(Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + 'Bright Text', end='')
print(Style.RESET_ALL)
print(Style.NORMAL + 'Normal Text')
