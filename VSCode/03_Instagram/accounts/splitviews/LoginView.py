from .common import *

# 로그인
def LoginView(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    else:
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user=user)
            return redirect('instagram:main')
        else:
            messages.error(request,'아이디 또는 비밀번호가 일치하지 않습니다. 다시 입력해주세요.')
            return redirect('accounts:login')