import urllib
import  urllib2
import os
import re
import tool
__author__ = "__Mike__"

class Spider():
    def __init__(self):
        self.siteURL = 'mm.taobao.com/json/request_top_list.htm'
        self.tool = tool.Tool()
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append(item[0],item[1],item[2],item[3],item[4])
            return contents
    def getDetailPage(self,infoURL):
        response = urllib2.openurl(infoURL)
        return response.read()
    def getBrief(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result = re.search(pattern,page)
        return self.tool.replace(result.group(1))
    def getAllImg(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        content = re.search(pattern,page)
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg,content.group(1))
        return images
    def saveImgs(self,images,name):
        number = 1
        print "Found",name,"Total",len(images),"Pictures"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = "jpg"
            fileName = name + "/" +str(number) + "." + fTail
            self.saveImg(imageURL,fileName)
            number += 1
    def saveIcon(self,iconURL,name):
        splitPath  = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon" + fTail
        self.saveImg(iconURL,fileName)

    def saveBrief(self,content,name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName,"w+")
        print "Saving",fileName
        f.write(content)

    def saveImg(self,imageURL,fileName):
        u = urllib2.urlopen(imageURL)
        data = u.read()
        f = open(fileName,"wb")
        f.write(data)
        print "Saving another",fileName
        f.close()

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print "Create",path,"Folder"
            os.makedirs(path)
            return True
        else:
            print "Created",path,"'s folder"
            return False

    def savePageIofo(self,pageIndex):
        contents = self.getContents(pageIndex)
        for item in contents:
            print "Found a model",item[2]
            print "Saving",item[2]
            detailURL = item[0]
            detailPage = self.getDetailPage(detailURL)
            brief = self.getBrief(detailPage)
            images = self.getAllImg(detailPage)
        self.mkdir(item[2])
        self.saveBrief(brief,item[2])
        self.saveIcon(item[1],item[2])
        self.saveImgs(images,item[2])

    def savePageInfo(self,start,end):
        for i in range(start,end+1):
            self.savePageInfo(i)

spider = Spider()
spider.savePageInfo(2,10)
