from .common import *

def PostListView(request, user_id):
    return render(request, 'instagram/my_post_list.html')