from .common import *

# 메인페이지
def PreMainView(request):
    # request가 session을 가지고 있는지 판단 session안에서 user_id 키 값을 가져오고 False로
    # isSession = request.session.get('user_id',False)
    isSession = request.session.get('username',False)

    if isSession is not False:
        context = {
            'user_id':isSession,
        }
        return render(request, 'instagram/main.html',context)
    else:
        return redirect('accounts:login')