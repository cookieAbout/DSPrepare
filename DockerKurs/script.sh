#name=$1
#len=${#name}
#first_letter=${name::1}
#rest_letters=${name:1:len}
#if [ -z "$name" ]; then
#    echo "Нужно ввести аргумент"
#    exit 1
#else
#  echo "Hello, ${first_letter^}${rest_letters,,} :)"
#fi

#echo ":)"

if [ ! -e names.txt ]; then
    echo "Не могу найти файл 'names.txt'"
    exit 1
fi
cat names.txt | awk '{print "Hello, "$1}'
