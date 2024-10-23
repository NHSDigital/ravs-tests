FROM python:3.11

RUN apt-get update && apt-get install -y \
    curl \
    default-jre \
    default-jdk \
    libgtk-3-0 \
    libgbm-dev \
    libxkbcommon-x11-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libnss3 \
    libnspr4 \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    fonts-noto-core \
    fonts-noto-hinted \
    fonts-noto-ui-core \
    fonts-noto-unhinted

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install tox \
    && pip install --upgrade playwright \
    && playwright install \
    && playwright install --force chrome \
    && playwright install --force msedge \
    && playwright install --force webkit \
    && playwright install-deps \
    && curl -o allure-commandline-2.17.3.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.17.3/allure-commandline-2.17.3.tgz \
    && tar -zxvf allure-commandline-2.17.3.tgz -C /opt/ \
    && ln -s /opt/allure-2.17.3/bin/allure /usr/bin/allure \
    && rm -rf allure-commandline-2.17.3.tgz \
    && allure --version

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
&& locale-gen "en_GB.UTF-8"
ENV LANG=en_GB.UTF-8 \
    LANGUAGE=en_GB:en \
    LC_ALL=en_GB.UTF-8


# Expose port for Allure server
EXPOSE 5050

COPY . .

# Update the entrypoint to start both Allure server and tox
ENTRYPOINT ["tox"]
# ENTRYPOINT [ "bash" ]