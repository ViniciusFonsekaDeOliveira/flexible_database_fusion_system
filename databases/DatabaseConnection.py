class DatabaseConnection:
    def __init__(self, host, port, user, password, database_name) -> None:
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database_name = database_name

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def database_name(self):
        return self._database_name

    @host.setter
    def host(self, host):
        self._host = host

    @port.setter
    def port(self, port):
        self._port = port

    @user.setter
    def user(self, user):
        self._user

    @password.setter
    def password(self, password):
        self._password

    @database_name.setter
    def database_name(self, database_name):
        self._database_name = database_name
