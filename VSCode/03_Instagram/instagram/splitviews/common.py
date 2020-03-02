import os
import uuid # 랜덤문자열을 만들어줌
import datetime 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
from accounts.models import User
# 파일 경로 / default_storage.save(path, file)
from django.core.files.storage import default_storage

# 파일 업로드 / postimg :  파일 객체
# 이름이 같은 파일을 저장하는 경우 => 고유의 값으로 파일경로를 만들어준다.
def fileUpload(user, postImg):
    # 파일이름과 확장자를 분리
    fileName, extension = os.path.splitext(postImg.name)

    # uuid.uuid4()
    newFileName = str(uuid.uuid4()) + extension
    filePath = os.path.join('image', user.username, newFileName)

    # 사진 파일을 지정된 경로에 저장
    default_storage.save(filePath, postImg)
    # 저장된 파일의 경로 가져오기
    post_img_url = default_storage.url(filePath)

    return post_img_url

'''
# 파일 업로드 - 원래의 경우
def fileUpload(user, postImg):
    filePath = os.path.join('image', user.username, postimg.name)

    default_storage.save(filePath, postImg)
    # default_storage는 media부터 시작되는 url을 반환
    # 파일경로를 사용해서 풀경로를 받아온다.
    post_img_url = default_storage.url(filePath) 
    # => 파일경로가 아닌 파일이름으로하게 되면 
    #    같은 이름의 이미지를 여러개 가져올수 있으므로 파일경로로 탐색

    return post_img_url
'''