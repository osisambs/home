import os
import subprocess
from datetime import datetime
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('reset')  # This may help in some terminal environments


def display_art():
    ascii_art = r"""                                        
       ...::::::::...                                    
            ..::^~!?JJJ?7~.                              
      ..:^~!!777!!77?JYPBBG                            
     ....     .:^!7JJYYYJ?Y7                          
          .^!7!~^:..      :&&P55Y?7!^:.                                         
       .::..            .P#J~:::^!J5GGGJ.              
                        G&.          .!&&7               ___ ___   _   _  _     
                       .@B              :?J.       BY:  |_ _/ __| /_\ | \| |    
                        ?@5.                             | |\__ \/ _ \| .` |  _ 
                         :P#GY?!!!~~^:.                 |___|___/_/ \_\_|\_| (_)
                            :~!!!7?J5G#BP7~:                                    
                                       :!5?~7^          ▐▄▄▄ ▄▄▄·  ▐ ▄     ▄▄▄▄·  ▄▄▄·  ▄▄·       ▄▄▄▄▄
                                          ?? ^~          ·██▐█ ▀█ •█▌▐█    ▐█ ▀█▪▐█ ▀█ ▐█ ▌▪▪     •██  
                                           !! .        ▪▄ ██▄█▀▀█ ▐█▐▐▌    ▐█▀▀█▄▄█▀▀█ ██ ▄▄ ▄█▀▄  ▐█.▪
                                            !          ▐▌▐█▌▐█ ▪▐▌██▐█▌    ██▄▪▐█▐█ ▪▐▌▐███▌▐█▌.▐▌ ▐█▌·
                                                        ▀▀▀• ▀  ▀ ▀▀ █▪    ·▀▀▀▀  ▀  ▀ ·▀▀▀  ▀█▄▀▪ ▀▀▀ 
    """
    
    print(ascii_art)

def main():
    print("\033[46m \033[1m CAPE BRE BANYAK HATERS WKWK🤮 \033[0m")
    print("\033[35mGa butuh temen yang bnyk bacot,\nkalo ga suka, anggep aja gw error yang harus di-debug. \033[0m")
    print("\033[34m⏰ selau inget waktu: {:%H:%M:%S}\033[0m".format(datetime.now()))

    display_art()

    while True:
        user_input = input("\033[36mIsan😪 > \033[0m")
        if user_input.lower() == 'exit':
            break
        else:
            try:
                subprocess.run(user_input, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error saat menjalankan '{user_input}': {e}")

if __name__ == "__main__":
    main()
