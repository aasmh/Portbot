import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

BOT_TOKEN = "MTA2MDYxMTI5MDM3ODI4OTE4NA.G0zNa4.uF_YwDi-nKVMmiSjsn7cWvKaVghSPD7a4nnQ54"
CHANNEL_ID = 1049759266245980212


num = 0

    

def getinport():
    # Set the URL of the website
    url = 'http://spsonlinealex.apa.gov.eg/SPS-web/faces/harbor/inquiries/inportships/SearchInPortShipsOnline.xhtml'
    downdir = "/home/mod/desktop/downloads/existing"

    # Start a web browser and navigate to the website
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downdir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    button = driver.find_element(By.ID, 'searchForm:dataTableId:j_idt14')
    button.click()
    driver.implicitly_wait(3000)
    time.sleep(2)
    driver.quit()

def chnme(number):
    os.chdir('/home/mod/desktop/downloads/existing')
    os.rename('tableData.xls',f'existing{number}.xls')
    os.chdir('/home/mod/desktop')

def getdepart():
    url = 'http://spsonlinealex.apa.gov.eg/SPS-web/faces/harbor/inquiries/departureships/SearchDepartureShipsOnline.xhtml'
    downdir = "/home/mod/desktop/downloads/departing"
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": downdir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    button = driver.find_element(By.ID, 'searchForm:dataTableId:j_idt14')
    button.click()
    driver.implicitly_wait(3000)
    time.sleep(2)
    driver.quit()

def chnmd(number):
    os.chdir('/home/mod/desktop/downloads/departing')
    os.rename('tableData.xls',f'departing{number}.xls')
    os.chdir('/home/mod/desktop')

def addone(number):
    file = open('/home/mod/desktop/file.txt','w')
    file.write(str(number))
    file.close()

def readone():
    global num
    file = open('/home/mod/desktop/file.txt','r')
    content = file.read()
    file.close()


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    #print("Hello! Study bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    


@tasks.loop(hours=24)
async def my_task():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        readone()
        getinport()
        getdepart()
        time.sleep(2)
        chnme(num)
        chnmd(num)
        addone(num)
        await channel.send("", file=discord.File(f'/home/mod/desktop/downloads/existing/existing{num}.xls'))
        await channel.send("", file=discord.File(f'/home/mod/desktop/downloads/departing/departing{num}.xls'))
    except Exception as e:
        await channel.send(f"An error occured: {e}")


@tasks.loop(hours=24)
async def break_reminder():

    # Ignore the first execution of this command.
    # if break_reminder.current_loop == 0:
         return
    
@bot.command()
async def ping(ctx):
    
    await ctx.send(f"Server is online.")

@bot.command()
async def turnoff(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Port Bot is shutting down now")
    exit()

bot.run(BOT_TOKEN)
