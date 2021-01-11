#!/usr/bin/env python

import sys

class Contact(object):

	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return ('{} {} {}'.format(self.name, self.phone, self.email))

class ContactList(object):

	def __init__(self, d={}):
		self.d = d

	def add_contact(self, contact):
		if contact.name not in self.d:
			self.d[contact.name] = (contact.phone, contact.email)
		else:
			self.d[contact.name] = (contact.phone, contact.email)

	def del_contact(self, x):
		if x in self.d:
			del self.d[x]

	def get_contact(self, x):
		if x in self.d:
			return self.d[x]
		else:
			return 

	def __str__(self):
		b = ['Contact list\n', ('-' * len('Contact list')) + '\n']
		for name in sorted(self.d.keys()):
			b.append('{} {} {}\n'.format(name, self.d[name][0], self.d[name][1]))
		return "".join(b).strip()
def main():
    cl = ContactList()
    for line in sys.stdin:
        [name, phone, email] = line.strip().split()
        c = Contact(name, phone, email)
        cl.add_contact(c)

    print(cl.get_contact('Jimmy'))
    print(cl.get_contact('Mary'))

    print(cl)
    cl.del_contact('Maggie')
    cl.del_contact('Maggie')

    c = Contact('Sue', '087-6442378', 'sue@eircom.net')
    cl.add_contact(c)
    c = Contact('Fred', '085-8776543', 'fred@yahoo.com')
    cl.add_contact(c)
    print(cl)

if __name__ == '__main__':
    main()
