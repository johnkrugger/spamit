# spamit
Just some simple emailing script

# How to use
import spamit

myserver = spamit.mailserver('mail.example.com', 'no-reply@example.com')

for spamlist in spamit.dataset('database.example.com', 'dbname', 'user', 'password', 'SELECT email from users'):
    myserver.spam(spamlist, 'Title', 'message', None)
    
