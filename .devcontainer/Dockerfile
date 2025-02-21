# Using the Ubuntu image (our OS)
FROM ubuntu:latest

# Update package manager (apt-get) 
# and install (with the yes flag `-y`)
# Python and Pip
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-venv \
    python3-pip

# # Set working directory in the container
# WORKDIR /workspace

# # Copy files from the host to the container
# COPY ../ /workspace

# Make the script executable
# RUN chmod +x /workspace/scripts/setup.sh
