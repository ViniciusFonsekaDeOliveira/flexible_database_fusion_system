class Person:
    def __init__(self, realname, username, email, profession) -> None:
        self._realname = realname
        self._username = username
        self._email = email
        self._profession = profession

    @property
    def realname(self) -> str:
        return self._realname

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def profession(self) -> str:
        return self._profession

    @realname.setter
    def realname(self, realname) -> None:
        self._realname = realname

    @username.setter
    def username(self, username) -> None:
        self._username = username

    @email.setter
    def email(self, email) -> None:
        self._email = email

    def __str__(self):
        return str({
            "realname": self.realname,
            "username": self.userName,
            "email": self.email,
            "profession": self.profession
        })

    def __eq__(self, other) -> bool:
        return (isinstance(other, Person) and
                self.realname == other.realname and
                self.username == other.username and
                self.email == other.email and
                self.profession == self.profession)

    def __hash__(self) -> int:
        return (hash(self.realname) ^ hash(self.username) ^ hash(self.email) ^ hash(self.profession))
