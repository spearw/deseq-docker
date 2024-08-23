# Pin base image
# Base image https://hub.docker.com/_/r-base
# Latest version of R compatible with Bioconductor 3.19 is 4.4.1
FROM r-base:4.4.1
LABEL description="Base docker image with R"

# Install procps (so that Nextflow can poll CPU usage)
RUN apt-get update && \
    apt-get install -y procps && \
    apt-get clean -y

# Work in root
WORKDIR /root

# Install the R packages
# Latest version of Bioconductor with DESeq2 is 3.19
RUN Rscript  \
    -e "install.packages('BiocManager',dependencies=TRUE, version='3.19', repos='http://cran.rstudio.com/')"  \
    -e 'BiocManager::install("DESeq2")'
