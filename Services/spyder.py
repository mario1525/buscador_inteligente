import subprocess

def ejecutar_spider_scrapy(urls):
    # Forma la cadena de comandos con las URLS de los productos
    comando = ['scrapy', 'crawl', 'comentarios_spider', '-a', f'start_urls={",".join(urls)}']
    
    # Llama al proceso Scrapy
    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Captura la salida y el error (si los hay)
    salida, error = proceso.communicate()
    
    # Maneja el resultado del proceso
    if proceso.returncode != 0:
        print(f'Ocurrió un error: {error.decode("utf-8")}')
    else:
        print("Scrapy se ejecutó correctamente.")