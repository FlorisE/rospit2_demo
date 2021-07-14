FROM ros:foxy

ADD https://api.github.com/repos/FlorisE/rospit2_demo/git/refs/heads/main version.json

RUN git clone https://github.com/FlorisE/rospit2_demo
