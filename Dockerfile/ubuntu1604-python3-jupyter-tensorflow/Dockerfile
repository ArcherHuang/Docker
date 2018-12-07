FROM ubuntu:16.04
LABEL MAINTAINER Archer Huang <mmosconii@gmail.com>

# ----------------- #
#   Configuration   #
# ----------------- #
ARG jupyter_port=8888

# ---------------- #
#   Installation   #
# ---------------- #

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends apt-utils
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
            curl \
            xz-utils \
            build-essential \
            libsqlite3-dev \
            libreadline-dev \
            libssl-dev \
            ca-certificates \
            openssl \
            net-tools \
            python3 \
            python3-pip \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN curl https://bootstrap.pypa.io/ez_setup.py -k -o - | python3

WORKDIR /
RUN rm -rf /tmp/ez_setup.py
    
RUN pip3 install --no-cache-dir \
        jupyter

RUN pip3 install tensorflow

# Run service of Jupyter.
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh \
    && ln -s /usr/local/bin/docker-entrypoint.sh 
ENTRYPOINT [ "docker-entrypoint.sh" ]
EXPOSE ${jupyter_port}

CMD [ "jupyter", "--version" ]