from fdfs_client.client import Fdfs_client

if __name__ == '__main__':
    # 创建连接对象
    client = Fdfs_client('client.conf')
    # 上传文件,文件所在目录是/home/python/桌面/111.jpg
    ret = client.upload_by_filename('/home/python/桌面/111.jpg')
    # 响应值
    print(ret)

'''
mysql -h127.0.0.1 -uroot -pmysql meiduo_tbd39 < goods_data.sql(大于号导出,小于号导入)
运行后返回值展示:
{'Remote file_id': 'group1/M00/00/00/wKiZhF6m1hKAR3T9AACVNfeHyA8404.jpg', 
'Status': 'Upload successed.', 
'Group name': 'group1', 
'Local file name': '/home/python/桌面/111.jpg', 
'Uploaded size': '37.00KB',
'Storage IP': '192.168.153.132'}

'''