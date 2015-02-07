echo "SHOW TABLES" | python manage.py dbshell > /tmp/tables
for t in $(cat /tmp/tables) ; do
    echo $t
    SQL="ALTER TABLE $t CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci"
    echo ${SQL}
    echo ${SQL} | python manage.py dbshell
done
