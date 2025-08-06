# BrendUserbot T.me/BrendUserbot

FROM brendsup/brenduserbot:latest
RUN git clone https://github.com/husudu/Hus.git /root/Hus
WORKDIR /root/Hus/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
