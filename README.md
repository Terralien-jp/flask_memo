# flask_memo
Flask Markdown Memo

docker-compose up -d

## gomisouji
```bash
docker-compose down -v
docker rmi $(docker images -q)
docker system prune
```

### SQLite3
Python console
DB・テーブル作成時のみ /appディレクトリ内で
```
python
from app import db
db.create_all()
```
templates, staticディレクトリの場所ミスった模様、検証の後確定