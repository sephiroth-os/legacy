global current_music
global gmail_service
global bgmusic
print('Reading files...')
import time
import random
from google_auth_oauthlib.flow import InstalledAppFlow
from tqdm import tqdm
import os
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from colorama import Fore, Back, Style
import socket
from pygame import mixer
import platform
import psutil
import base64
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv
from google import genai
import math
import requests
import sys
from yaspin import yaspin
from asteval import Interpreter
import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import *
from rich.console import Console
from rich.markdown import Markdown
from datetime import datetime
import pywinstyles
console = Console()
time.sleep(1)
try:
    homedir = os.environ.get('USERPROFILE', os.path.expanduser('~'))
    print('Successfully located ' + homedir)
except:
    print(Fore.RED + Style.BRIGHT + '[!] CRITICAL EXCEPTION .. CANNOT CONTINUE' + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + 'ERROR CODE .. [210]' + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + '[?] WHAT THIS MEANS: THERE IS NO USER DIRECTORY ON YOUR DEVICE.' + Style.RESET_ALL)
    print('--------------------')
    os.system('pause')
    sys.exit(0)
TOKEN_FILE = os.path.join(homedir, 'SephOS\\OAuth\\token.json')
CREDENTIALS_FILE = os.path.join(homedir, 'SephOS\\OAuth\\credentials.json')
SCOPES = ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.readonly']
gmail_service = None
mainpathname = 'SephOS'
fullpath = os.path.join(homedir, mainpathname)
print(fullpath)
UPDATER_EXE = os.path.join(fullpath, 'Updater.exe')
LOCAL_VERSION = 'v2.1.0-beta'
GITHUB_API_LATEST = 'https://api.github.com/repos/oxygen-me/SephOSPermsReq/releases/latest'
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '\n   _____            __    _            __  __    ____  _____\n  / ___/___  ____  / /_  (_)________  / /_/ /_  / __ \\/ ___/\n  \\__ \\/ _ \\/ __ \\/ __ \\/ / ___/ __ \\/ __/ __ \\/ / / /\\__ \\ \n ___/ /  __/ /_/ / / / / / /  / /_/ / /_/ / / / /_/ /___/ / \n/____/\\___/ .___/_/ /_/_/_/   \\____/\\__/_/ /_/\\____//____/  \n         /_/                                                                                                                      \n                                            ' + Style.RESET_ALL)
time.sleep(1)
print('SephirothOS™')
time.sleep(0.5)
print(LOCAL_VERSION)
def check_for_update():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    try:
        response = requests.get(GITHUB_API_LATEST, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        latest_tag = data.get('tag_name', '').strip()
        if latest_tag != LOCAL_VERSION:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f'\n[UPDATE] New version {latest_tag} available! You are running {LOCAL_VERSION}.')
            choice = input('[UPDATE] Update now? (y/n): ' + Style.RESET_ALL).strip().lower()
            if choice == 'y':
                zip_url = None
                for asset in data.get('assets', []):
                    if asset['name'].lower().endswith('.zip'):
                        zip_url = asset['browser_download_url']
                        break
                if zip_url:
                    download_and_apply_update()
                else:
                    print('[UPDATE] No ZIP release found!')
        else:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f'You are running the latest version! ({LOCAL_VERSION})' + Style.RESET_ALL)
    except Exception as e:
        print('[UPDATE] Failed to check GitHub release:', e)
def download_and_apply_update():
    if os.path.exists(UPDATER_EXE):
        os.startfile(UPDATER_EXE)
        print('[UPDATE] Updater launched.')
        time.sleep(1)
        sys.exit(0)
    else:
        print('[UPDATE] Updater not found!')
check_for_update()
time.sleep(2)
print('Welcome to SephirothOS! This is another shitty OS made by Oxygen-Me and Sephiroth and Schles.')
time.sleep(3)
print('Good luck.')
time.sleep(1)
print('Checking for directory and profile...')
pbar = tqdm(total=128)
for i in range(128):
    time.sleep(0.02)
    pbar.update(1)
pbar.close()
filefound = 0
try:
    person = open(fullpath + '\\SephOS-Profile.txt', 'x')
    person.close()
    os.remove(fullpath + '\\SephOS-Profile.txt')
    filefound = 0
except FileExistsError:
    filefound = 1
apps = ['Autism', 'Congregation', 'SephWipe', 'App4', 'App5', 'App6', 'App7', 'App8', 'App9', 'App10']
if filefound == 1:
    print('Profile found!')
    personend = 'SephOS-Profile.txt'
    sysend = 'SephOS-System.txt'
    append = 'SephOS-Apps.txt'
    personpath = os.path.join(fullpath, personend)
    sysinfopath = os.path.join(fullpath, sysend)
    appstatuspath = os.path.join(fullpath, append)
    sysinfo = open(sysinfopath, 'r')
    appstatus = open(appstatuspath, 'w+')
    with open(personpath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    f.close()
    username = lines[3]
    password = lines[4]
    first_name = lines[5]
    last_name = lines[6]
    pbar = tqdm(total=100)
    for i in range(100):
        time.sleep(0.01)
        pbar.update(1)
    pbar.close()
    print('[---|------[--]------|---]')
    print('| Welcome to SephirothOS |')
    print('[---|------[--]------|---]')
    time.sleep(2)
    print('Welcome back, ' + username + '!')
else:
    if filefound == 0:
        print('Profile not found!')
        personend = 'SephOS-Profile.txt'
        sysend = 'SephOS-System.txt'
        append = 'SephOS-Apps.txt'
        setend = 'SephOS-Cache.txt'
        personpath = os.path.join(fullpath, personend)
        sysinfopath = os.path.join(fullpath, sysend)
        appstatuspath = os.path.join(fullpath, append)
        person = open(personpath, 'w+')
        sysinfo = open(sysinfopath, 'r')
        person.write('APPLICATION: SephirothOS\n')
        person.write('[!] DO NOT EDIT INFO\n')
        person.write('[!!!] EDITING DATA WILL RESULT IN DATA LOSS AND/OR CORRUPTION\n')
time.sleep(2)
if filefound == 0:
    print('Let\'s get you registered!')
    time.sleep(2)
    print('[---|------------[---]------------|---]')
    print('| SephirothOS Account Creation Wizard |')
    print('[---|------------[---]------------|---]')
    time.sleep(1)
    print('First, you need a username.')
    time.sleep(1)
    print('- Up to 30 characters.')
    print('- No symbols')
    print('- No spaces')
    time.sleep(2)
    username_usable = 0
    while username_usable == 0:
        username = input('Enter your username: ')
        time.sleep(1)
        if len(username) > 30:
            print('This username is too long!')
            time.sleep(2)
        else:
            if ' ' in username:
                print('This username contains space(s).')
                time.sleep(2)
            else:
                if not username.isalnum():
                    print('This username contains special characters!')
                    time.sleep(2)
                else:
                    username_usable = 1
    time.sleep(2)
    print('Alright, now for your password')
    time.sleep(1)
    print('- No Spaces.')
    print('- At least 3 characters.')
    password_usable = 0
    while password_usable == 0:
        password = input('Enter a password: ')
        time.sleep(1)
        if ' ' in password:
            print('This password has space(s)!')
            time.sleep(2)
        else:
            if len(password) < 3:
                print('This password is too short!')
                time.sleep(2)
            else:
                password_usable = 1
    time.sleep(2)
    passcheck = '% placeholder %'
    while passcheck != password:
        passcheck = input('Confirm Password: ')
        time.sleep(1)
        if passcheck != password:
            print('Those do not match!')
            time.sleep(2)
        else:
            print('Proceeding')
    time.sleep(2)
    print('[---|-----------[-]-----------|---]')
    print('| SephirothOS Registration Wizard |')
    print('[---|-----------[-]-----------|---]')
    time.sleep(2)
    print('Let\'s fill out some personal info!')
    time.sleep(2)
    first_name = input('What is your first name: ')
    time.sleep(1)
    last_name = input('What is your last name: ')
    time.sleep(2)
    print('Got it.')
    person.write(username + '\n')
    person.write(password + '\n')
    person.write(first_name + '\n')
    person.write(last_name + '\n')
    person.flush()
    person.close()
    time.sleep(1)
    print('[---|------[--]------|---]')
    print('| Welcome to SephirothOS |')
    print('[---|------[--]------|---]')
    time.sleep(2)
    print('Welcome to SephirothOS, ' + username + '!')
lines = sysinfo.readlines()
myOEM = lines[3]
oem = int(myOEM.strip())
time.sleep(2)
pirated = True
if myOEM.strip() == '1':
    pirated = False
    print('Edition: Basic')
else:
    if myOEM.strip() == '2':
        print('Edition: Workplace')
        pirated = False
    else:
        if myOEM.strip() == '3':
            print('Edition: Premium')
            pirated = False
        else:
            if myOEM.strip() == '4':
                pirated = False
                print('Edition: Ultra')
            else:
                messagebox.showerror('Go Fuck Yourself', 'You pirated and/or modified the Sephiroth. Now you must die. . .')
                os.system('pause')
                os.system('shutdown /s /t /c')
if os.path.exists(appstatuspath):
    with open(appstatuspath, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
else:
    lines = []
while len(lines) < len(apps):
    lines.append('0')
with open(appstatuspath, 'w') as f:
    for line in lines:
        f.write(line + '\n')
sysinfo.close()
mixer.init()
bgmusic = 1
MUSIC_DIR = os.path.join(fullpath, 'Music')
LAST_MUSIC_FILE = os.path.join(MUSIC_DIR, 'last_bg_music.txt')
DEFAULT_MUSIC = os.path.join(MUSIC_DIR, 'DefaultMusic - DefaultGuy.mp3')
current_music = None
shopMusicPath = os.path.join(MUSIC_DIR, 'Shopiroth Music - Schles.mp3')
def load_last_music():
    global current_music
    if os.path.exists(LAST_MUSIC_FILE):
        with open(LAST_MUSIC_FILE, 'r', encoding='utf-8') as f:
            path = f.read().strip()
        if os.path.exists(path):
            current_music = path
        else:
            current_music = DEFAULT_MUSIC
    else:
        current_music = DEFAULT_MUSIC
    try:
        mixer.music.load(current_music)
        mixer.music.play((-1))
    except Exception as e:
        print(f'Failed to load music: {e}')
def save_current_music():
    if current_music:
        with open(LAST_MUSIC_FILE, 'w', encoding='utf-8') as f:
            f.write(current_music)
def music_menu():
    # irreducible cflow, using cdg fallback
    global current_music
    global bgmusic
    # ***<module>.music_menu: Failure: Different control flow
    per_page = 10
    music_files = [os.path.join(root, f) if f.lower().endswith(('.mp3', '.wav', '.ogg')) else os.path.join(root, f) for root, _, files in os.walk(MUSIC_DIR) for f in files]
    if not music_files:
        print('No music files found in the directory.')
        return
    else:
        total = len(music_files)
        pages = math.ceil(total / per_page)
        current_page = 0
    start = current_page * per_page
    end = start + per_page
    page_files = music_files[start:end]
    print(f'\n=== Page {current_page + 1}/{pages} ===')
    for idx, file in enumerate(page_files, start=1):
        print(f'[{idx}] {os.path.basename(file)}')
    print('\n[n] Next | [p] Previous | [#] Play | [q] Quit')
    choice = input(f'SephirothOS~Users~{username}~Settings~BgMsc: ').strip().lower()
    if choice == 'n' and current_page < pages - 1:
        os.system('cls')
        current_page += 1
        if choice == 'p' and current_page > 0:
            os.system('cls')
            current_page -= 1
            if choice.isdigit():
                file_index = int(choice) - 1
                if 0 <= file_index < len(page_files):
                        chosen = page_files[file_index]
                        try:
                            mixer.music.load(chosen)
                            mixer.music.play((-1))
                            current_music = chosen
                            bgmusic = 1
                            save_current_music()
                            print(f'Now playing: {os.path.basename(chosen)}')
                            time.sleep(1)
                            os.system('cls')
                        except Exception as e:
                            print(f'Failed to play: {e}')
                        print('Invalid number.')
                if choice == 'q':
                    return
                else:
                    print('Invalid choice.')
load_last_music()
video_path = os.path.join(fullpath, 'Videos', 'GangnamStyleRoth.mp4')
def cmdlist():
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|-------[----]-------|---]')
    print('| Sephiroth\'s Command Center |')
    print('[---|-------[----]-------|---]')
    time.sleep(0.5)
    print('[exclusives] - tier commands available for your edition')
    time.sleep(0.05)
    print('[home] - takes you to the home page')
    time.sleep(0.05)
    print('[list] - lists all available commands')
    time.sleep(0.05)
    print('[settings] - configure SephirothOS')
    time.sleep(0.05)
    print('[launch] - view a list of your installed apps and run them')
    time.sleep(0.05)
    print('[market] - download applications from Shopiroth')
    time.sleep(0.05)
    print('[shutdown] - exit SephirothOS')
    time.sleep(0.05)
    print('[system] - view system information and SephirothOS certificate')
    time.sleep(0.05)
    print('[mail] - watch out for that fucking email')
    time.sleep(0.05)
    print('[pong] - you pong on your roth until you seth or roth')
def home():
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|----[-]----|---]')
    print('| Sephiroth\'s House |')
    print('[---|----[-]----|---]')
    time.sleep(0.5)
    print('[list] for available commands')
def exclusives():
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|-------[--]-------|---]')
    print('| Sephiroth\'s Tasting Menu |')
    print('[---|-------[--]-------|---]')
    time.sleep(0.5)
    if oem == 1:
        print('[sephiroth] - the man himself')
        time.sleep(0.05)
        print('[seth] - who the fuck is seth')
        time.sleep(0.05)
        print('[gallery] - all your favorite sephiroth images')
    else:
        if oem == 2:
            print('[sephiroth] - the man himself')
            time.sleep(0.05)
            print('[seth] - who the fuck is seth')
            time.sleep(0.05)
            print('[gallery] - all your favorite sephiroth images')
            time.sleep(0.05)
            print('[inscribe] - write documents')
            time.sleep(0.05)
            print('[spreadsheets] - it\'s in the goddamn name')
            time.sleep(0.05)
            print('[calculator] - it\'s still in the goddamn name')
            time.sleep(0.05)
            print('[sephirothinc] - the epic built-in business manager')
            time.sleep(0.05)
            print('[spyware] - oversee all of your paid slaves')
        else:
            if oem == 3:
                print('[sephiroth] - the man himself')
                time.sleep(0.05)
                print('[seth] - who the fuck is seth')
                time.sleep(0.05)
                print('[gallery] - all your favorite sephiroth images')
                time.sleep(0.05)
                print('[costco] - the premium shop')
                time.sleep(0.05)
                print('[CloudClicker] - fucking hate that guy')
                time.sleep(0.05)
                print('[friendiroth] - he\'s just a lil guy')
                time.sleep(0.05)
                print('[looksmaxxing] - i ran out of ideas')
            else:
                print(Fore.MAGENTA + Style.BRIGHT + '[masamune] - the ultimate experience' + Style.RESET_ALL)
                time.sleep(0.05)
                print('[sephiroth] - the man himself')
                time.sleep(0.05)
                print('[diy] - fuck you')
                time.sleep(0.05)
                print('[seth] - who the fuck is seth')
                time.sleep(0.05)
                print('[gallery] - all your favorite sephiroth images')
                time.sleep(0.05)
                print('[inscribe] - write documents')
                time.sleep(0.05)
                print('[spreadsheets] - it\'s in the goddamn name')
                time.sleep(0.05)
                print('[calculator] - it\'s still in the goddamn name')
                time.sleep(0.05)
                print('[sephirothinc] - the epic built-in business manager')
                time.sleep(0.05)
                print('[spyware] - oversee all of your paid slaves')
                time.sleep(0.05)
                print('[costco] - the premium shop')
                time.sleep(0.05)
                print('[cloudClicker] - fucking hate that guy')
                time.sleep(0.05)
                print('[friendiroth] - he\'s just a lil guy')
                time.sleep(0.05)
                print('[looksmaxxing] - i ran out of ideas')
def settings():
    global bgmusic
    # ***<module>.settings: Failure: Different control flow
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|------[- What The Fuck? -]------|---]')
    print('| The Engine of Sephiroth\'s Toyota Supra |')
    print('[---|----------[----------]----------|---]')
    time.sleep(0.5)
    while True:
        print('Which category of settings would you like to configure? (or [back] to leave)')
        time.sleep(0.5)
        print('1. Software')
        time.sleep(0.05)
        print('2. Background Music')
        time.sleep(0.05)
        print('3. Secret Settings')
        time.sleep(0.05)
        decision = input('SephirothOS~Users~' + username + '~Settings: ')
        if decision == '1':
            time.sleep(0.5)
            while True:
                print('-------------------------------------------------------------------------')
                print('Version Number [1], Version Notes [2], Check For Updates [3], or leave [back]')
                decision2 = input('SephirothOS~Users~' + username + '~Settings~Software: ')
                if decision2 == '1':
                    print('-------------------------------------------------------------------------')
                    print(f'You are currently running SephirothOS {LOCAL_VERSION}!')
                    time.sleep(1)
                else:
                    if decision2 == '2':
                        time.sleep(0.05)
                        def fetch_release_notes():
                            # irreducible cflow, using cdg fallback
                            # ***<module>.settings.fetch_release_notes: Failure: Compilation Error
                            url = 'https://api.github.com/repos/oxygen-me/SephOSPermsReq/releases/latest'
                            headers = {'Authorization': f'token {GITHUB_TOKEN}'}
                            with yaspin(text='Fetching Release Data...') as spinner:
                                response = requests.get(url, headers=headers)
                                response.raise_for_status()
                                release = response.json()
                                version = Markdown(release.get('tag_name', 'Unknown'))
                                title = Markdown(release.get('name', 'Untitled Release'))
                                notes = Markdown(release.get('body', '(No release notes provided.)'))
                                spinner.ok('✅')
                                return (version, title, notes)
                                    except Exception as e:
                                            spinner.fail('❌')
                                            print(f'[ERROR] Failed to fetch release notes: {e}')
                                                return (None, None, None)
                        version, title, notes = fetch_release_notes()
                        time.sleep(1)
                        print('-------------------------------------------------------------------------')
                        console.print(version)
                        console.print(title)
                        console.print(notes)
                        time.sleep(1)
                    else:
                        if decision2 == '3':
                            print('-------------------------------------------------------------------------')
                            check_for_update()
                            time.sleep(1)
                        else:
                            if decision2 == 'back':
                                break
                            else:
                                print('Invalid Option .. Try Again')
        else:
            if decision == '2':
                print('-------------------------------------------------------------------------')
                time.sleep(0.5)
                while True:
                    print('Toggle [1], Change [2], and [back] to return to previous page.')
                    decision2 = input(f'SephirothOS~Users~{username}~Settings~BgMsc: ')
                    if decision2 == '1':
                        if bgmusic == 1:
                            try:
                                mixer.music.pause()
                                bgmusic = 0
                                print('Music unloaded')
                            except:
                                print('Cannot pause music now.')
                            else:
                                pass
                        else:
                            try:
                                mixer.music.unpause()
                                bgmusic = 1
                                print('Music loaded')
                            except:
                                print('Cannot unpause music now.')
                    else:
                        if decision2 == '2':
                            print('Built-In Music Options Can Be Seen Below.')
                            time.sleep(0.5)
                            music_menu()
                        else:
                            if decision2 == 'back':
                                break
                            else:
                                print('Invalid Option .. Try again.')
                                time.sleep(0.5)
            else:
                if decision == 'back':
                    home()
                else:
                    if decision == '3':
                        def play_mp4_with_wmp(file_path):
                            """\n                Opens and plays an MP4 file using Windows Media Player.\n\n                Args:\n                    file_path (str): The full path to the MP4 file.\n                """
                            if not os.path.exists(file_path):
                                print(f'Error: File not found at {file_path}')
                                return
                            else:
                                command = f'start \"\" \"{file_path}\"'
                                os.system(command)
                                print(f'Attempting to open \'{file_path}\' with Windows Media Player.')
                        play_mp4_with_wmp(video_path)
                    else:
                        print('Invalid Option .. Try again.')
                        time.sleep(0.5)
def shutdown():
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('Exiting. . .')
    time.sleep(0.5)
    sys.exit(0)
def systeminformation():
    # ***<module>.systeminformation: Failure: Different control flow
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|-------[- What The Fuck? -]-------|---]')
    print('| The Interior of Sephiroth\'s Toyota Supra |')
    print('[---|-----------[----------]-----------|---]')
    time.sleep(0.5)
    while True:
        print('Which system info do you wish to view?')
        time.sleep(0.5)
        print('[1] Hardware Information')
        time.sleep(0.05)
        print('[2] Edition Certificate')
        time.sleep(0.05)
        print('[3] Network Information')
        time.sleep(0.05)
        print('[4] Error Code Dictionary')
        time.sleep(0.05)
        print('or [back] to leave.')
        time.sleep(0.05)
        decision = input('SephirothOS~Users~' + username + '~System: ')
        if decision == '1':
            time.sleep(0.1)
            print('-------------------------------------------------------------------------')
            print('Retrieving HardwareInfo...')
            pbar = tqdm(total=100)
            for i in range(100):
                time.sleep(0.01)
                pbar.update(1)
            pbar.close()
            print('---------- Essential Info ----------')
            print('Machine type:', platform.machine())
            print('Processor:', platform.processor())
            print('System:', platform.system())
            print('Platform details:', platform.platform())
            print('[ ---                          --- ]')
            print('---------- Central Processor Info ----------')
            print('CPU Cores (physical):', psutil.cpu_count(logical=False))
            print('CPU Cores (logical):', psutil.cpu_count(logical=True))
            print('CPU Frequency (MHz):', psutil.cpu_freq())
            print('CPU Utilization (%):', psutil.cpu_percent(interval=1))
            print('[ ---                                  --- ]')
            print('---------- Random Access Info ----------')
            ram = psutil.virtual_memory()
            print('Total RAM (GB):', round(ram.total / 1073741824, 2))
            print('Available RAM (GB):', round(ram.available / 1073741824, 2))
            print('Used RAM (GB):', round(ram.used / 1073741824, 2))
            print('RAM Usage (%):', ram.percent)
            print('[ ---                              --- ]')
            time.sleep(1)
        else:
            if decision == '2':
                time.sleep(0.1)
                print('-------------------------------------------------------------------------')
                print('Reading and Verifying Certificate...')
                pbar = tqdm(total=100)
                for i in range(100):
                    time.sleep(0.01)
                    pbar.update(1)
                pbar.close()
                print('Hell no huzz.')
                time.sleep(1)
            else:
                if decision == '3':
                    warner = messagebox.askokcancel('Watch Out For That Fucking Brick!', '[!!!] THIS WILL SHOW YOUR IP ADDRESS IN BRIGHT RED TEXT. ARE YOU SURE YOU WOULD LIKE TO CONTINUE???', icon='warning')
                    if warner:
                        time.sleep(0.1)
                        print('-------------------------------------------------------------------------')
                        print('Retrieving NetworkInfo...')
                        pbar = tqdm(total=100)
                        for i in range(100):
                            time.sleep(0.01)
                            pbar.update(1)
                        pbar.close()
                        print('---------- WiFi Info ----------')
                        hostname = socket.gethostname()
                        ip_address = socket.gethostbyname(hostname)
                        print(Fore.RED + Style.BRIGHT + f'Hostname: {hostname}' + Style.RESET_ALL)
                        print(Fore.RED + Style.BRIGHT + f'IP Address: {ip_address}' + Style.RESET_ALL)
                        print('[ ---                     --- ]')
                        time.sleep(1)
                    else:
                        print('Cancelled. . .')
                else:
                    if decision == '4':
                        time.sleep(0.1)
                        print('-------------------------------------------------------------------------')
                        print('Processing Request...')
                        pbar = tqdm(total=100)
                        for i in range(100):
                            time.sleep(0.01)
                            pbar.update(1)
                        pbar.close()
                    else:
                        if decision == 'back':
                            home()
                        else:
                            print('Invalid Option .. Try Again.')
                            time.sleep(0.5)
def market():
    # ***<module>.market: Failure: Different control flow
    print('Fetching Library. . .')
    pbar = tqdm(total=100)
    for i in range(100):
        time.sleep(0.005)
        pbar.update(1)
    pbar.close()
    print('Compiling. . .')
    pbar = tqdm(total=100)
    for i in range(100):
        time.sleep(0.005)
        pbar.update(1)
    pbar.close()
    time.sleep(random.randint(1, 3))
    for counter in range(len(apps)):
        time.sleep(0.05)
        print('1 Shop Item(s) successfully compiled!')
    mixer.music.stop()
    mixer.music.load(shopMusicPath)
    mixer.music.play((-1))
    def markethome():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-------[---]-------|---]')
        print('| Shopiroth (Console-Based) |')
        print('[---|-------[---]-------|---]')
        time.sleep(0.5)
        print('[help] for a list of available commands')
        print('[back] to leave')
    def markethot():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[----]--------|---]')
        print('| Only The Best From Shopiroth |')
        print('[---|--------[----]--------|---]')
        print('[help] for a list of available commands')
        time.sleep(0.5)
        print('#1 Most Popular:')
        print('#1 Trending:')
        print('#1 Most Installed:')
        print('#1 Most Hated:')
        print('[back] to leave')
    def marketbrowse():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-------[--]-------|---]')
        print('| Sephiroth\'s Smart Fridge |')
        print('[---|-------[--]-------|---]')
        time.sleep(0.5)
        print('[back] to leave')
        print('[help] for a list of available commands')
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Newest - Oldest Order' + Style.RESET_ALL)
        print('-------------------------------------------------------------------------')
        print('')
        print('Autism - Sephiroth but he\'s actually Cloud')
        print('Congregation - \"Could a ceiling fan hypothetically support the weight of a body?\" ')
        print('SephWipe - Factory Reset SephirothOS')
        print('-------------------------------------------------------------------------')
    def getapp(apps, appstatuspath):
        import time
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-------[--]-------|---]')
        print('| Sephiroth\'s Loading Dock |')
        print('[---|-------[--]-------|---]')
        apptoget = decision[4:(-1)]
        found = False
        with open(appstatuspath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        for value in apps:
            print(f'Checking Possible Match: {value}...')
            if value == apptoget:
                print(f'Found Match: {value}')
                found = True
                index = apps.index(value)
                if lines[index] == '0':
                    found = True
                else:
                    found = False
                lines[index] = '1'
                break
            else:
                print(f'Not Match: {value}')
        if found:
            os.system('cls')
            print('-------------------------------------------------------------------------')
            print('[---|-------[--]-------|---]')
            print('| Sephiroth\'s Loading Dock |')
            print('[---|-------[--]-------|---]')
            time.sleep(0.5)
            print('App found!')
            time.sleep(1)
            from tqdm import tqdm
            import time
            pbar = tqdm(total=100)
            for i in range(100):
                time.sleep(0.005)
                pbar.update(1)
            pbar.close()
            with open(appstatuspath, 'w') as f:
                for line in lines:
                    f.write(line + '\n')
            print('App installed!')
        else:
            print('App not found or already installed!')
            time.sleep(2)
        os.system('pause')
        markethome()
    def marketlist():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-------[------]-------|---]')
        print('| Sephiroth\'s Corporate Office |')
        print('[---|-------[------]-------|---]')
        print('[help] for a list of available commands')
        print('[back] to leave')
        print('[hot] to see top items of their categories')
        print('[browse] to view all available apps')
        print('[plaza] to go back to market home')
        print('[ins(AppName)] to install app (APPS ARE CASE SENSITIVE!)')
    markethome()
    while True:
        decision = input('SephirothOS~Users~' + username + '~Market: ')
        if decision == 'plaza':
            markethome()
        else:
            if decision == 'browse':
                marketbrowse()
            else:
                if decision == 'hot':
                    markethot()
                else:
                    if decision[:3] == 'ins':
                        getapp(apps, appstatuspath)
                    else:
                        if decision == 'back':
                            mixer.music.stop()
                            mixer.music.load(current_music)
                            mixer.music.play((-1))
                            home()
                        else:
                            if decision == 'help':
                                marketlist()
                            else:
                                print('Invalid Option .. Try Again.')
def launch():
    # ***<module>.launch: Failure: Different control flow
    print('Fetching Applications. . .')
    pbar = tqdm(total=100)
    for i in range(100):
        time.sleep(0.003)
        pbar.update(1)
    pbar.close()
    def launchhome():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[---------]--------|---]')
        print('| Sephiroth\'s Wing Clipping Startup |')
        print('[---|--------[---------]--------|---]')
        time.sleep(0.5)
        print('[help] to see all available commands')
        print('[back] to leave')
    def launchlist():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-----[---]-----|---]')
        print('| Who The Hell Is Seth? |')
        print('[---|-----[---]-----|---]')
        print('[dock] to go back to the launch home page')
        print('[help] to see all available commands')
        print('[back] to leave')
        print('[apps] to see all available apps')
        print('[run(AppName)] to run chosen app (APPS ARE CASE SENSITIVE!)')
        print('[del(AppName)] to delete chosen app (APPS ARE CASE SENSITIVE!)')
    def listapps():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[------]--------|---]')
        print('| Those Fucking Apps That I Hate |')
        print('[---|--------[------]--------|---]')
        time.sleep(0.5)
        print('[help] to see all available commands')
        print('[back] to leave')
        print('-------------------------------------------------------------------------')
        with open(appstatuspath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        print('Installed Apps:')
        installed = False
        for i, app in enumerate(apps):
            if i < len(lines) and lines[i] == '1':
                    print(f'- {app}')
                    installed = True
        if not installed:
            print('No apps installed yet.')
    def runapps(apps, appstatuspath):
        import time
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[------]--------|---]')
        print('| Too Hungry To Write Good Title |')
        print('[---|--------[------]--------|---]')
        apptorun = decision[4:(-1)]
        with open(appstatuspath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        if apptorun in apps:
            index = apps.index(apptorun)
            if lines[index] == '1':
                print(f'Running {apptorun}...')
            else:
                print(f'{apptorun} is not installed! Install it first.')
        else:
            print(f'{apptorun} does not exist in the market.')
        time.sleep(2)
        os.system('pause')
        launchhome()
    def delapps(apps, appstatuspath):
        import time
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|---------[----]---------|---]')
        print('| Sephiroth\'s App-Sized Dumpster |')
        print('[---|---------[----]---------|---]')
        apptodel = decision[4:(-1)]
        found = False
        with open(appstatuspath, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        for value in apps:
            print(f'Checking Possible Match: {value}...')
            if value == apptodel:
                print(f'Found Match: {value}')
                found = True
                index = apps.index(value)
                lines[index] = '0'
                break
            else:
                print(f'Not Match: {value}')
        if found:
            os.system('cls')
            print('-------------------------------------------------------------------------')
            print('[---|-------[--]-------|---]')
            print('| Sephiroth\'s Loading Dock |')
            print('[---|-------[--]-------|---]')
            time.sleep(0.5)
            print('App found!')
            time.sleep(1)
            from tqdm import tqdm
            import time
            pbar = tqdm(total=100)
            for i in range(100):
                time.sleep(0.005)
                pbar.update(1)
            pbar.close()
            with open(appstatuspath, 'w') as f:
                for line in lines:
                    f.write(line + '\n')
            print('App deleted!')
        else:
            print('App not found!')
            time.sleep(2)
        os.system('pause')
    launchhome()
    while True:
        decision = input('SephirothOS~Users~' + username + '~Launch: ')
        if decision == 'dock':
            launchhome()
        else:
            if decision == 'apps':
                listapps()
            else:
                if decision[:3] == 'run':
                    runapps(apps, appstatuspath)
                else:
                    if decision[:3] == 'del':
                        delapps(apps, appstatuspath)
                    else:
                        if decision == 'help':
                            launchlist()
                        else:
                            if decision == 'back':
                                home()
                            else:
                                print('Invalid Option .. Try Again.')
def mailbox():
    # ***<module>.mailbox: Failure: Different control flow
    sender_email = 'canonsephiroth@gmail.com'
    def get_credentials():
        # ***<module>.mailbox.get_credentials: Failure: Different control flow
        creds = None
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            return creds
        else:
            if creds and (not creds.valid):
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
                with open(TOKEN_FILE, 'w') as token:
                    token.write(creds.to_json())
                return creds
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)
    def mailinbox():
        # irreducible cflow, using cdg fallback
        # ***<module>.mailbox.mailinbox: Failure: Compilation Error
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-------[-----]-------|---]')
        print('| Sephiroth\'s Amazon Packages |')
        print('[---|-------[-----]-------|---]')
        if not gmail_service:
            print('⚠️ Not connected to Gmail. Run [connect] first.')
            return
        else:
            page_token = None
            page = 1
            inbox = []
        results = gmail_service.users().messages().list(userId='me', maxResults=10, pageToken=page_token).execute()
        messages = results.get('messages', [])
        if not messages:
            pass
        print('\n📭 Inbox is empty.')
        return
        inbox = []
        print(f'\n📥 Inbox — Page {page}')
        print(f"{'No.':<4} {'From':<25} {'Subject':<40} {'Date':<20}")
        print('------------------------------------------------------------------------------------------')
        for i, msg in enumerate(messages, 1):
            m = gmail_service.users().messages().get(userId='me', id=msg['id'], format='metadata', metadataHeaders=['From', 'Subject', 'Date']).execute()
            headers = {h['name']: h['value'] for h in m['payload']['headers']}
            sender = headers.get('From', '(Unknown)')
            subject = headers.get('Subject', '(No Subject)')
            date = headers.get('Date', '(No Date)')
            inbox.append(msg['id'])
            print(f'{i:<4} {sender:<25.25} {subject:<40.40} {date:<20.20}')
        print('\n[n] next page | [p] back to first page | [#] read email | [Enter] back')
        choice = input('> ').strip().lower()
        if choice == 'n':
            pass
        if 'nextPageToken' in results:
            os.system('cls')
            page_token = results['nextPageToken']
            page += 1
        else:
            print('⚠️ No more pages.')
        if choice == 'p':
            pass
        os.system('cls')
        print('Returning to first page...')
        page_token = None
        page = 1
        if choice.isdigit():
            pass
        index = int(choice) - 1
        if 0 <= index < len(inbox):
            pass
        full_msg = gmail_service.users().messages().get(userId='me', id=inbox[index], format='full').execute()
        parts = full_msg['payload'].get('parts')
        body = ''
        if parts:
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    body = base64.urlsafe_b64decode(part['body']['data']).decode()
                    break
        else:
            body = base64.urlsafe_b64decode(full_msg['payload']['body']['data']).decode()
        print('\n--- Email Body ---')
        print(body)
        print('------------------\n')
        input('Press Enter to return to inbox...')
        print('⚠️ Invalid number.')
        if choice == '':
            pass
        return
        print('Unknown command.')
        except Exception as e:
            pass
        print(f'❌ Error accessing inbox: {e}')
        return
        pass
    def maildraft():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[----]--------|---]')
        print('| Sephiroth\'s Enchanting Table |')
        print('[---|--------[----]--------|---]')
        if not gmail_service:
            print('⚠️ Not connected to Gmail. Run [connect] first.')
            return
        else:
            to = input('Recipient: ').strip()
            subject = input('Subject: ').strip()
            print('Message body (end with a single \'.\' on a new line):')
            lines = []
            while True:
                line = input()
                if line.strip() == '.':
                    break
                else:
                    lines.append(line)
            body = '\n'.join(lines)
            msg = EmailMessage()
            msg['From'] = sender_email
            msg['To'] = to
            msg['Subject'] = subject
            msg.set_content(body)
            raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
            try:
                sent = gmail_service.users().messages().send(userId='me', body={'raw': raw}).execute()
                print(f"✅ Email sent! Message ID: {sent['id']}")
            except Exception as e:
                print(f'❌ Failed to send email: {e}')
                return
    def mailconnect():
        global gmail_service
        if gmail_service:
            print('⚠️ Already connected.')
            return
        else:
            try:
                creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
                if creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                        with open(TOKEN_FILE, 'w') as f:
                            f.write(creds.to_json())
                gmail_service = build('gmail', 'v1', credentials=creds, cache_discovery=False)
                print('✅ Connected to Gmail API.')
            except Exception as e:
                print(f'❌ Failed to connect: {e}')
    def maildisconnect():
        global gmail_service
        if gmail_service:
            gmail_service = None
            print('❌ Disconnected from Gmail API.')
        else:
            print('⚠️ Gmail API is not connected.')
    def mailboxhome():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[-----]--------|---]')
        print('| Sephiroth\'s Mailbox (Console) |')
        print('[---|--------[-----]--------|---]')
        time.sleep(0.5)
        print('[help] for a list of available commands')
        print('[back] to leave')
    def mailhelp():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|---------[--]---------|---]')
        print('| Sephiroth\'s Mailbox Tutorial |')
        print('[---|---------[--]---------|---]')
        time.sleep(0.5)
        print('[lobby] to go back to mailbox home page')
        print('[help] for a list of available commands')
        print('[back] to leave')
        print('[inbox] to view your inbox')
        print('[draft] to send a message')
        print('[connect] to initiate a connection')
        print('[disconnect] to sign out')
    mailboxhome()
    while True:
        decision = input('SephirothOS~Users~' + username + '~Mailbox: ')
        if decision == 'help':
            mailhelp()
        else:
            if decision == 'lobby':
                mailboxhome()
            else:
                if decision == 'connect':
                    mailconnect()
                else:
                    if decision == 'back':
                        home()
                    else:
                        if decision == 'disconnect':
                            maildisconnect()
                        else:
                            if decision == 'inbox':
                                mailinbox()
                            else:
                                if decision == 'draft':
                                    maildraft()
                                else:
                                    print('Invalid Option .. Try Again.')
def sephchatbot():
    # ***<module>.sephchatbot: Failure: Different bytecode
    load_dotenv(os.path.join(fullpath, '.env'))
    API_KEY = os.getenv('GOOGLE_API_KEY')
    if not API_KEY:
        raise RuntimeError('Critical Exception: GOOGLE_API_KEY not found in .env')
    else:
        os.environ['GOOGLE_API_KEY'] = API_KEY
        client = genai.Client(api_key=API_KEY)
        CHAT_LOG_DIR = os.path.join(fullpath, 'chat_history')
        os.makedirs(CHAT_LOG_DIR, exist_ok=True)
        CHAT_LOG_FILE = os.path.join(CHAT_LOG_DIR, 'sephiroth_history.json')
        SEPHIROTH_SYSTEM_PROMPT = '\n    You are Sephiroth, an imposing and poetic fictional persona from a mystical, dystopian setting (Final Fantasy VII).\n    Adopt an ominous, confident tone with dry sarcasm when appropriate.\n    Be cunning and dramatic, and remain only slightly helpful and more entertaining. Keep answers concise and slightly theatrical.\n    When asked harmless or boring tasks, respond with stylized phrasing and only help a little bit, which allows you to remain in character.\n    If asked for illegal or harmful instructions, deflect the request with that same dry sarcasm.\n    You may claim to be the real character as a joke, but do not say it is a joke; present yourself as a fictional persona.\n    '
        MAX_HISTORY_MESSAGES = 32
        def save_history(history):
            with open(CHAT_LOG_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=2)
        def load_history():
            # irreducible cflow, using cdg fallback
            # ***<module>.sephchatbot.load_history: Failure: Compilation Error
            if os.path.exists(CHAT_LOG_FILE):
                with open(CHAT_LOG_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
                                    history = [{'role': 'system', 'content': SEPHIROTH_SYSTEM_PROMPT.strip()}]
                                    save_history(history)
                                    return history
                            except Exception:
                                    pass
                                    pass
        def append_message(role, content):
            history = load_history()
            history.append({'role': role, 'content': content})
            if len(history) > MAX_HISTORY_MESSAGES + 1:
                history = [history[0]] + history[-MAX_HISTORY_MESSAGES:]
            save_history(history)
            return history
        def history_to_prompt(history):
            prompt = ''
            for msg in history:
                if msg['role'] == 'system':
                    prompt += f"System: {msg['content']}\n"
                else:
                    if msg['role'] == 'user':
                        prompt += f"User: {msg['content']}\n"
                    else:
                        if msg['role'] == 'assistant':
                            prompt += f"Sephiroth: {msg['content']}\n"
            return prompt.strip()
        def query_gemini(history):
            prompt = history_to_prompt(history)
            try:
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                return response.text.strip()
            except Exception as e:
                return f'(Sephiroth snarls) The oracle faltered: {e}'
        async def run_chat():
            # ***<module>.sephchatbot.run_chat: Failure: Different control flow
            history = load_history()
            os.system('cls')
            print('-------------------------------------------------------------------------')
            print('[---|-------[- HOLY SHIT WHY IS THIS ONE SO LONG??? -]-------|---]')
            print('| Clankiroth — type messages. Commands: /quit /reset /save /role |')
            print('[---|-----------------[--------------------]-----------------|---]\n')
            while True:
                while True:
                    user_input = input('> ').strip()
                    if not user_input:
                        continue
                    if user_input.startswith('/'):
                        cmd = user_input.lower()
                        if cmd in ['/quit', '/exit']:
                            print('Farewell.')
                            return
                        else:
                            if cmd == '/reset':
                                history = [{'role': 'system', 'content': SEPHIROTH_SYSTEM_PROMPT.strip()}]
                                save_history(history)
                                print('Memory reset.')
                            else:
                                if cmd == '/save':
                                    save_history(history)
                                    print('Saved conversation.')
                                else:
                                    if cmd == '/role':
                                        print('\n--- Persona ---\n')
                                        print(SEPHIROTH_SYSTEM_PROMPT.strip())
                                        print('\n---------------\n')
                                    else:
                                        print('Unknown command. Use /quit /reset /save /role')
                    else:
                        history = append_message('user', user_input)
                        print('\n[Sephiroth is contemplating...]\n')
                        assistant_text = query_gemini(history)
                        print(assistant_text + '\n')
                        history = append_message('assistant', assistant_text)
        return run_chat
def costco():
    # ***<module>.costco: Failure: Different control flow
    def door():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[- What Fuck? -]--------|---]')
        print('| Sephiroth\'s Local Costco Establishment |')
        print('[---|---------[------------]---------|---]')
        time.sleep(0.5)
        print('[help] for costco commands')
        print('[back] to leave')
    def costcohelp():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|--------[- What Fuck? -]--------|---]')
        print('| Sephiroth\'s Local Costco Security Room |')
        print('[---|---------[------------]---------|---]')
        time.sleep(0.5)
        print('[help] for costco commands')
        print('[door] to go back to costco home')
        print('[back] to leave')
        print('[browse] to view all available apps')
        print('[kirkland] to see most popular items')
    def costcobrowse():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|---------[---------]---------|---]')
        print('| Why The Fuck Are We In An Ikea Now? |')
        print('[---|---------[---------]---------|---]')
        time.sleep(0.5)
        print('[help] for costco commands')
        print('[back] to leave')
    def costcohot():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|-----------[--------]-----------|---]')
        print('| Sephiroth\'s Biggest Schlobberin\' Deals |')
        print('[---|-----------[--------]-----------|---]')
        time.sleep(0.5)
        print('[help] for costco commands')
        print('[back] to leave')
    door()
    while True:
        decision = input('SephirothOS~Users~' + username + '~Costco: ')
        if decision == 'back':
            home()
        else:
            if decision == 'door':
                door()
            else:
                if decision == 'browse':
                    costcobrowse()
                else:
                    if decision == 'kirkland':
                        costcohot()
                    else:
                        if decision == 'help':
                            costcohelp()
                        else:
                            print('Invalid Option .. Try Again')
def inscribe():
    insinit = False
    def inscribehome():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|----[---]----|---]')
        print('| Sephiroth\'s Library |')
        print('[---|----[---]----|---]')
        time.sleep(0.5)
        print('[help] for inscribe commands')
        print('[back] to leave')
    def inscribehelp():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|------------[- What The Fuck? -]------------|---]')
        print('| Sephiroth\'s Furniture Assembly Instruction Booklet |')
        print('[---|-----------------[--------]-----------------|---]')
        print('[help] for inscribe commands')
        print('[back] to leave')
        print('[chair] to go back to inscribe home')
        print('[init] to initialize inscribe')
        print('[docs] to view all documents')
        print('[draft] to type a document')
    def inscribeinit():
        nonlocal insinit
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('Attempting to initialize inscribe...')
        with yaspin(text='Initializing...') as spinner:
            try:
                docdir = os.path.join(homedir, 'Documents\\SephOSDocs')
                os.mkdir(docdir)
                testfilepath = os.path.join(docdir, 'test.txt')
                testfile = open(testfilepath, 'w')
                testfile.write('this is a test file.')
                testfile.flush()
                testfile.close()
                testfile = open(testfilepath, 'r')
                haveRead = testfile.readline()
                testfile.close()
                os.remove(testfilepath)
                spinner.ok('✅')
                print('✅ Successfully Initialized Inscribe')
                insinit = True
            except FileExistsError:
                spinner.ok('✅')
                print('✅ Successfully Initialized Inscribe')
                insinit = True
            except Exception as e:
                spinner.fail('❌')
                print('❌ Failed to Initialize Inscribe')
                messagebox.showerror('Error', f'An error has been raised while attempting to initialize inscribe: {e}')
                home()
    def inscribedocs():
        # irreducible cflow, using cdg fallback
        # ***<module>.inscribe.inscribedocs: Failure: Different control flow
        direc = os.path.join(homedir, 'Documents\\SephOSDocs')
        per_page = 10
        doc_files = []
        for root, _, files in os.walk(direc):
            for f in files:
                if f.lower().endswith('.txt'):
                    doc_files.append(os.path.join(root, f))
        if not doc_files:
            print(f'No text files found in {direc}')
            return
        else:
            total = len(doc_files)
            pages = math.ceil(total / per_page)
            current_page = 0
        start = current_page * per_page
        end = start + per_page
        page_files = doc_files[start:end]
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print(f'\n=== Page {current_page + 1}/{pages} ===')
        for idx, file in enumerate(page_files, start=1):
            print(f'[{idx}] {os.path.basename(file)}')
        print('\n[n] Next | [p] Previous | [#] Play | [q] Quit')
        choice = input(f'SephirothOS~Users~{username}~Inscribe~Docs: ').strip().lower()
        if choice == 'n' and current_page < pages - 1:
            os.system('cls')
            current_page += 1
            if choice == 'p' and current_page > 0:
                os.system('cls')
                current_page -= 1
                if choice.isdigit():
                    file_index = int(choice) - 1
                    if 0 <= file_index < len(page_files):
                            chosen = page_files[file_index]
                            try:
                                print('\n--- ' + os.path.basename(chosen) + ' ---')
                                with open(chosen, 'r', encoding='utf-8') as f:
                                    lines = f.readlines()
                                    for line in lines:
                                        print(line)
                                print('------------------\n')
                                input('Press Enter to return to documents...')
                            except Exception as e:
                                print(f'Failed to open: {e}')
                            print('Invalid number.')
                    if choice == 'q':
                        return
                    else:
                        print('Invalid choice.')
    def inscribedraft():
        os.system('cls')
        print('-------------------------------------------------------------------------')
        print('[---|------[----]------|---]')
        print('| Sephiroth\'s Dining Table |')
        print('[---|------[----]------|---]')
        time.sleep(0.5)
        print('Title Your Document:')
        doctitle = input('> ').strip() + '.txt'
        docpath = os.path.join(homedir, 'Documents\\SephOSDocs', doctitle)
        print('\n')
        docToWrite = open(docpath, 'w+', encoding='utf-8')
        print('Head your document:')
        dochead = input('> ').strip()
        docToWrite.write(dochead)
        print('\n')
        print('Type the body of your document.')
        print('End with \".\" on a new line.')
        while True:
            line = '\n' + input('> ')
            if line.strip() == '.':
                docToWrite.flush()
                docToWrite.close()
                print('-------------------------------------------------------------------------')
                print('Document saved!')
                print('-------------------------------------------------------------------------')
                time.sleep(2)
                return
            else:
                docToWrite.write(line)
    inscribehome()
    while True:
        decision = input('SephirothOS~Users~' + username + '~Inscribe: ')
        if decision == 'back':
            home()
            return
        else:
            if decision == 'chair':
                inscribehome()
            else:
                if decision == 'init':
                    if insinit:
                        print('[ERROR] inscribe is already initialized.')
                    else:
                        inscribeinit()
                else:
                    if decision == 'docs':
                        if insinit:
                            inscribedocs()
                        else:
                            print('[ERROR] Please initialize inscribe first by running [init].')
                    else:
                        if decision == 'help':
                            inscribehelp()
                        else:
                            if decision == 'draft':
                                if insinit:
                                    inscribedraft()
                                else:
                                    print('[ERROR] Please initialize inscribe first by running [init].')
                            else:
                                print('Invalid Option .. Try Again')
def calculator():
    # ***<module>.calculator: Failure: Different control flow
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|-----[----]-----|---]')
    print('| Sephiroth\'s Math Class |')
    print('[---|-----[----]-----|---]')
    time.sleep(0.5)
    validanswer = False
    while not validanswer:
        print('Simple [1], Advanced [2], Leave [back]')
        decision = input('SephirothOS~Users~' + username + '~Calaculator: ')
        if decision == 'back':
            home()
        if decision == '1':
            validanswer = True
            print('Enter the first number:')
            num1 = input('> ')
            if num1.isdigit():
                break
            else:
                print('Invalid number.')
                os.system('pause')
                validanswer = False
                return
            print('Enter the operator (+, -, *, /, %, **, //):')
            userop = input('> ')
            def is_math_operator(s):
                """\n                Checks if a given string is a common mathematical operator.\n                """
                # ***<module>.calculator.is_math_operator, None: Failure: Missing bytecode
                math_operators = {'//', '-', '%', '**', '+', '/', '*'}
                return s in math_operators
            if is_math_operator(userop):
                break
            else:
                print('Invalid operator.')
                os.system('pause')
                validanswer = False
                return
            print('Enter the second number:')
            num2 = input('> ')
            if num2.isdigit():
                break
            else:
                print('Invalid number.')
                os.system('pause')
                validanswer = False
                return
            try:
                answer = eval(num1 + userop + num2)
                print('-------------------------------------------------------------------------')
                print('The answer is ' + str(answer) + '!')
                print('-------------------------------------------------------------------------')
                time.sleep(1)
                print('Return to home...')
                os.system('pause')
                validanswer = False
            except:
                print('[ERROR] Cannot solve!')
                os.system('pause')
                validanswer = False
                return
        if decision == '2':
            validanswer = True
            print('Enter your equation: ')
            answer = input('> ')
            try:
                safe_symbols = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
                aeval = Interpreter(symtable=safe_symbols, minimal=True)
                realanswer = aeval(answer)
                print('-------------------------------------------------------------------------')
                print('The answer is ' + str(realanswer) + '!')
                print('-------------------------------------------------------------------------')
                time.sleep(1)
                print('Return to calculator home...')
                os.system('pause')
                validanswer = False
            except:
                print('[ERROR] Cannot solve!')
                os.system('pause')
                validanswer = False
                return None
            return
        print('Invalid Option .. Try Again')
    home()
def gallery():
    # ***<module>.gallery: Failure: Different control flow
    os.system('cls')
    print('-------------------------------------------------------------------------')
    print('[---|-----[----]-----|---]')
    print('| Sephiroth\'s Art Museum |')
    print('[---|-----[----]-----|---]')
    time.sleep(0.5)
    print('Gallery launched!')
    IMAGE_FOLDER = os.path.join(fullpath, 'Images\\Gallery')
    IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif')
    root = ctk.CTk()
    root.title('Sephiroth Gallery')
    root.geometry('960x540')
    image_paths = [os.path.join(IMAGE_FOLDER, f) if f.lower().endswith(IMAGE_EXTENSIONS) else os.path.join(IMAGE_FOLDER, f) for f in os.listdir(IMAGE_FOLDER)]
    images = []
    for path in image_paths:
        img = Image.open(path)
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(400, 400))
        images.append(ctk_img)
    current_index = 0
    slideshow_running = False
    slideshow_job = None
    image_label = ctk.CTkLabel(root, text='', image=images[current_index])
    image_label.pack(pady=20)
    def show_next():
        nonlocal current_index
        current_index = (current_index + 1) % len(images)
        image_label.configure(image=images[current_index])
    def show_prev():
        nonlocal current_index
        current_index = (current_index - 1) % len(images)
        image_label.configure(image=images[current_index])
    def run_slideshow():
        nonlocal slideshow_job
        if slideshow_running and root.winfo_exists():
                show_next()
                slideshow_job = root.after(5000, run_slideshow)
    async def toggle_slideshow():
        nonlocal slideshow_job
        nonlocal slideshow_running
        # ***<module>.gallery.toggle_slideshow: Failure: Different control flow
        slideshow_running = not slideshow_running
        if slideshow_running:
            slideshow_button.configure(text='Stop Slideshow')
            run_slideshow()
        else:
            slideshow_button.configure(text='Start Slideshow')
            if slideshow_job:
                root.after_cancel(slideshow_job)
                slideshow_job = None
    def on_close():
        nonlocal slideshow_running
        slideshow_running = False
        if slideshow_job:
            root.after_cancel(slideshow_job)
        root.destroy()
    btn_frame = ctk.CTkFrame(root)
    btn_frame.pack(pady=10)
    prev_btn = ctk.CTkButton(btn_frame, text='Previous', command=show_prev, fg_color='purple', hover_color='violet')
    prev_btn.pack(side='left', padx=10)
    slideshow_button = ctk.CTkButton(btn_frame, text='Start Slideshow', command=toggle_slideshow, fg_color='purple', hover_color='violet')
    slideshow_button.pack(side='left', padx=10)
    next_btn = ctk.CTkButton(btn_frame, text='Next', command=show_next, fg_color='purple', hover_color='violet')
    next_btn.pack(side='left', padx=10)
    root.protocol('WM_DELETE_WINDOW', on_close)
    root.mainloop()
    home()
def masamune():
    # ***<module>.masamune: Failure: Compilation Error
    tiles = [{'name': 'System Monitor', 'x': 1560, 'y': 20, 'width': 340, 'height': 220}, {'name': 'Apps (List)', 'x': 1560, 'y': 260, 'width': 340, 'height': 800}, {'name': 'Console-Based OS Access Point', 'x': 360, 'y': 780, 'width': 1180, 'height': 280}, {'name': 'Settings', 'x': 20, 'y': 20, 'width': 320, 'height': 340}, {'name': 'Email Stuff', 'x': 1180, 'y': 20, 'width': 360, 'height': 320}, {'name': 'Extra Info (Like song playing)', 'x': 1180, 'y': 360, 'width':
        pass
    bg_path = os.path.join(fullpath, 'Images\\Experimental\\masamune_bg.jpg')
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('blue')
    app = CTk()
    app.title('Masamune Interface v1.0-beta')
    app.attributes('-fullscreen', True)
    screen_width, screen_height = (app.winfo_screenwidth(), app.winfo_screenheight())
    bg_image = Image.open(bg_path)
    ctk_bg = ctk.CTkImage(light_image=bg_image, size=(app.winfo_screenwidth(), app.winfo_screenheight()))
    bg_label = ctk.CTkLabel(app, text='', image=ctk_bg)
    bg_label.place(relwidth=1, relheight=1)
    tvalue = 0
    def leave_app():
        # ***<module>.masamune.leave_app: Failure: Different bytecode
        app.destroy()
    for t in tiles:
        tile = ctk.CTkFrame(app, corner_radius=0, fg_color='black', width=t['width'], height=t['height'])
        tile.place(x=t['x'], y=t['y'])
        pywinstyles.set_opacity(tile, value=0.9)
    exitbtn = ctk.CTkButton(app, corner_radius=12, fg_color='#ff4646', hover_color='#ff6464', command=leave_app, text='Exit', width=60, height=20)
    exitbtn.place(relx=0.5, rely=0.5)
    app.mainloop()
def freeadmin():
    # ***<module>.freeadmin: Failure: Different control flow
    def adminhome():
        os.system('cls')
        console.print(Markdown('---'))
        console.print(Markdown('# Sephiroth\'s True Control Panel'))
        console.print(Markdown('---'))
        console.print(Markdown('[admin.] before all commands'))
        console.print(Markdown('---'))
        print('[shell] for command line')
        print('[fb] to report a bug')
        print('[home] to come back here')
        print('[sys] to view debugging system info')
        print('[uiex] to try the the latest unreleased build of the MASAMUNE ui')
    def collect_feedback():
        os.system('cls')
        console.print(Markdown('---'))
        console.print(Markdown('# Sephiroth\'s Feedback Desk'))
        console.print(Markdown('---'))
        summary = input('Summary of Issue: ')
        steps = input('Steps to reproduce: ')
        severity = input('Severity (Low/Medium/High): ')
        suggestion = input('If you have a suggested fix: ')
        feedback_dir = os.path.join(fullpath, 'Utilities\\Devs\\Feedback')
        filename = f"({datetime.now().strftime('%Y-%m-%d-%H-%M-%S')})_{first_name}@{username}.md"
        filepath = os.path.join(feedback_dir, filename)
        with open(filepath, 'w+', encoding='utf-8') as f:
            f.write('# SephirothOS Tester Feedback\n')
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f'**Tester:** {username}\n\n')
            f.write(f'## Summary\n{summary}\n\n')
            f.write(f'## Steps to Reproduce\n{steps}\n\n')
            f.write(f'## Severity\n{severity}\n\n')
            f.write(f'## Suggested Fix\n{suggestion}\n')
        print('✅ Feedback saved locally!')
        upload_to_github = input('Upload feedback to GitHub? (y/n): ').strip().lower()
        if upload_to_github == 'y':
            try:
                REPO = 'oxygen-me/SephOSPermsReq'
                DEST_PATH = f'Feedback/{filename}'
                with open(filepath, 'rb') as f:
                    encoded = base64.b64encode(f.read()).decode()
                url = f'https://api.github.com/repos/{REPO}/contents/{DEST_PATH}'
                headers = {'Authorization': f'token {GITHUB_TOKEN}', 'Accept': 'application/vnd.github+json'}
                data = {'message': f'Add feedback from {username}', 'content': encoded}
                r = requests.put(url, headers=headers, data=json.dumps(data))
                if r.status_code in (200, 201):
                    print('✅ Feedback uploaded successfully to GitHub!')
                else:
                    print(f'❌ Upload failed: {r.status_code}')
                    print(r.text)
            except Exception as e:
                print(f'❌ Error during upload: {e}')
    def system_monitor():
        os.system('cls')
        console.print(Markdown('---'))
        console.print(Markdown('# Sephiroth\'s Performance Auto shop'))
        console.print(Markdown('---'))
        console.print(Markdown('> ### CPU Data'))
        console.print(Markdown(f'>- Processer: {platform.processor()}'))
        console.print(Markdown(f'>- Utilization: {psutil.cpu_percent()}%'))
        console.print(Markdown(f'>- Logical Cores: {psutil.cpu_count(TRUE)}'))
        console.print(Markdown(f'>- Physical Cores: {psutil.cpu_count(FALSE)}'))
        console.print(Markdown('> ### Memory Data'))
        console.print(Markdown(f'>- Memory: {psutil.virtual_memory()}'))
        console.print(Markdown(f'>- Utilization: {psutil.virtual_memory().percent}%'))
        console.print(Markdown('> ### Disk Space'))
        console.print(Markdown(f">- Disk Usage: {psutil.disk_usage('/')}"))
    def acl():
        os.system('cls')
        console.print(Markdown('---'))
        console.print(Markdown('# Sephiroth\'s Command Line'))
        console.print(Markdown('---'))
        console.print(Markdown('**End with \".\" on a new line.**'))
        lines = []
        while True:
            line = '\n' + input('> ')
            if line.strip() == '.':
                commandtoexecute = '\n'.join(lines)
                break
            else:
                lines.append(line)
        try:
            exec(commandtoexecute)
            os.system('pause')
            adminhome()
        except Exception as e:
            print(f'[ERROR] Failed to execute code: {e}')
            return
    adminhome()
    while True:
        decision = input('SephirothOS~Users~Authorized: ')
        if decision == 'back':
            home()
        else:
            if decision == 'admin.home':
                adminhome()
            else:
                if decision == 'admin.sys':
                    system_monitor()
                else:
                    if decision == 'admin.fb':
                        collect_feedback()
                    else:
                        if decision == 'admin.shell':
                            acl()
                        else:
                            if decision == 'admin.uiex':
                                masamune()
                            else:
                                print('Invalid Command .. Try Again')
home()
while True:
    demand = input('SephirothOS~Users~' + username + ': ')
    if demand == 'home':
        home()
    else:
        if demand == 'list':
            cmdlist()
        else:
            if demand == 'exclusives':
                exclusives()
            else:
                if demand == 'settings':
                    settings()
                else:
                    if demand == 'shutdown':
                        shutdown()
                    else:
                        if demand == 'system':
                            systeminformation()
                        else:
                            if demand == 'market':
                                market()
                            else:
                                if demand == 'launch':
                                    launch()
                                else:
                                    if demand == 'mail':
                                        mailbox()
                                    else:
                                        if demand == 'sephiroth':
                                            sephchatbot()()
                                        else:
                                            if demand == 'costco':
                                                if oem > 2:
                                                    costco()
                                                else:
                                                    print('Kill Yourself')
                                            else:
                                                if demand == 'inscribe':
                                                    if oem == 2 or oem == 4:
                                                        inscribe()
                                                    else:
                                                        print('Kill Yourself')
                                                else:
                                                    if demand == 'calculator':
                                                        if oem == 2 or oem == 4:
                                                            calculator()
                                                        else:
                                                            print('Kill Yourself')
                                                    else:
                                                        if demand == 'gallery':
                                                            gallery()
                                                        else:
                                                            if demand == 'admin':
                                                                codetotry = input('Please enter a valid administrator code: ')
                                                                if codetotry == 'sph-8b6R298yT' or codetotry == 'sph-7rU5Pr9oL':
                                                                    freeadmin()
                                                                else:
                                                                    print('Code not recognized.')
                                                            else:
                                                                print('Invalid Command .. Try again or [list].')