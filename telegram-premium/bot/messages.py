import abc

import telegram as tg


class BaseMessages(abc.ABC):
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def echo(self, text: str) -> str:
        pass


class RegularUser(BaseMessages):
    def start(self) -> str:
        return "Ciao!"

    def help(self) -> str:
        return "Devi acquistare l'abbonamento"

    def echo(self, text: str) -> str:
        return f"{text}"


class PremiumUser(RegularUser):
    def start(self) -> str:
        return "Ciao! (premium)"

    def help(self) -> str:
        return "Il nostro responsabile la contatterà al più presto"


def get_messages(user: tg.User) -> BaseMessages:
    if not user.is_premium:
        return PremiumUser()
    return RegularUser()
