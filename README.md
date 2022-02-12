There are two files.
1. spam_text.txt : Whatever you write in this file will be used as spam text.
2. main.py : It is the main code.

How it works:
Once you execute "main.py" by default you have 5 seconds (unless you change it in main.py) after 5 seconds, wherever your cursor is, it will start writing contents from "spam_text.txt" line by line and button "Enter" will be pressed after each line, if you are writing on any text editor then "Enter" will create newline but you your cursor is somewhere where "Enter" performs different action then it will follow accordingly.

This process process is too fast, if you want to make it slow, just uncomment the line after "Enter" line in main.py. By default it is set to 1 sec, you can change it ofcourse for your requirements.

To stop this program, open command line where it is being executed and press "ECS" on keyboard, it will stop instantly.
