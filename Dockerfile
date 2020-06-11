FROM debian:bullseye
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Install software
RUN apt update && \
    apt install --no-install-recommends -y \
        ca-certificates \
        git \
        golang \
        librtlsdr-dev \
        python3-paho-mqtt \
        rtl-sdr && \
    rm -rf /var/lib/apt/lists/*
RUN go get github.com/bemasher/rtlamr

# Copy files into place
COPY * /amridm2mqtt/
COPY settings_docker.py /amridm2mqtt/settings.py

# Set the entrypoint
ENTRYPOINT ["/amridm2mqtt/amridm2mqtt"]
