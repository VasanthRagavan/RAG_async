# Use Microsoft Python 3.12 Dev Container base image
FROM mcr.microsoft.com/devcontainers/python:3.12

# Avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Update apt packages and install curl (already present in most base images)
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"
