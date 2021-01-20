import subprocess
import schedule
import datetime
import sys
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

sys.path.append(os.path.join(BASE_DIR, 'bubbles'))
for x in sys.path:
    print(x)
# sys.path.append(os.path.dirname(os.path.abspath('FloatSpiderProject')))
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'FloatDjangoProject.settings'
import django
django.setup()
from bubbles.models import Ettoday
def crawl_work():
    subprocess.Popen('scrapy crawl ettoday_spider')
    Ettoday.delete_repeat()


if __name__ == '__main__':
    schedule.every().day.at("10:30").do(crawl_work)
    print('目前時間{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    while True:
        schedule.run_pending()