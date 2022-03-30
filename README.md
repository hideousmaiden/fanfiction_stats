# fanfiction_stats

В этом проекте я попробовала обучить натренировать модель для генерации текста на наборе фанфиков с сайта Archive of Our Own.

--> вот ссылка на саму модель: https://drive.google.com/drive/folders/11jJVikGAIkgFHRbgjth8f5C6Z03pqkQf?usp=sharing

--> бот: @garbage_barge_bot

Что я делала:
▲ скачивала данные с сайта, парсила html через BeautifulSoup и регулярки
▲ тексты и метаинформацию записывала в базу данных: название, автор, жанр, дата публикации, возрастное ограничение, теги с именами персонажей, теги с взаимоотношениями, дополнительные теги, статус завершён \ не завершён, количество плюсиков от читателей и собственно превью.
--> это ПРОЕКТ_db.ipynb и voltron.db

▲ обучала модель на наборе "блоков": все теги + превью. Мне было интересно посмотреть, как модель подхватит форматирование тегов и поможет ей наличие большого количества регулярностей в тексте или помешает (В итоге скорее помешало: модель стала почти игнорировать превью и писать только теги. Но гибкость она не потеряла, например, она придумывала несуществующие термины похожие на сленг фикрайтерш)
--> это ПРОЕКТ_model.ipynb 
(блокнот с моделью лучше открывать по ссылке в колабе, потому что так ничего не видно)

▲ сделала датафрейм из базы данных и наделала графиков
--> это ПРОЕКТ_data.ipynb

▲ сделала бот, который присылает нагенерированные моделью обложки фанфиков и графики
(Бот шлёт рандомные тексты из заранее предзаписанного файла, а не дополняет тексты пользователя, потому что если и установить tensorflow, и загрузить модель, то pythonanywhere падает и просит освободить память)
--> это project.py

всё!!
