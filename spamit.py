#!/usr/bin/python
# vim: set fileencoding=utf-8

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEImage import MIMEImage
from email import encoders
import email.header

import psycopg2
import psycopg2.extras

# MIME capable mail server object
class mailserver(object):

    def __init__(self, servername, emailaddress):
        self.server = smtplib.SMTP()
        self.servername = servername
        self.fromaddr = emailaddress

    def spam(self, recipients, title, body, filename):

	msg = MIMEMultipart()

    	msg['From'] = self.fromaddr
    	msg['To'] = self.fromaddr
    	msg['Subject'] = email.header.Header( title, 'utf-8' ).encode()

    	msg.attach(MIMEText(body, 'html'))

    	if filename:
            attachment = open(filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)


        self.server.connect(self.servername, 25)
        self.server.quit()

# Postgresql data set
class dataset(object):
    
    def __init__(self, host, dbname, user, password, query):
        with psycopg2.connect(host, dbname, user, password, cursor_factory=psycopg2.extras.RealDictCursor) as connection:
            self.cursor = connection.cursor()
            self.cursor.execute(query)

    def __iter__(self):
        return self

    def __next__(self):
        result = self.cursor.fetchmany(100)

        if( result ):
            return([ x['email'] for x in result ])
        else:
            raise StopIteration

    def next(self):
        return self.__next__()


