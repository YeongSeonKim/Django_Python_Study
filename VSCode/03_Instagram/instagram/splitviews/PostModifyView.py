from .common import *

@login_required
def PostModifyView(request):
    if request.method == 'GET':
        return render(request, 'instagram/post_modify.html')
    else:
        pass