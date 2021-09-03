# secrets to be set before running script:
# MYSQL_DATABASE
# MYSQL_ROOT_PASSWORD

if [ -z $MYSQL_ROOT_PASSWORD ] || [ -z $MYSQL_DATABASE ] || [ -z $DATABASE_URI ]
then
    echo " one or more environment variables have not been set"
    exit 1
fi

sed \
    -e 's,{{DATABASE_URI}},$DATABASE_URI,g;' \
    -e 's,{{MYSQL_DATABASE}},$MYSQL_DATABASE,g;' \
    -e 's,{{MYSQL_ROOT_PASSWORD}},$MYSQL_ROOT_PASSWORD,g;' secrets.yaml | kubectl apply -f -
