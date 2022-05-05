import jwt
s = jwt.encode({"username":'zh'},key='123456',algorithm='HS256')
print('加密后的数据是',s)
s_later = jwt.decode(s,'123456',algorithms='HS256')
print('解密后的数据是',s_later)


