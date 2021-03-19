//Programa para duplicar um arquivo
#include<stdio.h>
#include<stdlib.h>

int main(int argc, char ** args){
	//tamanho maximo do arquivo de 5Mb
  	size_t size_buff =1024*5000;
  	size_t bytes_lido;
  	char *buff;
  	FILE *file_in,*file_out;

	file_in = fopen(args[1],"rb");
	file_out = fopen(args[2],"wb");
  	
 	buff =(char*) malloc(size_buff);
  	if(!buff){
     	fprintf(stderr,"Erro ao alocar memoria\n");
     	goto final;
  	}

  	while(!feof(file_in)){
    	bytes_lido = fread(buff,1,size_buff,file_in);
    	if(bytes_lido <=0)
			break;
    	fwrite(buff,bytes_lido,1,file_out);
  	}
  	free(buff);
  	final:
  	fclose(file_in);
  	fclose(file_out);
  	return 0;
}
