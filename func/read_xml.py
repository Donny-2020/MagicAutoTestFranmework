from xml.dom.minidom import parse
import os
def readXml(module_name,tage_name):
    files = os.listdir("D:\Projects\MagicAutoTestFranmework\\ui\project\qiqiao\\xml")
    path = "D:\Projects\MagicAutoTestFranmework\\ui\project\qiqiao\\xml"
    for file in files:
        domtree = parse(os.path.join(path,file))
        rootnode = domtree.documentElement
        elements = rootnode.getElementsByTagName(module_name)
        try:
            loc = elements[0].getElementsByTagName(tage_name)[0].childNodes[0].data
        except:
            continue
        return loc
        # if len(elements)>0:
        #     try:
        #         loc = elements[0].getElementsByTagName(tage_name)[0].childNodes[0].data
        #         print(loc)
        #         return loc
        #     except IndexError:
        #         raise IndexError("标签'%s'在xml文件中找不到！！！" %tage_name)
        # else:
        #     raise TypeError("标签'%s'在xml文件中找不到！！！" %module_name)

if __name__=="__main__":
    print(readXml("date","sendValue"))