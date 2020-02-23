from .common import *

def PostListView(request, user_id):

    return render(request, 'instagram/post_list.html')