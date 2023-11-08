COPY anime_list(anime_id, title, title_english,title_japanese,title_synonym,image_url, type, source, episodes, status, airing, airing_string, aired, duration, rating, score, scored_by, rank, popularity, members, favorites, background, premiered,broadcast, related, producer, licensor, studio, genre, opening_theme, ending_theme)
FROM 'C:\Users\jorda\OneDrive\Desktop\CS RIT\Intro to Big Data\Project\AnimeList.csv'
DELIMITER ','
CSV HEADER;