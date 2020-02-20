from .common import *

def PostDetailView(request):
    return render(request, 'instagram/each_post_detail.html')