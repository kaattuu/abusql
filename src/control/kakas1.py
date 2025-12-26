# cara 1 : bersihkan layar terminal
import os
def clear_view():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# bershihkan_layar()

# cara 2 : bersihkan layar terminal
# import subprocess
# import platform
# def bershihkan():
#     system = platform.system()
#     if system == "Windows":
#         subprocess.run("cls", shell=True)
#     elif system == "Linux" or system == "Darwin":
#         subprocess.run("clear", shell=True)
#     else:
#         pass
# bershihkan()

# # cara 3 : bersihkan layar terminal
# CLEAR_SCREEN = '\033[H\033[J'
# def bershihkan():
#     print(CLEAR_SCREEN)
# bershihkan()



