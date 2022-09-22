from publick import dellExcel,DellFirefox

class DictDELL():
    def dell(self):
        caseParameter = eval(dellExcel.ExcelDell().getCase('参数',0))
        element_key = []
        done_key = []
        for key in caseParameter:
            for fist_key in caseParameter[key]:
                element_key = [key,fist_key,caseParameter[key][fist_key]]

            done_key.append(element_key)
        return done_key
if __name__ == "__main__":
    aa = DictDELL().dell()
    print(aa)