from .common import *

'''
[Instagram] 북마크 뷰
: 사용자가 포스트의 컬렉션 버튼을 누르면 사용자의 컬렉션에 저장되는 뷰
- CollectionView는 main.html, post_detail.html에 있는 컬렉션 버튼과 연결되어있다.
- Ajax
1. 현재 로그인된 유저가 컬렉션을 누른 포스트의 post_id와 현재 유저의 아이디로 collection에 데이터 INSERT
2. 성공 여부를 return
'''

@login_required
def CollectionView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "INSERT INTO collection(post_id, user_id)"
        strSql += " VALUES ((%s), (%s))"

        result = cursor.execute(strSql, (post_id, user.username))

        return HttpResponse(json.dumps({'result': '200',}), content_type="application/json")

    except:
        connection.rollback()
        print("Failed inserting in CollectionView")

    finally:
        connection.close()