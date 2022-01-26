


import fbchat
from fbchat import log, Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):

    def onMessage(self, author_id, message_object, thread_id=id, thread_type=2, **kwargs):


        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        ImageAttachment = "/Users/Pierre/Downloads/249787853_2764300960526907_7964688598667753929_n.gif"
        if thread_id == "100004021827347" and (message_object.text.casefold() == "fesse" or message_object.text.casefold() == "bum" or message_object.text.casefold() == "fesses"):
            self.sendLocalFiles(ImageAttachment, thread_id=thread_id, thread_type=thread_type)
        if thread_id in["100003832782257","100001009787116","100005667604915","2753997274625987"] :

            if author_id!=self.uid and "bite"in message_object.text.casefold():
                message =fbchat.Message("bite")
                self.send(message, thread_id=thread_id, thread_type=thread_type)

        if thread_id == "1623932997":

            if author_id!=self.uid and "i love"in message_object.text.casefold():
                message =fbchat.Message("Rock&Roll")
                self.send(message, thread_id=thread_id, thread_type=thread_type)
        if thread_id == "100015773266916":


            if author_id!=self.uid and "bite"in message_object.text.casefold():
                message =fbchat.Message("bite")
                self.send(message, thread_id=thread_id, thread_type=thread_type)

        if thread_id == "3326109884106903":
            self.moveThreads('ARCHIVED',"3326109884106903")


client = EchoBot("pierrepierreremacle@gmail.com", "Romacaputmundi1")
client.listen()
