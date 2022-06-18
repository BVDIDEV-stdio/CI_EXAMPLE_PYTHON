FROM python:3.9
WORKDIR /code/
COPY req.txt ./
RUN pip install -r req.txt
COPY main.py ./
CMD [ "python", "main.py" ]
