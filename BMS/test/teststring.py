fname = "bill gates"
age = "100"
txt1 = "My name is {}, I'am {}".format(fname, age)
txt2 = "My name is {0}, I'am {1}".format("Bill", 64)
txt3 = "My name is {}, I'am {}".format("Bill", 64)
print(txt1)
print(txt2)
print(txt3)


sql = " select * from users where user_name = {} and user_passwd = {};".format(
    fname, age)
print(sql)
