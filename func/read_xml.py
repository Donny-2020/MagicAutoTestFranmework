from xml.dom.minidom import parse
def readXml(module_name):
    domtree = parse("D:\Projects\MagicAutoTestFranmework\\ui\project\qiqiao\element\\test.xml")
    rootnode = domtree.documentElement
    elements = rootnode.getElementsByTagName("element")
    # method = elements[0].getElementsByTagName("method")[0]
    # re = method.childNodes[0].data
    # if "单行文本" ==
    # print(re)
    for element in elements:
        if module_name == element.getAttribute("name"):
            method = element.getElementsByTagName("method")[0].childNodes[0].data
            loc = element.getElementsByTagName("location")[0].childNodes[0].data
            print(method)
            print(loc)


if __name__=="__main__":
    readXml("singlelinetext")