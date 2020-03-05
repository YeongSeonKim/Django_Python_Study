from .common import *

def PostDeleteView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "DELETE FROM post"
        strSql += " WHERE post_id = (%s)"
        
        result = cursor.execute(strSql, (post_id,))
        
        return redirect('instagram:post_list', user.username)

    except:
        connection.rollback()
        print('Failed deleting in PostDeleteView')

        messages.error(request, '포스트를 삭제하는데 에러가 발생했습니다.')
        return redirect('instagram:post_detail', post_id)
    
    finally:
        connection.close()

