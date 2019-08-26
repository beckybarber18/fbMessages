# fbMessages
Graph cumulative Facebook messages with a given person over time.

1. Download your facebook message data: Go to Facebook --> Click on the down arrow in top right corner --> Click on settings --> Go to "Your Facebook Information" --> Click "View" under "Download your information" --> Select messages only. You can use low quality, and you should select json format.
2. Download this file and put it in the "messages" folder with your data.
3. Create a file called "people.txt". Put it in the same folder as the python script. In this file, list (on separate lines) the first and last names (with no space) of the people whose data you want to graph. For example, if I want to graph John Doe's data, I would list johndoe.
3a. Note that each line only needs to contain a substring of a folder in your "inbox" folder in "messages." So if you want to look at a group chat, just write a substring of the name of the folder containing the messages from that group in people.txt.
4. Run the program in terminal by typing:
   python mssgs_over_time.py.
