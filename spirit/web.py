import datetime
import os

from flask import Flask

app = Flask(__name__)


class Tagught():

    def __init__(self, taught, date):
        self.taught = taught
        self.date = date

    def get_tahught(self):
        return self.taught

    def get_date(self):
        return self.date

    def format(self):
        return """
<tr>
    <td>{}</td>
    <td>{}</td>
</tr>

""".format(self.get_tahught(), self.get_date())


class TaughtsFile():
    def __init__(self, file_path):
        self.file_path = file_path

    def get_thaughts(self):
        file_interactor = open(self.file_path, "r")
        lines = file_interactor.readlines()
        taughts = []
        for line in lines:
            taughts.append(Tagught(line,
                                   convert_file_name_to_date(self.file_path)))
        file_interactor.close()
        return taughts

    def format(self):
        return "\n".join([t.format() for t in self.get_thaughts()])


class User():
    def __init__(self, user):
        self.template = \
            """<li><a href="/users/{user_id}">
            user{user_id}</a></li>"""
        self.user = user

    def format(self):
        return self.template.format(user_id=self.user)


class UsersListHTTP():
    def __init__(self, users_list):
        self.users_list = users_list
        self.template = """<html>
    <head>
        <title>Brain Computer Interface</title>
    </head>
    <body>
        <ul>
            {users}
        </ul>
    </body>
</html>
"""

    def format_users_list(self):
        formatted_users = [User(user).format() for user in self.users_list]
        users_text = "\n".join(formatted_users)
        return self.template.format(users=users_text)


def get_users_list(data_dir):
    @app.route('/')
    def wrappe():
        u_list = [user_dir for user_dir in os.listdir(data_dir)]
        print(UsersListHTTP(u_list).format_users_list())
        return UsersListHTTP(u_list).format_users_list(), 200

    return wrappe


def get_user_thaughts(data_dir):
    @app.route('/users/<int:user_id>')
    def wrapper(user_id):
        user_path = os.path.join(data_dir, str(user_id))
        if not (os.path.exists(user_path)):
            return "", 404
        files = [TaughtsFile(
            os.path.join(user_path, file)).format()
                 for file in os.listdir(user_path)]
        return """
        <html>
        <head>
        <title>Brain Computer Interface: User {}</title>
        </head>
        <body>
        <table>
            {}
        </table>
        </body>
        </html>

        """.format(user_id, "\n".join(files)), 200

    return wrapper


def run_webserver(host, port, data_dir):
    get_user_thaughts(data_dir)
    get_users_list(data_dir)
    app.run(host=host, port=port)


def delete_comma(string):
    return string.replace("'", "")


def convert_file_name_to_date(file_name):
    return datetime.datetime.strptime(
        os.path.basename(file_name),
        '%Y-%m-%d_%H-%M-%S.txt') \
        .strftime('%Y-%m-%d %H:%M:%S')
