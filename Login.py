# Importacion de Librerias
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# import time
# import os
# import sys
# import sqlite3
import getpass
 
#declaracion de variables
 
# registeredUser = ('Admin')
# registeredPW = ('123')

users = {'jorge': '1234', 'fonso':'naruto', }

usuario = 'karime'
pswrd = '456'
# print(users.get('jorge'))
 
def login(usuario, passw):
  user = users.get(usuario)
  # print(user)
  if user == passw:
    #Usuario y contraseña correctas
    return 0
  elif user == None:
    #Usuario no encontrado
    return 1
  elif user != passw:
    #Contraseña incorrecta
    return 2
  else:
    #ERROR
    return 3
  
def userAccess():
  # access = False
  for i in range(3):
    usuario=input('User: ')
    passw = getpass.getpass('Password: ')
    userLogin = login(usuario, passw)
    if userLogin==0:
      print('Bienvenido ',usuario, '\n')
      #break
      return True
    elif userLogin ==1:
      print('Usuario no registrado.\n')
    elif userLogin == 2:
      print("El usuario y contraseña no coinciden...\n")
    else:
      print('ERROR!')
  return False


 