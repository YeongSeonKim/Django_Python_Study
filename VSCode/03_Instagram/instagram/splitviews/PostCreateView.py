from .common import *

def PostCreateView(request):
    return render(request, 'instagram/post_create.html')