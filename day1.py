email_id='saketh@codegnan.com'
print(email_id[email_id.index('@')+1 : email_id.index('.') ])

email_ids = ['saketh@codegnan.com', 'hemanth@gmail.com', 'hemanth@google.com']
for i in email_ids:
    print(i[i.index('@')+1 : i.index('.') ])
email_ids.extend(['abc@codegnan.com','def@123.com','ssmb@rajmouli.romcom'])
print(email_ids)

user={}
for i in range(len(email_ids)):
    user[i+1]=email_ids[i]
print(user)
hh={}
hh = dict(enumerate(email_ids,1))
print(hh)
    









