from telegram.ext import MessageFilter
from telegram import Message
from bot import AUTHORIZED_CHATS, SUDO_USERS, OWNER_ID


class CustomFilters:
    class __OwnerFilter(MessageFilter):
        def filter(self, message: Message):
            return message.from_user.id == OWNER_ID

    owner_filter = __OwnerFilter()

    class __AuthorizedUserFilter(MessageFilter):
        def filter(self, message: Message):
            uid = message.from_user.id
            return uid in AUTHORIZED_CHATS or uid in SUDO_USERS or uid == OWNER_ID

    authorized_user = __AuthorizedUserFilter()

    class __AuthorizedChat(MessageFilter):
        def filter(self, message: Message):
            return message.chat.id in AUTHORIZED_CHATS

    authorized_chat = __AuthorizedChat()

    class __SudoUser(MessageFilter):
        def filter(self, message: Message):
            return message.from_user.id in SUDO_USERS

    sudo_user = __SudoUser()

    def _owner_query(user_id):
        return user_id == OWNER_ID or user_id in SUDO_USERS