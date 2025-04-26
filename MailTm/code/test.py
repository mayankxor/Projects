from mailtm import Email

client = Email()
domain = client.domain
client.register()
address = client.address
def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
print("Email: {}@{}".format(address, domain))
client.start(listener)
print("Waiting...	")