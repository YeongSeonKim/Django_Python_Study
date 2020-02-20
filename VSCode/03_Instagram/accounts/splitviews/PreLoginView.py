from .common import *

# 로그인
def PreLoginView(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    else:
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

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