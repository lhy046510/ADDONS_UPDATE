import hashlib

content = open("E:\Repo\ADDONS_UPDATE\pre_install_addons.xml").read()
md5 = hashlib.md5(content)
print md5.hexdigest()
