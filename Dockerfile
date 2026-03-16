FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    unzip \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN wget -qO - https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
USER jenkins