highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list =  highlighted_poems.split(',')
# print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  poems_stripped = poem.strip()
  highlighted_poems_stripped.append(poems_stripped)

# print(highlighted_poems_stripped)

highlighted_poems_details = []
for poems in highlighted_poems_stripped:
  print(poems)

highlighted_poems_details = []
for poems in highlighted_poems_stripped:
  highlighted_poems_details.append(poems.split(':'))

titles, poets, dates = [], [], []
for detail in highlighted_poems_details:
  titles.append(detail[0])
  poets.append(detail[1])
  dates.append(detail[2])

for title, poet, date in zip(titles, poets, dates):
  card = "The poem {} was published by {} in {}.".format(title, poet, date)
  print(card)


  