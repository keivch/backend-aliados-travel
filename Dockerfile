FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN python -c "from pathlib import Path; p = Path('requirements.txt'); data = p.read_bytes(); p.write_text(data.decode('utf-16') if data.startswith((b'\xff\xfe', b'\xfe\xff')) else data.decode('utf-8-sig'), encoding='utf-8')" \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["flask", "run"]
