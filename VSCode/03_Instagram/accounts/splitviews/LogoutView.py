from .common import *

# 로그아웃
def LogoutView(request):
    logout(request)
    # return render(request, 'accounts/login.html')
    return redirect('accounts:login')