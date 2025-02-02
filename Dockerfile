FROM python:3.13.1-bookworm

RUN pip install --upgrade pip

ENV ROBOFLOW_API_KEY=pmYGAawja0bc61QUy0rH
ENV ROOT_FOLDER=/workspaces/rooftop

COPY . /workspaces/rooftop

WORKDIR /workspaces/rooftop

