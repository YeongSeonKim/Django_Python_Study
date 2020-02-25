from .common import *

def PostDetailView(request):
    return render(request, 'instagram/post_detail.html')