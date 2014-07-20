from decorators import async
from flask import render_template
from flask.ext.mail import Message
from app import mail
from config import ADMINS


@async
def send_async_email(msg):
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


def follower_notification(followed, follower):
    subject = '[microblog] %s is now following you!' % follower.nickname
    text_body = render_template('follower_email.txt', user=followed, follower=follower)
    html_body = render_template('follower_email.html', user=followed, follower=follower)
    send_email(subject, ADMINS[0], [followed.email], text_body, html_body)