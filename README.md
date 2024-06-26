# restaurant-information-system

## Backend Usage Guide

To activate and use the server, you need to setup a virtual environment
*FROM THIS DIRECTORY, OPEN A TERMINAL*
Use the following commands:

```powershell
> cd backend
> py -3 -m venv .venv
```

You should only ever need to do that once on your machine. Now when you run python, you need to activate your environment with the following command from the /backend directory

```powershell
> .venv\Scripts\activate # CMD
> .venv\Scripts\activate.ps1 # POWERSHELL
```

*NOTE* Make sure you are using the correct command for whatever terminal you are using, later there will be differences.
*NOTE2* You can leave the virtual environment at any time with: 'deactivate'

When you are in the activated environment, you will need to use the following set of commands the first time:

```powershell
pip install Flask
pip install mysql-connector-python
```

Flask Documentation[https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses]
mysql-connector-python Documentation[https://www.w3schools.com/python/python_mysql_getstarted.asp] - kinda
More exact mysql-connector-python documentation[https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html]

One last thing on discord I will post the DB password, grab that if its still there or DM me for it. If everything has worked up to this point, you should have a .venv/Scripts folder. Based on your terminal type do the following:

### POWERSHELL

After this line on roughly line 167 of the activate.ps1 file in .venv/Scripts:

```script
<# Begin Activate script --------------------------------------------------- #>
```

type the following:
$env:DB_PASSWORD=PASSWORD

Where the password is what you find on discord. Place it in quotes. I did mine on line 172
*NOTE* YOU MAY NEED TO DEACTIVATE ENVIRONMENT AND REACTIVATE IT TO SEE RESULTS
You should be able to check that it works if you type: 'echo %MY_VARIABLE%' while the environment is on. It should spit the password back to you

### CMD

Somewhere in the file activate.bat in .venv/Scripts, probably at the end is fine, idk type the following

SET DB_PASSWORD=PASSWORD

Where the password is what you find on discord. Place it in quotes. I did mine on line 172
You should be able to check that it works if you type: echo $env:MY_VARIABLE while the environment is on. It should spit the password back to you
*NOTE* YOU MAY NEED TO DEACTIVATE ENVIRONMENT AND REACTIVATE IT TO SEE RESULTS

### WSL

IF you are using WSL for this, probably just chatgpt the equivalent commands. I think those will end up in the 'activate file'.

### Starting the server

At this point if you followed everything, it should be ready to go. First activate the environment, then you can use one of two commands

```powershell
flask run
OR
flask run --debug
```

--debug will put it in a 'watch' mode where you will not have to restart the server when you make changes, and is generally more resistent to bugs. This can mean that bugs can go unnoticed. Do the final demo in flask run just to make sure things work.
