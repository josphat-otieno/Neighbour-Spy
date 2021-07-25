from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    #creating message subject and sender
    subject = "Thanks for signing up to spy on your neighbours"
    sender = 'egesacollins92@gmail.com'

    #passing in the context variables
    text_context = render_to_string('email/email.txt',{"name":name})
    html_content = render_to_string('email/email.html',{"name":name})

    msg = EmailMultiAlternatives(subject, text_context,sender,[receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()