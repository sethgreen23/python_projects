
class Email:
    def __init__(self, local, domain, extention):
        self.local = local
        self.domain = domain
        self.extention = extention
    @classmethod
    def slicer_email(cls, str):
        local, _, first_result = str.partition('@')
        domain, _, extention = first_result.partition('.')
        return (Email(local, domain, extention))
# prepare the import
email_slicer = Email.slicer_email
