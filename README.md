# DriverMP
DriverMP is a cancer driver gene classifier based on a deep neural network using a wealth of prior signaling pathways information.
## Dependencies
### R packages
R 4.0.3  
fgsea 1.16.0  
org.Hs.eg.db 3.12.0  
ensembldb 2.14.1  
tidyverse 1.3.1  
rlist 0.4.6.1  
data.table 1.14.0  
  
### python 3.8.5
datatable 0.11.1  
keras 2.4.3  
tensorflow 2.4.1  

### model and curated pathways

It is recommended to build the environment with conda.
```
conda env create -f environment_python.yml ###install dependencies for python
source activate DriverMPr-data.table
conda install r bioconductor-fgsea bioconductor-org.hs.eg.db bioconductor-ensembldb r-tidyverse r-rlist r-data.table
```

## usage
Download the latest release and unzip it. You will get the trained model and all scripts for prediction.
The input file is the somatic mutation annotation format file (MAF). Once you have all the essential packages installed, you just need to run DriverMP.sh file like this:
```
DriverMP.sh $MAF_file
```
Note: If you have a very large MAF file, e.g. > 100k somatic mutations, to reduce the memory usage, it is recommended to split your MAF file into few small file with header first. Feed the splitted file to the DriverMP.sh and then concatenate the outputs.

## Outputs
A list of predicted driver genes.
