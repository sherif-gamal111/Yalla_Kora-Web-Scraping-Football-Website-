import requests 
from bs4 import BeautifulSoup 
import csv

date = input("Please enter the data in the following formate MM/DD/YYY: ")
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")

def main(page):

    # content --> it contains the source code for this page, but in bytecode code
    src = page.content 

    # parsing the byte code --> turns the byte code into a code we can read and deal with it
    soup = BeautifulSoup(src, "lxml") # the "lxml" is the parser

    matches_details = []

    championships = soup.find_all("div", {"class" : "matchCard"})

    def get_match_info(championships):
        
        championship_title = championships.contents[1].find("h2").text.strip() 

        all_matches = championships.contents[3].find_all("div", {"class" : "liItem"}) 

        number_of_matches = len(all_matches)
        
        for i in range (number_of_matches):
            # get teams names
            team_A = all_matches[i].find("div", {"class" : "teamA"})
            team_B = all_matches[i].find("div", {"class" : "teamB"})

            # get match result
            match_result = all_matches[i].find("div", {"class" : "MResult"}).find_all("span", {"class" : "score"})
            score = f"({match_result[0].text.strip()} - {match_result[1].text.strip()})"

            # get match time
            match_time = all_matches[i].find("div", {"class" : "MResult"}).find("span", {"class" : "time"})

            # get the channel that broadcasts the match
            match_channel = all_matches[i].find("div" , {"class" : "icon-channel"})

            # get match status/duration
            match_status_duration = all_matches[i].find("div" , {"class" : "matchStatus"})
            
            # get match status/championship
            match_status_championship = all_matches[i].find("div" , {"class" : "date"})

            # add match info to matches_details[]
            matches_details.append({
                "Championship Type" : championship_title,
                "Match Status/Championship" : match_status_championship.text.strip() if match_status_championship else "غير محدد",
                "Team A" : team_A.text.strip() if team_A else "غير محدد",
                "Team B" : team_B.text.strip() if team_B else "غير محدد",
                "Match Time" : match_time.text.strip() if match_time else "غير محدد",
                "Match Score" : score,
                "Broadcasting Channel" : match_channel.text.strip() if match_channel else "غير محدد",
                "Match Status/Duration" : match_status_duration.text.strip() if match_status_duration else "غير محدد"
            })

    for i in range (len(championships)):
        get_match_info(championships[i]) 

    keys = matches_details[0].keys()

    # CSV writer is trying to write Arabic characters (from YallaKora) using the default Windows encoding (cp1252), which can’t handle Arabic.
        # which does not work, so we have to add encoding="utf-8-sig", newline="" so CSV could write Arabic characters
    with open (r"D:\Important\Programming\Data\Data_Engineering\Web Scraping\codzila\first_project\YallaKoraProject.csv", "w", encoding="utf-8-sig", newline="") as project_file:
        dict_writer = csv.DictWriter(project_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("File is created")


main(page)
