-- salam
SELECT CONCAT(
    'CREATE TABLE `', table_name, '` (\n',
    GROUP_CONCAT(
        '  `', column_name, '` ', column_type,
        IF(is_nullable='NO',' NOT NULL',''),
        IF(extra<>'',' ',extra),
        IF(column_default IS NOT NULL, CONCAT(' DEFAULT \'', column_default, '\''),'')
        ORDER BY ordinal_position
        SEPARATOR ',\n'
    ),
    ',\n  PRIMARY KEY(`id`)\n',
    ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;'
) AS create_table_statement
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table'
GROUP BY table_name;
