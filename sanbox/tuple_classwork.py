email_adresses = ('uduak@gmail.com', 'aitee@gmail.net', 'emmy@yahoo.com', 'sophie@yahoo.net', 'sara23@gmail.com', 'youyou@yahoo.net')


def take_tuple(email_adresses):
    email_list = []
    for email_adress in email_adresses:
        if not email_adress.endswith('.com'):
            user_name = email_adress.split('@')[0]
            email_list.append(user_name + '.com')
        else:
            email_list.append(email_adress)
    return email_list


print(take_tuple(email_adresses))

  

