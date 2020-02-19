from django.shortcuts import render, redirect, HttpResponseRedirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
import string
import random
import hashlib
import base64
from django.contrib.auth.hashers import pbkdf2

'''
http request method 사용방법
viewName(request):
1.    request.method == 'GET':

2.    request.method == 'POST':
'''
# Create your views here.
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

# 회원가입
def RegisterAccountsView(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')

    else:
        # form data 받아오기
        email = request.POST.get('email')
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

        # django 사용자 인증 사용하는 코드 
        '''
        user = User.objects.get(username=user_id)

        if user is not None:
            messages.error(request,'이미 존재하는 아이디가 있습니다. 다른 아이디로 가입해주세요.')
            return redirect('accounts:register')
        else:
            user = User.objects.create_user(username=user_id, password=user_pw, email=email, first_name=name)
            messages.success(request,'회원가입에 성공했습니다. 로그인해주세요.')
            return redirect('accounts:login')
        '''

        try:
            cursor = connection.cursor()

            strSql = "SELECT user_id"
            strSql += " FROM user"
            strSql += " WHERE user_id = (%s)"

            result = cursor.execute(strSql, (user_id,))
            datas = cursor.fetchall()
            connection.commit()   

            if len(datas) != 0:
                # return render(request,'accounts/register.html')
                messages.error(request, '이미 존재하는 아이디가 있습니다. 다른 아이디로 가입해주세요.')
                return redirect('accounts:register')

            else:
                # 비밀번호 hash를 위해 salt, hash_pw 호출
                salt, hashed_pw = hashing_password(user_pw)

                strSql = "INSERT INTO user(user_id, user_pw, name, email, salt)" 
                strSql += " VALUES(%s, %s, %s, %s, %s)"

                result = cursor.execute(strSql, (user_id, hashed_pw, name, email, salt, ))
                             
                messages.success(request, '회원가입에 성공했습니다. 로그인해주세요.')
                # return render(request,'accounts/login.html')
                return redirect('accounts:login')

        except:
            connection.rollback()
            print("Failed RegisterAccountsView")
            messages.error(request, '회원가입을 하는과정에서 문제가 발생했습니다.')
            return redirect('accounts:register')

        finally:
            connection.close()

# 로그인
def LoginView(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    else:
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

        # django 사용자 인증 사용하는 코드 
        '''
        user = authenticate(request, username=user_id, password=user_pw)

        if user is None:
            login(request, user=user)
            return redirect('instagram:main')
        else:
            messages.error(request,'아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력해주세요.')
            return redirect('accounts:login')
        '''

        try:
            cursor = connection.cursor()

            strSql = "SELECT user_id, user_pw, salt"
            strSql += " FROM user"
            strSql += " WHERE user_id = (%s)"

            result = cursor.execute(strSql, (user_id,))
            datas = cursor.fetchall()
            connection.commit()   

            # 아이디가 틀린경우 : 로그인 실패
            if len(datas) == 0:
                messages.error(request,'존재하지 않는 아이디 입니다. 아이디를 다시 입력해주세요.')
                return redirect('accounts:login')

            else:
                reg_id = datas[0][0]
                reg_pw = datas[0][1]
                salt = datas[0][2]

                # hash
                hash = pbkdf2(user_pw, salt, 10000, digest=hashlib.sha256)
                hashed_pw = base64.b64encode(hash).decode('ascii').strip()

                # 비밀번호가 틀린경우 : 로그인 실패
                if str(hashed_pw) != reg_pw:
                    messages.error(request, '비밀번호가 일치하지 않습니다. 비밀번호를 입력해주세요.')
                    return redirect('accounts:login')

                # 둘다 맞는경우 : 로그인 성공
                else:   
                    request.session['user_id'] = reg_id
                    # 메인으로 이동
                    # return render(request, 'acccounts/main.html')
                    return redirect('instagram:main') 

        except:
            connection.rollback()
            print("Failed LoginView")
            messages.error(request, '로그인을 하는 과정에서 문제가 발생했습니다. 다시 로그인해주세요.')
            return redirect('accounts:login')

        finally:
            connection.close()

# 로그아웃
def LogoutView(request):
    logout(request)
    # return render(request, 'accounts/login.html')
    return redirect('accounts:login')