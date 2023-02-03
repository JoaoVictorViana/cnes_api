FROM ubuntu:22.10

RUN mkdir /app

WORKDIR /app

COPY . .

RUN apt update

RUN apt install -y python3-pip

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
