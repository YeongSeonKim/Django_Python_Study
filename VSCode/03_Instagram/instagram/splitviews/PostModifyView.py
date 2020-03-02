from .common import *

'''
[Instagram] 포스트 글 수정 페이지
: 사용자 입력한 포스트 글을 수정하는 페이지
1. request.method == GET
: post_modify.html rendering
2. request.method == POST
: post_modify.html 의 form 데이터를 받아와 포스트 글 UPDATE
2.1 post_modify.html 의 form 데이터를 받아온다.
'''

@login_required
def PostModifyView(request):
    if request.method == 'GET':
        return render(request, 'instagram/post_modify.html')
    else:
        try:
            return redirect('instagram:post_detail')
        
        except: 
            messages.error(request, '사용자가 포스터 내용을 수정하는 과정에서 에러가 발생했습니다.')
            return redirect('instagram:post_modify')