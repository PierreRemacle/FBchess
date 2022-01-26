#1001 programming , python project

#import library

from fbchat import Client
from fbchat.models import Message, MessageReaction
import matplotlib.pyplot as plt

# facebook username & password
username = "pierrepierreremacle@gmail.com"
password = "Romacaputmundi1"

# login
client = Client(username, password)

# get list users you most recently talked to
users = client.fetchThreadList(limit=400)


# get the detailed informations about users
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users ]
print("j'ai les infos \n")
# sort by number of messages

sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
print("j'ai trier les infos \n")

textfile = open("NomEtNombreMessage.txt", "w")
textfile2 = open("nombreMessage.txt", "w")

for element in sorted_detailed_users:

    textfile.write(str(i.name )+" "+ str(i. message_count)+"\n")
    textfile2.write(str(i. message_count)+"\n")
textfile.close()
textfile2.close()
print("j'ai fais les fichiers \n")
list = []
for i in sorted_detailed_users:
    List.append(i.message_count)




# get all users you talked to in messenger in your account
print("je fais le plot \n")

plt.plot(List)

plt.show()

print("done\n")

# logout
client.logout()
