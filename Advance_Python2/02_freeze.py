# PIP FREEZE COMMAND : ‘pip3 freeze’ returns all the package installed in a given python environment along with the versions.

# Output in Terminal of pip3 freeze :
# distlib==0.3.9
# filelock==3.16.1
# numpy==2.1.3
# pandas==2.2.3
# platformdirs==4.3.6
# python-dateutil==2.9.0.post0
# pytz==2024.2
# six==1.16.0
# tzdata==2024.2
# virtualenv==20.28.0

#  pip3 r freeze > requirements .txt : The ommand creates a file named ‘requirements.txt’ in the same directory containing the output of ‘pip3 freeze’.



# We can distribute this file to other users, and they can recreate the same environment using : # pip3 install –r requirements.txt

# Note : Here, 'r' is the read command that read the requirements.txt file and install that packages.
