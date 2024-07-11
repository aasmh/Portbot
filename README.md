# Portbot
A Discord bot that automatically fetches the port of alexandria's data everyday and pushes that info to a discord server



#### How does it work??


The getinport and getdepart functions click on the excel file so the file downloads.

--headless means it emulates the opening of chrome which decreases overhead and makes it quicker


##the loop

the loop is set to work every 24 hours

it's incased in a try catch block to check for errors, if any are thrown the exception is then sent over discord to notify someone of said error and get it fixed.

readone reads the number
then gets the files from inport and departing
sleeps for 2 seconds to allow for pipelining

proceeds by changing the names of both files in departing and existing.
adds one to the file.txt

sends the files over discord server in the code 





