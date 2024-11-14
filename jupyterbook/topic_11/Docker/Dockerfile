FROM continuumio/miniconda3:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user and set up permissions
RUN useradd -m jupyteruser && \
    mkdir -p /workspace && \
    chown -R jupyteruser:jupyteruser /workspace

# Copy environment.yml
COPY --chown=jupyteruser:jupyteruser Docker/environment.yml /workspace/

# Copy contents from the current directory to the user's home directory in the container
COPY --chown=jupyteruser:jupyteruser . /home/jupyteruser/

# Initialize conda for bash and setup jupyter kernel
USER root
RUN conda init bash && \
    conda env create -f /workspace/environment.yml && \
    conda clean -afy && \
    conda run -n jupyter_env python -m ipykernel install --name jupyter_env --display-name "Python (jupyter_env)"

# Set ownership of the conda environment to jupyteruser
RUN chown -R jupyteruser:jupyteruser /opt/conda

# Switch to the non-root user
USER jupyteruser
WORKDIR /workspace

# Set up Jupyter config
RUN mkdir -p /home/jupyteruser/.jupyter && \
    echo "c.NotebookApp.ip = '0.0.0.0'" > /home/jupyteruser/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /home/jupyteruser/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /home/jupyteruser/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /home/jupyteruser/.jupyter/jupyter_notebook_config.py

# Setup conda in jupyteruser's bash profile
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate jupyter_env" >> ~/.bashrc

# Create an entrypoint script
RUN echo '#!/bin/bash\n\
    . /opt/conda/etc/profile.d/conda.sh\n\
    conda activate jupyter_env\n\
    cp -r . ~ && cd ~\n\
    exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser\n\
    ' > /home/jupyteruser/entrypoint.sh && \
    chmod +x /home/jupyteruser/entrypoint.sh

# Add environment variables for conda
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
ENV SHELL=/bin/bash
ENV TERM=xterm

EXPOSE 8888

ENTRYPOINT ["/home/jupyteruser/entrypoint.sh"]