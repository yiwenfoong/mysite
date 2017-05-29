<<<<<<< HEAD
def getdata():
    #Authentication parameters
    headers = { 'AccountKey' : 'xCAGHu5NSIK88QUz4Crh5w==',
    'accept' : 'application/json'} #this is by default

    #API parameters
    uri = 'http://datamall2.mytransport.sg/' #Resource URL
    path = '/ltaodataservice/Traffic-Images'
    #Build query string & specify type of API call
    target = urlparse(uri + path)
    #print (target.geturl()) #checking

    #Get handle to http
    h = http.Http()
    #Obtain results
    response, content = h.request(target.geturl(),'GET','',headers)

    #json.loads changes 'content' (json file) into Dict file
    jsonObj = json.loads(content.decode("utf-8")) #decode changes content byte into string type
    #print (jsonObj['value'][0]['ImageLink'])
    #print (len(jsonObj['value']))
    return jsonObj

def imagelink(jsonObj):
    imagelist = []
    i=0

    while i < 50:
        if jsonObj['value'][i]['CameraID'] == '2701':
            imagelist.append(jsonObj['value'][i]['ImageLink'])
        if jsonObj['value'][i]['CameraID'] == '2702':
            imagelist.append(jsonObj['value'][i]['ImageLink'])
        if jsonObj['value'][i]['CameraID'] == '2704':
            imagelist.append(jsonObj['value'][i]['ImageLink'])
        #imagelist.append(jsonObj['value'][1]['ImageLink'])
        i = i + 1
    return imagelist
=======
def getdata():
    #Authentication parameters
    headers = { 'AccountKey' : 'xCAGHu5NSIK88QUz4Crh5w==',
    'accept' : 'application/json'} #this is by default

    #API parameters
    uri = 'http://datamall2.mytransport.sg/' #Resource URL
    path = '/ltaodataservice/Traffic-Images'
    #Build query string & specify type of API call
    target = urlparse(uri + path)
    #print (target.geturl()) #checking

    #Get handle to http
    h = http.Http()
    #Obtain results
    response, content = h.request(target.geturl(),'GET','',headers)

    #json.loads changes 'content' (json file) into Dict file
    jsonObj = json.loads(content.decode("utf-8")) #decode changes content byte into string type
    #print (jsonObj['value'][0]['ImageLink'])
    #print (len(jsonObj['value']))
    return jsonObj

def imagelink(jsonObj):
    imagelist = []
    i=0

    while i < 50:
        if jsonObj['value'][i]['CameraID'] == '2701':
            imagelist.append(jsonObj['value'][i]['ImageLink'])
        if jsonObj['value'][i]['CameraID'] == '2702':
            imagelist.append(jsonObj['value'][i]['ImageLink'])
        if jsonObj['value'][i]['CameraID'] == '2704':
            imagelist.append(jsonObj['value'][i]['ImageLink'])
        #imagelist.append(jsonObj['value'][1]['ImageLink'])
        i = i + 1
    return imagelist
>>>>>>> 5b744b5dacc4eec2022b27003b68580972539abf
