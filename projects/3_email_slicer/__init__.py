from email_slicer import email_slicer

email_sl = email_slicer("dridi.chaith@gmail.com")
print(f'{email_sl.local} {email_sl.domain} {email_sl.extention}')
