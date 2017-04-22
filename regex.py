import re
Email = re.compile(r'\w+@\w+\.\w+')
Email.search('someone@gmail.com').group()

Email_1 = re.compile(r'\w+\.\w+@\w+\.\w+')
Email_1.search('bill.gates@microsoft.com').group()

name = re.compile(r'\<\w+\s+\w+\>\s+\w+@\w+\.\w+')
name.search('<Tom Paris> tom@voyager.org').group()