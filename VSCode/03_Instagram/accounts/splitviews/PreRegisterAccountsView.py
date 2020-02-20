from .common import *

'''
http request method 사용방법
viewName(request):
1.    request.method == 'GET':

2.    request.method == 'POST':
'''

# 회원가입
def PreRegisterAccountsView(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')

    else:
        # form data 받아오기
        email = request.POST.get('email')
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

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