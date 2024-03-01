Hello World!
This is our first project in NYM ecosystem - Nym Helper Bot. It is a Telegram bot. It can navigate you through mixnodes ecosystem, connect with our AI-support or show you our Youtube guides.
Also it can track chosen node by several parameters such as active/inactive, routing score, saturation etc...

Hope it will help newbies to integrate in NYM ecosystem a little bit easier...
                                TopsecretDAO squad.

Парсер с сайта

Пакеты для установки

node.js, express.js, typescript (https://blog.logrocket.com/how-to-set-up-node-typescript-express/),

cheerio, puppeteer, cors,

npm install cheerio puppeteer cors

Запуск

Ввести команду npx ts-node src/index.ts

Перейти на сайт(https://reqbin.com/)

В строке url-адреса сервера ввести
http://localhost:8000/routingScore

Выбрать POST-запрос

Выбрать JSON(application/json)

в качестве тела написать

{"name": "Здесь нудно указать ID ноды, от которой мы получаем routing score"}

обратить внимание на терминал, там появится routing score

