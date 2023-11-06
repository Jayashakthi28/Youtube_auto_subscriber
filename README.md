# Youtube auto subscriber

### This script helps you to subscribe to your favourite youtube channels by saving you some time

### Things you need :
- Firefox Browser
- Python
- A decent internet connection
- A list of youtube channnel URLs
  
### Tutorial :
- Install the required packages
- Find the profile folder for mozilla firefox in which the target Google account is already signed in.
- For eg: The profile folder in Manjaro Firefox is located in `/home/username/.mozilla/firefox/ba2uc9zw.default-release`
- Replace the firefox profile folder in the `firefoxProfileFolder` variable of the `sub.py` file
- Run the `sub.py` file

### Get Old Youtube account Data :
- Visit [Google Takeout](https://takeout.google.com/) and signin in with your old account.
- Select Youtube and youtube music.
- Click on Export.
- You will get a link to download the data in your email.

### Commands :
```sh 
git clone git@github.com:Jayashakthi28/Youtube_auto_subscriber.git
cd Youtube_auto_subscriber
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
python sub.py
```

## Give a Star if you like it