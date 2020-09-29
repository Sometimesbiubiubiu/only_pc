import xlrd



# file_name = "pc数据.xlsx"
class dataLoading(object):

    @classmethod
    def login_data(cls, file_name):
        workspace = xlrd.open_workbook(file_name)
        # 获取全部表名
        # biaos = workspace.sheet_names()
        sheet1 = workspace.sheet_by_name("账号密码")
        row_Nums = sheet1.nrows
        col_Nums = sheet1.ncols
        print('行数：%s, 列数：%s' %(row_Nums, col_Nums))
        key = sheet1.row_values(0)
        s = []
        if row_Nums <= 1:
            print("Null")
        else:
            row = 1
            for i in range(row_Nums - 1):
                d = {}
                values = sheet1.row_values(1)
                # 合并两个列表为字典
                news = dict(zip(key, values))
                s.append(news)

        return s[0]

a = dataLoading.login_data("pc数据.xlsx")
print(a)
print(a['账号'])
