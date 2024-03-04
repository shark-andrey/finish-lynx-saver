# Saving FinishLynx Data


## Установка

На виртуалке с сайтом выполни, поменяв `DB_URL`.
Формат: `mysql+asyncmy://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}`

```bash
cd ~
git clone https://github.com/fertilis/finish-lynx-saver.git
cd finish-lynx-saver
cat > .env <<EOT
DB_URL=mysql+asyncmy://root:password@localhost:3306/dev
PORT=10000
EOT
make build
```

## Запуск

```bash
cd ~/finish-lynx-saver && make run
```


## Остановка

```bash
cd ~/finish-lynx-saver && make stop
```

## Логи

```bash
cd ~/finish-lynx-saver && make logs
```
