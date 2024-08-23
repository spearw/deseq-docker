[![Build a Docker image](https://github.com/spearw/deseq-docker/actions/workflows/docker-image.yml/badge.svg)](https://github.com/spearw/deseq-docker/actions/workflows/docker-image.yml)[![Build and push a Docker image](https://github.com/spearw/deseq-docker/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/spearw/deseq-docker/actions/workflows/docker-publish.yml)

# deseq-docker

[DEseq](https://github.com/spearw/deseq.git) estimates variance-mean dependence in count data from high-throughput sequencing assays and test for differential expression based on a model using the negative binomial distribution. deseq-docker provides Docker files and GitHub Action workflows for building and publishing a Docker image so that deseq can be used in Nextflow workflows.

For additional information about the package, see [analyzing RNA-seq data with DESeq2](https://bioconductor.org/packages/3.18/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)

### Build

To build your image from the command line:
* You can do this on [Google shell](https://shell.cloud.google.com) since docker is installed and available.

```bash
docker build --platform linux/amd64 -t deseq:latest .
```

### Test

To test this tool from the command line:

```bash
docker run -it deseq:latest snakemake -h
```

Disclaimer
THIS WEBSITE AND CONTENT AND ALL SITE-RELATED SERVICES, INCLUDING ANY DATA, ARE PROVIDED "AS IS," WITH ALL FAULTS, WITH NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTIES OF MERCHANTABILITY, SATISFACTORY QUALITY, NON-INFRINGEMENT OR FITNESS FOR A PARTICULAR PURPOSE. YOU ASSUME TOTAL RESPONSIBILITY AND RISK FOR YOUR USE OF THIS SITE, ALL SITE-RELATED SERVICES, AND ANY THIRD PARTY WEBSITES OR APPLICATIONS. NO ORAL OR WRITTEN INFORMATION OR ADVICE SHALL CREATE A WARRANTY OF ANY KIND. ANY REFERENCES TO SPECIFIC PRODUCTS OR SERVICES ON THE WEBSITES DO NOT CONSTITUTE OR IMPLY A RECOMMENDATION OR ENDORSEMENT BY SCIENCE and TECHNOLOGY CONSULTING LLC.
