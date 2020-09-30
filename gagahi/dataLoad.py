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
        accouts = []
        if row_Nums <= 1:
            print("Null")
        else:
            row = 1
            for i in range(row_Nums - 1):
                d = {}
                values = sheet1.row_values(i+1)
                # 合并两个列表为字典
                news = dict(zip(key, values))
                accouts.append(news)

        return accouts

    @classmethod
    def message_data(cls, file_name):
        workspace = xlrd.open_workbook(file_name)
        # 获取全部表名
        # biaos = workspace.sheet_names()
        sheet2 = workspace.sheet_by_name("聊天文本")
        row_Nums1 = sheet2.nrows
        print('行数：%s,' %row_Nums1)
        messages = []
        if row_Nums1 <= 1:
            print("Null")
        else:
            row = 1
            for i in range(row_Nums1-1):
                d = {}
                value = sheet2.row_values(i+1)
                messages.append(value)

        return messages

if __name__ == '__main__':
    a = dataLoading.login_data("./gagahi/pc数据.xlsx")
    print(a)
    a = dataLoading.message_data("./gagahi/pc数据.xlsx")
    print(a)


