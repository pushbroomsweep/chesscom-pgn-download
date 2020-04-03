import requests
username = 'z3ppj1g5aw'
start_month = 1
start_year = 2011
end_month = 11
end_year = 2017
# https://api.chess.com/pub/player/z3ppj1g5aw/games/2017/11/pgn

def months(start_month, start_year, end_month, end_year):

    monthlist = []
    month, year = end_month, end_year

    while (year, month) >= (start_year, start_month):

        str = format(year) + '/' + '{:02d}'.format(month)
        monthlist.append(str)

        month -= 1
        if month < 1:
            month = 12
            year -= 1
    
    return monthlist

monthlist = months(start_month, start_year, end_month, end_year)

fname = "ChessCom_" + username + ".pgn"

for i in range(0,len(monthlist)):
    print(monthlist[i])
    url_string = "https://api.chess.com/pub/player/" + username + "/games/" + monthlist[i] + "/pgn"
    r = requests.get(url_string)
    with open(fname,'ab') as f:
        f.write(r.content)
    f.close()


# url_string = "https://api.chess.com/pub/player/" + username + "/games/" + 2017/11 + "/pgn"
# r = requests.get()
