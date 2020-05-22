try:
    from email.message import EmailMessage 
    import smtplib 
    import vk
except ModuleNotFoundError as e:
    print(e)

class network:
    def gmail_message_sender(by_user, password, to_user, subject, text):
        pass
