# О проекте
Это репозиторий проекта, разрабатываемого в качестве тестового задания для IT-Solution

Суть проекта - создание скрипта, создающего видео анимированого текста, введеного пользователем. 


# Установка и использование

## Базовый скрипт

Для использования самого скрипта достаточно скачать файл main.py (весь репозиторий клонировать не обязательно) и запустить его:

`` python main.py <текст> <путь_к_выходу_видео.mp4>``

## Веб-сервис

Для хостинга веб-сервиса необходимо склонировать репозиторий и скачать зависимости

```
git clone https://github.com/lunaro-4/text-to-video-web-service.git
cd text-to-video-web-service
python -m venv venv 
venv/bin/pip install -r requirements.txt
```
Вариант без создания виртуальной среды:
```
git clone https://github.com/lunaro-4/text-to-video-web-service.git
cd text-to-video-web-service
pip install -r requirements.txt
```
После этого зпускаем проект django с помощью одной из команд:
Если установка проводилась с созданием виртуальной среды:
```
venv/bin/python ./manage.py
```
Если виртуальная среда не создавалась:
```
python ./manage.py
```
