if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Apnamovi/PaidRepo.git /PaidRepo
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /PaidRepo
fi
cd /PaidRepo
pip3 install -U -r requirements.txt
echo "Starting JK DEVELOPER BoT...."
python3 bot.py
