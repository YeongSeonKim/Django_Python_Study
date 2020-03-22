from .common import *

'''
[Instagram] 포스트 검색 뷰
'''

def SearchView(request):
    return render(request, 'instagram/search.html')