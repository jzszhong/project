import re

def getQueryMap():
    q1 = open('topics.51-100', 'r').read()
    q2 = open('topics.101-150', 'r').read()
    q3 = open('topics.151-200', 'r').read()
    
    files = [q1, q2, q3]
    queryMap = {}
    
    idPattern = re.compile(r'Number:\s*([0-9]+)\s*\n?')
    
    for file in files:
        ids = idPattern.findall(file)
        queries = []
        
        file = file.replace('Topic:', 'SplitPoint')
        file = file.replace('<desc>', 'SplitPoint')
        splitedFile = file.split('SplitPoint')
        
        for part in splitedFile:
            if ('<title>' not in part) and ('Description:' not in part):
                queries.append(part.strip('\n'))
        
        for i in range(len(ids)):
            queryMap[ids[i]] = queries[i].strip(' ')
            
    return queryMap
        
def writeFormalQueryFile(queryMap, filePath):
    file = open(filePath, 'w')
    
    for queryId in queryMap:
        if int(queryId) < 100:
            file.write('<top>\n<num>' + queryId[1:] + '</num><title>\n')
        else:
            file.write('<top>\n<num>' + queryId + '</num><title>\n')
        file.write(queryMap[queryId])
        file.write('\n</title>\n</top>\n')
        
    file.close()

if __name__ == '__main__':
    writeFormalQueryFile(getQueryMap(), 'topics.trec')
