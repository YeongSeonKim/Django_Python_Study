from .common import *

def PasswordModifyView(request):
    return render(request,'accounts/password_modify.html')