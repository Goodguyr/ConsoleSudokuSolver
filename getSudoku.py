from bs4 import BeautifulSoup as bs
import requests

def getSudoku():
    allRows = []
    listRows = []
    sudokuInfo = []
    filledSudoku = []
    url = "https://www.sudokuweb.org/"
    reader = requests.get(url)
    reader = reader.text
    reader = bs(reader, 'html.parser')
    sudokuDiv = reader.find('div', class_='sudoku nine')
    for rows in sudokuDiv.find_all('tr'):
        rows = str(rows)
        rows = rows.replace("</td>", "")
        rows = rows.replace('<',"")
        rows = rows.replace('"',"")
        rows = rows.replace("line>","")
        rows = rows.replace("</tr>", "")
        rows = rows.replace(" ", "")
        rows = rows.replace("\n\n", "")
        rows = rows.replace(" \n\n\n", "")
        rows = rows.replace("spanclass=","")
        rows = rows.replace(">","")
        rows = rows.replace("tdid=","")
        rows = rows.replace('<"',"")
        rows = rows.replace('">',"")
        rows = rows.replace("/span", "")
        rows = rows.replace("right", "")
        for i in range(1,81):
            replacer = "right" + str(i)
            rows = rows.replace(replacer, "")
        rows = rows.replace("\n",";")
        rows = rows.replace("\xa0","")
        rows = rows.replace("/tr", "")
        rows = rows.replace(";;","")
        for i in range(81):
            num = ";" + str(i) + ";"
            rows = rows.replace(num,";")
        allRows.append(rows)
    for row in allRows:
        listRows.append(row.split(";"))
    for row in listRows:
        oneRow = []
        for square in row:
            if "true" in square:
                oneRow.append(0)
            if "sedy" in square:
                oneRow.append(int(square[-1]))
        sudokuInfo.append(oneRow)
    for row in sudokuInfo:
        oneRow = [row[i:i + 3] for i in range(0, len(row), 3)]
        filledSudoku.append(oneRow)
    return filledSudoku
