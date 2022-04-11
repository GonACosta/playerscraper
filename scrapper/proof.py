import re
from traceback import print_tb
import urllib.parse
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


listOfTeams = []
listOfPlayers = [[]]
searchFW = True
#get the response from a url and parse it
def setupLink(suffix="comps/32/Primeira-Liga-Stats"):
    #set url to fbref + suffix (PT L1 by default)
    url = 'https://fbref.com/en/path' 
    q = urllib.parse.urljoin(url,suffix)
   
    #response from url
    r = requests.get(q)

    #parse the response in html format
    soup=BeautifulSoup(r.content, "html.parser")
    
    #return the parsed response ready to be explored
    return soup
 
 
#explores the parsed object and looks for teams' links 
def findTeams(resp):
    
    #find containers of features
    divs = resp.findAll('div')
    

    #find teams table 
    counter=0
    for div in divs:       
        table=div.find('div',id='all_results112691')
        if table == None:
           continue
        table1=table.find('div',id='switcher_results112691')
        table2=table1.find('table',id="results112691_overall")
        table3=table2.find('tbody')
        table4=table3.findAll('tr')
        counter+=1
        
        #find links
        for row in table4:    
            if counter == 1:   
                cur=row.find(class_="left").find('a')['href'] 
                listOfTeams.append(cur) 
          


#finds the players and builds their stats         
def findPlayers(): 
        teamCounter=0
        for teamSuffix in listOfTeams:
            teamCounter+=1
            soup=setupLink(teamSuffix)
            
            divs=soup.findAll('div')  
            
            counter=0
            for div in divs:
                table=div.find('div',id='all_stats_standard')
                if table == None:
                    continue                
                table1=table.find('div',id='div_stats_standard_11269')
                table2=table1.find('table',id="stats_standard_11269")
                table3=table2.find('tbody')
                table4=table3.findAll('tr')
                counter+=1
                listOfPlayers.extend
                
                if counter == 1:  
                    auxlist=[] 
                    for row in table4:  
                        cur=row.find(class_="left").find('a')['href'] 
                        fieldRole = row.find(class_="center").contents
                        if ("FW" not in fieldRole) & searchFW :
                            continue
                        auxlist.append(cur)
                    listOfPlayers.insert(teamCounter,auxlist)   

                                 
def getDataFromPlayerPage():
    for playerSuffixes in listOfPlayers:
        for playerSuffix in playerSuffixes:
            if isinstance(playerSuffix,str)==False:
                continue
            soup=setupLink(playerSuffix)
            
            divs=soup.findAll('div')  
            for div in divs:
                    table=div.find('div',id='all_stats_standard')
                    if table == None:
                        continue                
                    table1=table.find('div',id='div_stats_standard_11269')
                    table2=table1.find('table',id="stats_standard_11269")
                    table3=table2.find('tbody')
                    table4=table3.findAll('tr')
                    counter+=1
                    listOfPlayers.extend
                    
                    if counter == 1:  
                        auxlist=[] 
                        for row in table4:  
                            cur=row.find(class_="left").find('a')['href'] 
                            auxlist.append(cur)
                        listOfPlayers.insert(teamCounter,auxlist)
        
def savePlayerStats():
     #TODO
     pass
    
    
#runs the prog
if __name__ == '__main__':
    print("Are you searching only for forwards?(Y/n)")
    #TODO: PROCESS TYPE OF FIELDROLE TO SEARCH FOR
    soup=setupLink()
    findTeams(soup)
    findPlayers()
    getDataFromPlayerPage()      

    counter=0
    for i in listOfTeams:
        print("\n")
        counter+=1
        print(i)
        for p in listOfPlayers[counter]:
            print("\t",p)
            
    


        

    
    

