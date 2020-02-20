from .common import *

# 회원가입
def RegisterAccountsView(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')

    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        
        try:
            user = User.objects.get(username=user_id)

            messages.error(request,'이미 존재하는 아이디가 있습니다. 다른 아이디로 가입해주세요.')
            return redirect('accounts:register')

        # objectDoesNotExist 
        # -> 모든 예외가 발생하면이 아니라 가져오려는 객체가 없을 때만 에러처리를 해주는 것을 의미
        except ObjectDoesNotExist:
            user = User.objects.create_user(username=user_id, password=user_pw, email=email, first_name=name)
            messages.success(request,'회원가입에 성공했습니다. 로그인해주세요.')
            return redirect('accounts:login')


        # user_error = get_object_or_404(User, username=user_id)
        # user = User.objects.get(username=user_id)

        # if user is not None:
        #     messages.error(request,'이미 존재하는 아이디가 있습니다. 다른 아이디로 가입해주세요.')
        #     return redirect('accounts:register')
        # else:
        #     user = User.objects.create_user(username=user_id, password=user_pw, email=email, first_name=name)
        #     messages.success(request,'회원가입에 성공했습니다. 로그인해주세요.')
        #     return redirect('accounts:login')