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
DB・テーブル作成時のみ
`from app import db`
`db.create_all()`

作成ができないので現在調査中