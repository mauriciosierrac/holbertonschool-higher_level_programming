-- list all the cities of california in hbtn usa BD
SELECT id, name
FROM cities
WHERE state_id IN (
	SELECT id
	FROM states
	WHERE name = "California"
)
ORDER BY id;
