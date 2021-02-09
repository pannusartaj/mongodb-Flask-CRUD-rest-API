FROM tiangolo/uwsgi-nginx-flask:python3.7

# If STATIC_INDEX is 1, serve / with /static/index.html directly (or the static URL configured)
ENV STATIC_INDEX 0

COPY ./app /app

WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt