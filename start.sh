#!/bin/bash

if [ -d "data" ]; then
  echo "Папка data уже существует."
else
  mkdir data
fi

if [ -f "data/vk_bot_def_company.db" ]; then
  echo "База данных vk_bot_def_company.db уже существует."
else
  python3 init_db.py
  python3 seed_data.py

python3 boy.py
