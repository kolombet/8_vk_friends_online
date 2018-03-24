import vk
import argparse
import sys
from getpass import getpass


def get_api(app_id, user_login, user_password, api_version):
    scope = "friends"
    session = vk.AuthSession(
        app_id=app_id,
        user_login=user_login,
        user_password=user_password,
        scope=scope
    )
    return vk.API(session, v=api_version)


def get_online_friends_ids(api):
    return api.friends.getOnline()


def get_online_friends(api):
    return api.users.get(user_ids=get_online_friends_ids(api))


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("{} {}".format(friend["first_name"], friend["last_name"]))


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
        help="vk api version",
        default="5.73"
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
    if not args.login:
        sys.exit("please specify login")
    if not args.app_id:
        sys.exit("please specify app id")
    password = getpass("enter password:")
    if not password or password.isspace():
        sys.exit("please enter password")
    api = get_api(args.app_id, args.login, password, args.version)
    friends_online = get_online_friends(api)
    if not len(friends_online):
        sys.exit("no friends online")
    print("friends online:")
    output_friends_to_console(friends_online)
