from django.shortcuts import render, get_object_or_404
# from .models import Category,Product
from django.db import connection

# Create your views here.
def DKEA_main(request):

    try:
        cursor = connection.cursor()

        strSql = "SELECT DISTINCT(c.c_name), c.c_code FROM dkea_category as c"

        result = cursor.execute(strSql)
        categories = cursor.fetchall()
        
        connection.commit()
        connection.close()

        data = []
        for category in categories:
            row = {
                'c_name' : category[0],
                'c_code' : category[1],
            }

            data.append(row)

    except:
        connection.rollback() 
        print("Failed selecting in DKEA_main") 

    return render(request, 'DKEA/DKEA_main.html', {'categories':data})


def DKEA_category_list(request, c_code):

    try:
        cursor = connection.cursor()

        # c_name만 가져오는 sql
        c_nameSql  = "SELECT DISTINCT(c_name) FROM dkea_category where c_code = (%s)"

        strSql = "SELECT p.p_id, p.p_name, p.img_src, p.price, c.c_code, c.c_name"
        strSql += " FROM dkea_product as p"
        strSql += " LEFT JOIN dkea_category as c ON p.c_id = c.c_id"
        strSql += " WHERE c.c_code = (%s)"

        c_result = cursor.execute(c_nameSql,(c_code,))
        c_name = cursor.fetchall()

        result = cursor.execute(strSql,(c_code,))
        products = cursor.fetchall()
            
        connection.commit()
        connection.close()

        c_name_data = c_name[0][0]

        data = []
        for product in products:
            row = {
                    'p_id': product[0],
                    'p_name': product[1],
                    'img_src': product[2],
                    'price': product[3],
                    'c_code': product[4],
                    'c_name': product[5],
            }
            data.append(row)

        content = {
            'products':data,
            'c_name_data':c_name_data
            }

    except:
        connection.rollback()
        print("Failed selecting in DKEA_category_list")

    return render(request, 'DKEA/DKEA_category_list.html', content)


def DKEA_product_detail(request, p_id):

    try:
        cursor = connection.cursor()

        strSql = "SELECT p.p_id, p.p_name, p.price, p.link, p. c.c_code, c.c_name, c.i_name"
        strSql += " FROM dkea_product as p"
        strSql += " LEFT JOIN dkea_category as c ON p.c_id = c.c_id"
        strSql += " WHERE p.p_id = (%s)"
        result = cursor.execute(strSql,(p_id,))
        datas = cursor.fetchall()
            
        connection.commit()
        connection.close()

        product_info = {
            'p_id': datas[0][0],
            'p_name': datas[0][1],
            'price': datas[0][2],
            'link': datas[0][3],
            'c_code': datas[0][4],
            'c_name': datas[0][5],
            'i_name': datas[0][6],
        }

    except:
        connection.rollback()
        print("Failed selecting in DKEA_product_detail")
        # product_info = {}

    return render(request, 'DKEA/DKEA_product_detail.html', {'product_info':product_info})