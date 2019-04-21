from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, id=None, all_phones_from_edit_page=None, email=None,
                 email2=None, email3=None, all_emails_from_edit_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_edit_page = all_phones_from_edit_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_edit_page = all_emails_from_edit_page

        self.id = id

    def __repr__(self):
        return '{%s:%s:%s}' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def sorting_id_or_maxsize(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
