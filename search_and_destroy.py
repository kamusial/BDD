import os

#pierwsza metoda.... znaleźć pliki, wyciągnąć ścieżki i skasować. Nieskończone - bez sensu ;)
# os.system('cmd /c "cd C://Users//kamusial//Desktop && dir /s *.pcap >> result.txt"')
#
# with open ('C://Users//kamusial//Desktop//result.txt', 'r', encoding='ANSI') as search_pcap:
#     content = search_pcap.readlines()

#2ga metoda - komenda del /S *.pcap w terminalu
os.system('cmd /c "cd C://Users//kamusial//Desktop && del /S *.pcap"')


