-- Lists shows without a genre linked
-- Filtered by NULL genre_id
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
