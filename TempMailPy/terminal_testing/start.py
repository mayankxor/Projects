from pymailtm import MailTm

client = MailTm()

# domain = client._get_domains_list()[0]
password = client._generate_password(length=10)
print(password)