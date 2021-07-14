FROM ros:foxy

RUN mkdir /workspace

ADD https://api.github.com/repos/FlorisE/rospit2_demo/git/refs/heads/main rospit2_demo_version.json

RUN git clone https://github.com/FlorisE/rospit2_demo && \
    cp -r /rospit2_demo/* /workspace

ADD https://api.github.com/repos/FlorisE/rospit2/git/refs/heads/main rospit2_version.json

RUN git clone https://github.com/FlorisE/rospit2/ && \
    cp -r /rospit2/src/* /workspace

WORKDIR /workspace
