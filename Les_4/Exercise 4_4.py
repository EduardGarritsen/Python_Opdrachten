def new_password(newpassword, oldpassword):
    if len(newpassword) >= 6 and newpassword != oldpassword:
        return True
    else:
        return False

print(new_password('hallo1', 0))

print(new_password('hallo1', 'hallo1'))
