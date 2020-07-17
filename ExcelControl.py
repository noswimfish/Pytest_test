# -*- coding:utf-8 -*-
import xlrd

class ExcelControl(object):
    def __init__(self):
        self.mod = 0

    def open_excel(self,file,mod=0):
        '''
        *打开指定路径的Excel文件*

        | *参数*　 | *类型* | *描述* |
        | file | string | 要读的Excel路径 |
        | mod | int | mod用来区分后面获取Excel表格的值是根据行号和列号获取还是 根据指定的Key，默认值是0，即获取值是根据 （1，2）即表示获取一行二列单元格的值，如果mod是1，获取值应该是（'key1','key2'）即表示从行中key1和列中的key2获取单元格的值 |


        | *返回值*　 | *描述* |
        | None   | 返回空 |

        *--Robot Example--*
        | Open Excel | ./data.xlsx |
        '''
        self.workbook = xlrd.open_workbook(file,encoding_override='utf-8')
        self.mod = int(mod)

    def getNormalNum(self,num):
        value = int(num)
        value = value -1
        return value

    def read_excel_sheet_value_with_key_name(self,sheetName,rowKeyName,colKeyName):
        '''
        *获取在指定Sheet下的指定行的Key和指定列的Key的单元格值（mod必须等于1）*

        | *参数*　 | *类型* | *描述* |
        | sheetName  | string | 指定 Sheet |
        | rowKeyName | string | 指定行的Key，第一列的值 |
        | colKeyName | string | 指定列的Key，第一行的值 |


        | *返回值*　 | *描述* |
        | data   | 返回 |

        *--Robot Example--*
        | Read Excel Sheet Value With Key Name | Sheet1 | key1 | key2 |
        '''
        if self.mod != 1:
            raise AssertionError("The operate excel mod should be '1',current mod is %s" % self.mod)
        worksheet = self.workbook.sheet_by_name(sheetName)
        rown = self.getRowKeyName(rowKeyName,worksheet)
        coln = self.getColKeyName(colKeyName,worksheet)

        cell = worksheet.cell_value(rown, coln)
        return cell

    def getRowKeyName(self,rowKeyName,worksheet):
        rown = -1
        for num in range(0, 100):
            cell = worksheet.cell_value(num, 0)
            if cell == rowKeyName:
                rown = num
                break
        if rown == -1:
            raise AssertionError("Can not find the row,keyName is %s" % rowKeyName)
        return rown

    def getColKeyName(self,colKeyName,worksheet):
        coln = -1
        for num in range(0, 100):
            cell = worksheet.cell_value(0, num)
            if cell == colKeyName:
                coln = num
                break
        if coln == -1:
            raise AssertionError("Can not find the col,keyName is %s" % colKeyName)
        return coln

    def read_excel_sheet_value(self,sheetName,rown,coln):
        '''
        *获取在指定Sheet下的指定行号和指定列号的单元格值（mod必须等于0）*

        | *参数*　 | *类型* | *描述* |
        | sheetName  | string | 指定 Sheet |
        | rown | string | 行号 |
        | coln | string | 列号 |


        | *返回值*　 | *描述* |
        | data   | 返回 |

        *--Robot Example--*
        | Read Excel Sheet Value | Sheet1 | 3 | 2 |
        '''
        if self.mod != 0:
            raise AssertionError("The operate excel mod should be '0',current mod is %s" % self.mod)
        worksheet = self.workbook.sheet_by_name(sheetName)
        cell = worksheet.cell_value(self.getNormalNum(rown), self.getNormalNum(coln))
        return cell

    def read_excel_sheet_values_with_columns(self,sheetName,rown,colns):
        if self.mod != 0:
            raise AssertionError("The operate excel mod should be '0',current mod is %s" % self.mod)
        worksheet = self.workbook.sheet_by_name(sheetName)
        data = []
        for coln in colns:
            value = worksheet.cell_value(self.getNormalNum(rown), self.getNormalNum(coln))
            data.append(value)
        return data

    def read_excel_sheet_values_with_rows_columns(self,sheetName,rowns,colns):
        if self.mod != 0:
            raise AssertionError("The operate excel mod should be '0',current mod is %s" % self.mod)
        worksheet = self.workbook.sheet_by_name(sheetName)
        datas = []
        for row in rowns:
            data = []
            for coln in colns:
                value = worksheet.cell_value(self.getNormalNum(row), self.getNormalNum(coln))
                data.append(value)
            datas.append(data)
        return datas

if __name__ == '__main__':
    excelControl = ExcelControl()
    excelControl.open_excel('C:/Users/MG01730/Desktop/test.xlsx')
    #value = excelControl.read_excel_sheet_value('Sheet1',1,2)
    #print value

