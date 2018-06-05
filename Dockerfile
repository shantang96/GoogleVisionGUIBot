FROM ubuntu
COPY . /src
RUN apt-get update
RUN apt-get install python
RUN apt-get install python3-pip
RUN pip3 install python3-xlib
RUN apt-get install scrot
RUN apt-get install python3-tk
RUN apt-get install python3-dev
RUN pip3 install pyautogui
CMD ["python", "/src/GoogleVisionBot.py"]
