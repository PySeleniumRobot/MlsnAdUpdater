# MlsnAdUpdater

Робот автоматического обновления объявлений на сайте mlsn.ru

## Установка

### Установить python

Сказать с сайта (https://www.python.org/downloads/windows/) и установить.

### Установить зависимости

Запустить PowerShell и выполнить команду

```PowerShell
pip install selenium
```

### Скачать архив с последней версией скрипта Python

Скачать архив с последней версией скрипта по ссылке (https://github.com/PySeleniumRobot/MlsnAdUpdater/archive/master.zip). Распаковать в локальную папку.

### Обновить selenium driver

Скачать последний стабильный релиз со страницы (https://chromedriver.chromium.org/home).

Скачивается zip архив с единственным файлом внутри "chromedriver.exe". Его нужно скопировать в папку со скриптом "UpdateMlsnAd.py".

## Подготовка к запуску

Открыть файл ./UpdateMlsnAd.py и вписать свой логин и пароль к сайту MLSN

```Python
#Load configuration
MLSNLogin = "<login>"
MLSNPass  = "<pass>"
```

## Запуск

Запустить PowerShell и выполнить команду

```PowerShell
cd "<путь к папке со скриптом>"
& python ./UpdateMlsnAd.py
```
