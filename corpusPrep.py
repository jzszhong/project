import os

def prepCorpus(inputFileDir, targetFilePath):
    def extractText(file):
        text = ''
        lines = file.split('\n')
        
        extract = False
        for line in lines:
            if extract:
                if line != '</TEXT>':
                    text += line
                    text += ' '
                else:
                    extract = False
            if line == '<TEXT>':
                extract = True

        return text

    def removeNoise(text):
        noise = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                 '+', '=', '{', '}', '[', ']', ':', ';', '"', '<', '>', '?',
                 ',', '.', '/', "'s", "'", '1', '2', '3', '4', '5', '6', '7',
                 '8', '9']

        for c in noise:
            text = text.replace(c, '')

        return text.lower()

    inputFilePaths = os.listdir(inputFileDir)
    targetFile = open(targetFilePath, 'w')

    for inputFilePath in inputFilePaths:
        inputFile = open(inputFileDir+'/'+inputFilePath, 'r').read()
        text = removeNoise(extractText(inputFile)).split(' ')

        for word in text:
            targetFile.write(word + ' ')

# Prepare the corpus, must be executed in the directory outside the AP8889 folder
prepCorpus('AP8889', 'AP8889text')
    
