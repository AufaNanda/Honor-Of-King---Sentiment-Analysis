from google_play_scraper import reviews_all, Sort
import pandas as pd
import csv

# Scraping 
print("Mulai scraping review dari Google Play Store...")
Scrap_HOK = reviews_all(
    "com.levelinfinite.sgameGlobal",
    lang="id",
    country="id",
    sort=Sort.MOST_RELEVANT
)
print(f"Berhasil scraping {len(Scrap_HOK)} review!")

# Save the comment text on HOK_comment.csv
with open('HOK_comment.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in Scrap_HOK:
        writer.writerow([review['content']])

print("HOK_comment.csv berhasil disimpan!")

# Save all the fiture comment to Hok_playstore.csv
df = pd.DataFrame(Scrap_HOK)
df.to_csv('Hok_playstore.csv', index=False)

print("Hok_playstore.csv berhasil disimpan!")
print(f"Total review: {len(df)}")
print(f"Kolom: {list(df.columns)}")
