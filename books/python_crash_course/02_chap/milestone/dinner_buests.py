import sys
sys.path.append("..")
from guest_list import program, persons_dinner, delete_lst
program(persons_dinner)
print(len(persons_dinner))
delete_lst(persons_dinner)

#https://vegibit.com/how-to-import-module-from-parent-directory-in-python/
