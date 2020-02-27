import string
import random
import hashlib
import base64

from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.db import connection
from django.contrib import messages
# from django.contrib.auth.models import User
from accounts.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import pbkdf2
# 파일 경로
from django.core.files.storage import default_storage

# 비밀번호 암호화
def hashing_password(user_pw):
    # salt 생성 - salt는 최소 128bit 이상이 권고된다 하여 다음과 같이 생성
    count = random.randint(16, 21) # 랜덤으로 17개
    string_pool = string.ascii_letters + string.digits + string.punctuation
    # count만큼 문자열을 랜덤 선택하여 합치기
    # ""의 의미는 공백없이 합친다는 것을 의미한다.
    salt = "".join(random.choices(string_pool, k=count))    

    hash = pbkdf2(user_pw, salt, 10000, digest=hashlib.sha256)
    hashed_pw = base64.b64encode(hash).decode('ascii').strip()

    return salt, hashed_pw

# 프로필편집 사진 업로드 