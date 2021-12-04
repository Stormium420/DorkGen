import sys
sys.dont_write_bytecode = True

class KFT_Dork: #Make a <keyword><pformat><ptype> format dork.
    def __init__(self, pathKeyWords, pathPageType, pathPageFormat):
        self.pathKeyWords = pathKeyWords
        self.pathPageType = pathPageType
        self.pathPageFormat = pathPageFormat

    def createString(self): #Where the actual dorks are made
        keyWordsList = []
        pageTypesList = []
        pageFormatList = []

        #START SPLITTING KEYWORDS
        fileKeyWords = open(self.pathKeyWords)
        for line in fileKeyWords: #Load keywords into keyWordsList
            keyWordsList.append(line.strip()) #Add keyword to list
        fileKeyWords.close()
        #END SPLITTING KEYWORDS

        #START SPLITTING PAGETYPES
        filePageType = open(self.pathPageType)
        for line in filePageType:
            pageTypesList.append(line.strip()) #Add pagetype to list
        filePageType.close()
        #END SPLITTING PAGETYPES

        #START SPLITTING PAGEFORMATS
        filePageFormat = open(self.pathPageFormat)
        for line in filePageFormat:
            pageFormatList.append(line.strip())
        filePageFormat.close()
        #END SPLITTING PAGEFORMATS

        dorkWriter = open("Dorks.txt", "w")
        dorkWriter.truncate(0)

        for Key in keyWordsList:
            for Types in pageTypesList:
                for Format in pageFormatList:
                    dorkWriter.write(f"{Key} {Format} {Types}\n")
