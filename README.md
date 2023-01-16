# Portbot
A Discord bot that automatically fetches the port of alexandria's data everyday and pushes that info to a discord server



#### How does it work??


The getinport and getdepart functions click on the excel file so the file downloads.
### chrome options

--headless means it emulates the opening of chrome which decreases overhead and makes it quicker
##
time.sleep to allow time for the file to download
driver.quit for the window to close



chnmx --->>> change name of existing or departing in port file 
##
changes dir to the download dir then looks for the file tabledata(which is automatically named when downloaded from the port's website.)

Renaming the file into the current number using a global var set above called num

Changes dir back to reset the current working dir 

addone opens the file.txt to remove the current number and write a new number.

readone opens the txt file to read the current number and adds one to it.

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) ### sets the command prefix that the bot listens to 

##the loop

the loop is set to work every 24 hours

it's incased in a try catch block to check for errors, if any are thrown the exception is then sent over discord to notify someone of said error and get it fixed.

readone reads the number
then gets the files from inport and departing
sleeps for 2 seconds to allow for pipelining

proceeds by changing the names of both files in departing and existing.
adds one to the file.txt

sends the files over discord





