-- lists all genres from database and display the number of shows linked to each
-- second cooment

SELECT `tv_genres`.`name` as genre, COUNT(*) AS number_of_shows
FROM `tv_genres`
INNER JOIN `tv_show_genres`
ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
GROUP BY `tv_show_genres`.`genre_id`
ORDER BY `number_of_shows` DESC;
