import vk
import argparse
import sys
from getpass import getpass



def get_api(app_id, user_login, user_password, api_version):
    session = vk.AuthSession(
        app_id=app_id,
        user_login=user_login,
        user_password=user_password,
    )
    api_version = "5.73"
    return vk.API(session, v=api_version)


def get_frineds(api):
    return api.friends.get(fields="domain")["items"]


def get_online_friends(api):
    friends = get_frineds(api)
    friends_online = [friend for friend in friends if friend["online"] == 1]
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("{} {}".format(friend["first_name"], friend["last_name"]));
    pass


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l",
        "--login",
        dest="login",
        help="vk.com login"
    )
    parser.add_argument(
        "-v",
        "--version",
        dest="version",
        help="vk api version"
    )
    parser.add_argument(
        "-a",
        "--appid",
        dest="app_id",
        help="vk app id"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    
    login = args.login
    if not login:
        sys.exit("please specify login")
        
    app_id = args.app_id
    if not app_id:
        sys.exit("please specify app id")
        
    default_api_version = "5.73"
    version = args.version
    if not version:
        version = default_api_version 
        
    password = getpass("enter password:")
    if not password or password.isspace():
        sys.exit("please enter password")
    api = get_api(app_id, login, password, version)
    friends_online = get_online_friends(api)
    print("friends online:")
    output_friends_to_console(friends_online)
