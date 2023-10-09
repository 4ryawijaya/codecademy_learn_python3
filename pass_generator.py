def username_generator(first_name, last_name):
  if len(first_name) <= 3 and len(last_name) <= 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username

def password_generator(user_name): 
  temp_pass = ""

  # user = username_generator(user_name)
  temp_pass = user_name[-1] + user_name[:-1]
  return temp_pass


print(username_generator("Abe", "Simpson"))
print(password_generator(username_generator("Abe", "Simpson")))
print(password_generator("apple"))