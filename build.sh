cd /root/AlipayMiniApp/

git fetch origin master
git merge origin/master

pip3 install -r requirements.txt

cd aliminiapp

python3 manage.py migrate --settings=aliminiapp.settings_prod
python3 manage.py collectstatic --no-input --settings=aliminiapp.settings_prod

supervisorctl restart aliminiapp

service nginx restart

