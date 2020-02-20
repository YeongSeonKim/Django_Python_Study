from .common import *

# 메인페이지
@login_required
def MainView(request):
    return render(request,'instagram/main.html')