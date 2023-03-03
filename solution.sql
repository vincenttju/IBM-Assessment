SELECT o.owner_id, o.owner_name, COUNT(DISTINCT c.category_id) as "different_category_count"
FROM owner o, article a, category_article_mapping c
WHERE o.owner_id = a.owner_id AND  a.article_id = c.article_id
ORDER BY COUNT(DISTINCT c.category_id) DESC
GROUP BY o.owner_id