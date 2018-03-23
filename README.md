# Watcher of Friends Online

This script show your online friends list for [vk.com](https://vk.com).

# Quickstart

You need to specify vk user **login** with parameter *-l* or *--login*. You can register account at [vk](https://vk.com).
When you run this script, you will be promted to enter your vk **password** securely.

You must turn off two factor in vk, to allow script authentification by login/password.

You need to specify **app_id** with parameter *-a* or *--appid*
To get **app_id**, create new app in [developers portal](https://vk.com/dev) 

Example of script launch on *Linux*, *Python 3.5*:

```
vk_friends_online.py -l mymail@gmail.com -a 12345
enter password:
friends online:
Guido Van Rossum
Linus Torvalds
Richard Stallman

```

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
