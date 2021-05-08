# DriverMP
OncoDMP is a cancer driver gene classifier based on a deep neural network using a wealth of prior signaling pathways information.
## Dependencies
### R

### python

### model and curated pathways

## usage
The input file is the somatic mutation annotation format file (MAF). Once you have all the packages installed, you just need to run DriverMP.sh file like this:
'''DriverMP.sh $MAF_file'''
Note: If you have a very large MAF file, e.g. > 100k somatic mutations, to reduce the memory usage, it is recommended to split your MAF file into few small file with header first. Feed the splitted file to the DriverMP.sh and then concatenate the outputs.
