# -*- coding: utf-8 -*-
"""
    Created on Sat Apr 06 00:28:24 2013
    
    @author: zzcwing
"""

class CNumber:
    def __init__(self):
        self.cdict = {1: '', 2: '拾', 3: '佰', 4: '仟'}
        self.xdict = {1: '元', 2: '万', 3: '亿', 4: '兆'}  # 数字标识符
        self.gdict = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}

    def csplit(self, cdata):  # 拆分函数，将整数字符串拆分成[亿，万，仟]的list
        g = len(cdata) % 4
        csdata = []
        lx = len(cdata) - 1
        if g > 0:
            csdata.append(cdata[0:g])
        k = g
        while k <= lx:
            csdata.append(cdata[k:k+4])
            k += 4
        return csdata

    def cschange(self, cki):  # 对[亿，万，仟]的list中每个字符串分组进行大写化再合并
        lenki = len(cki)
        lk = lenki
        chk = ''
        for i in range(lenki):
            if int(cki[i]) == 0:
                if i < lenki - 1:
                    if int(cki[i + 1]) != 0:
                        chk += self.gdict[int(cki[i])]
            else:
                chk += self.gdict[int(cki[i])] + self.cdict[lk]
            lk -= 1
        return chk

    def cwchange(self, data):
        cdata = str(data).split('.')
        
        cki = cdata[0]  # 整数部分
        ckj = cdata[1] if len(cdata) > 1 else '00'  # 小数部分，若无则补充"00"
        
        chk = ''
        cski = self.csplit(cki)  # 分解字符数组[亿，万，仟]三组List:['0000','0000','0000']
        ikl = len(cski)  # 获取拆分后的List长度
        
        # 大写合并
        for i in range(ikl):
            converted = self.cschange(cski[i])
            if converted:  # 处理全零情况
                chk += converted + self.xdict[ikl - i]

        # 处理小数部分
        if len(ckj) == 1:  # 若小数只有1位
            if int(ckj[0]) == 0:
                chk += '整'
            else:
                chk += self.gdict[int(ckj[0])] + '角整'
        else:  # 若小数有两位的四种情况
            if int(ckj[0]) == 0 and int(ckj[1]) != 0:
                chk += '零' + self.gdict[int(ckj[1])] + '分'
            elif int(ckj[0]) == 0 and int(ckj[1]) == 0:
                chk += '整'
            elif int(ckj[0]) != 0 and int(ckj[1]) != 0:
                chk += self.gdict[int(ckj[0])] + '角' + self.gdict[int(ckj[1])] + '分'
            else:
                chk += self.gdict[int(ckj[0])] + '角整'
        
        return chk


if __name__ == '__main__':
    pt = CNumber()
    num = input("请输入数字金额: ")  # 替代 sys.argv 方式
    print(pt.cwchange(num))