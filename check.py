import subprocess
import sys

def check_library():
    print("Start checking important library to run a program...")

    # check discord.py
    print("Checking discord.py...")
    try:
        import discord
    except ImportError:
        print("Discord.py not found.")
        print("Run install command : -m pip install discord.py")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
        print("Discord.py install complete!")

    # check pytube
    print("Checking pytube...")
    try:
        import pytube
    except ImportError:
        print("Pytube not found.")
        print("Run install command : -m pip install pytube")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pytube'])
        print("Pytube install complete!")
    finally:
        import pytube

    # check pytube
    print("Checking giphy_client...")
    try:
        import giphy_client
    except ImportError:
        print("giphy_client not found.")
        print("Run install command : -m pip install giphy_client")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'giphy_client'])
        print("giphy_client install complete!")
    finally:
        import giphy_client