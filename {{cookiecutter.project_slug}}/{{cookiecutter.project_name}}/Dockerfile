FROM node:slim AS node_builder

WORKDIR /opt/app

COPY . ./

RUN cd {{cookiecutter.project_slug}}/www \
    && npm i \
    && npm run build

CMD []


FROM python:3.12.4 AS {{cookiecutter.project_slug}}_app

WORKDIR /opt/app

RUN pip install build

COPY . ./

COPY --from=node_builder /opt/app/{{cookiecutter.project_slug}}/www/static/{{cookiecutter.project_slug}}/dist /opt/app/{{cookiecutter.project_slug}}/www/static/{{cookiecutter.project_slug}}/dist


RUN python -m build \
    && pip install dist/{{cookiecutter.project_slug}}-0.0.1-py3-none-any.whl

CMD []