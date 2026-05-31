FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD python manage.py migrate && \
    python manage.py load_autoimmune_diseases && \
    python manage.py load_eagleman_brain_mind && \
    python manage.py load_gabor_mate_autoimmune_trauma && \
    python manage.py load_nietzsche_beyond_good_evil && \
    python manage.py load_psychedelics_guide && \
    python manage.py load_peterson_be_a_monster && \
    python manage.py load_peterson_face_weakness && \
    python manage.py load_robert_greene_law_of_human_nature && \
    gunicorn max_health.wsgi --log-file -
