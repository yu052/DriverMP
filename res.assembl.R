

inputMAF = commandArgs(trailingOnly=TRUE)
#inputMAF<-"dw108.final.maf"
pred_res<-paste0(inputMAF,".feature.matrix.csv.pred")
gene_file<-paste0(inputMAF,".mutations.csv")

gene<-read.csv(gene_file,row.names = 1)
pred<-read.csv(pred_res,row.names = 1)

gene<-gene[rownames(pred),]
gene_pred<-merge(gene,pred,by=0,all = T)

driver_gene<-gene_pred[gene_pred$pred=='D',]
