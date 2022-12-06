from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GetData
from django.http import JsonResponse
from . serializers import GetDataSerializer
from rest_framework.decorators import api_view
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
import base64
import hashlib

class AESCipher:
    def __init__(self, key, iv):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.iv = hashlib.sha256(iv.encode('utf-8')).digest()[:16]

    __pad = lambda self,s: s + ((AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)).encode('utf-8')
    __unpad = lambda self,s: s[0:-ord(s[-1])]

    def encrypt( self, raw ):
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_CBC, self.iv.encode("utf8") )
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))

# cipher = AESCipher('c7b35827805788e77e41c50df44441491098be42', 'c09f6a9e157d253d0b2f0bcd81d338298950f246')

# enc_str = cipher.encrypt("secret")
# print(enc_str)
# def encrypt(password,key,iv):
  
#     secretkey = hashlib.sha256(key.encode('utf-8')).digest()
#     iv = hashlib.sha256(iv.encode('utf-8')).digest()[:16]
#     __pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
#     __unpad = lambda s: s[0:-ord(s[-1])]
#     raw = __pad(password)
#     cipher = AES.new(secretkey, AES.MODE_CBC, iv)
#     return base64.b64encode(cipher.encrypt(password))



@api_view(['GET','POST'])
def get(request):
    if request.method=='GET':
        data=GetData.objects.all()
        
        serializer=GetDataSerializer(data,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method=='POST':
        serializer=GetDataSerializer(data=request.data)

        u_name=request.POST['username']
        # pd=request.POST['password']
        cipher = AESCipher('bUbE5^o3SunEsb&UWh5^9pDTJlo7%3Ku', 'R4^2CF&ULo^0RP2i')

        enc_str = cipher.encrypt(b"password")
        if serializer.is_valid():
            serializer.save()
        return Response("password  : "+str(enc_str))
#         if serializer.is_valid():
#             serializer.save()
#             u_name=request.POST['username']
#             pd=request.POST['password']
#             cipher = AESCipher('bUbE5^o3SunEsb&UWh5^9pDTJlo7%3Ku', 'R4^2CF&ULo^0RP2i')

#             enc_str = cipher.encrypt(b"password")
#             GetData.username=u_name
#             GetData.password=enc_str
#             context={
#                 'username':u_name,
#                 'password':enc_str
#             }
#             serializer.save(password=enc_str)
            
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
# # Create your views here.
# class DataList(APIView):
    def get(self,request):
        data=GetData.objects.all()
        

        # cipherdata=data.password
        # print(cipherdata)
        serializer=GetDataSerializer(data,many=True)
        return Response(serializer.data)    