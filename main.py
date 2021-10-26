from bs4 import BeautifulSoup
import requests, statistics
twenty_url = "https://www.tfrrs.org/results/xc/17574"
nineteen_url = "https://www.tfrrs.org/results/xc/16685"
eighteen_url = "https://www.tfrrs.org/results/xc/14964"
race1 = 2
race2 = 4

def get_times(url, table_number):
    html_code = requests.get(url).text
    html_data = BeautifulSoup(html_code, "lxml")
    mens_race = html_data.find_all("table")[table_number-1]
    racers = []
    for row in mens_race.find_all('tr'):
        person =[]
        for column in row.find_all('td'):
            person.append(column.text.strip())
        racers.append(person)
    racers = racers[1:]
    times = []
    for racer in racers:
        times.append(racer[5])
    return(times)

def convert_to_seconds(times):
    list_in_seconds = []
    for time in times:
        if time != 'DNF' and time != 'DNS':
            mins = time[0] + time[1]
            seconds = time[3] + time[4]
            tenth = time[6]
            seconds= (int(mins)*60)+int(seconds)+(int(tenth)/10)
            list_in_seconds.append(seconds)
    return(list_in_seconds)

times = get_times(eighteen_url, race2) ###Change these inputs to get desired results
list_in_seconds = convert_to_seconds(times)
print ('SD: '+ str(statistics.stdev(list_in_seconds)))