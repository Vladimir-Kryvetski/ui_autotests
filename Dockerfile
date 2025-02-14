FROM python:3.10-slim AS baseimage
# создание непривелигированного пользователя для большей безопасности
RUN groupadd --gid 1000 RegularUser \
  && useradd --uid 1000 --gid RegularUser --shell /bin/bash --create-home RegularUser
WORKDIR /uitests
COPY requirements.txt /uitests/
# удаление кэша для уменьшения размера образа(для подстраховки dockerignore)
RUN pip install --no-cache-dir -r requirements.txt
COPY . /uitests/
USER RegularUser
CMD [ "pytest", "-k", "p100" ]


