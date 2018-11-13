# spamit
Just some simple emailing script

# How to use
import spamit

myserver = spamit.MailServer('mail.example.com', 'no-reply@example.com')

for spamlist in spamit.Dataset('database.example.com', 'dbname', 'user', 'password', 'SELECT email from users'):
    myserver.spam(spamlist, u'Title', 'message', None)

for spamlist in spamit.EmailFile('list.txt'):
    myserver.spam(spamlist, u'Title', message, None)

    
