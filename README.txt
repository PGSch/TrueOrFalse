Make scripts executeable:
# cd <path>/TrueOrFalse
ls | grep ".sh" | xargs chmod +x

# create file.txt to download and start http server
bash setup.sh

# copy file.txt content to ID_card.txt and output content
bash true_or_false.sh
