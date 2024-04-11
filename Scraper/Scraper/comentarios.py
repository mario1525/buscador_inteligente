import scrapy

class ComentariosSpider(scrapy.Spider):
    name = 'comentarios_spider'

    def __init__(self, *args, **kwargs):
        super(ComentariosSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_urls').split(',')  # Lista de URLs de productos

    def parse(self, response):
        # Aquí se realiza la extracción de los comentarios
        comentarios = response.xpath('XPATH_DE_LA_ETIQUETA_QUE_CONTIENE_LOS_COMENTARIOS')

        for comentario in comentarios:
            # Extraer el texto del comentario
            texto = comentario.xpath('XPATH_DEL_TEXTO_DEL_COMENTARIO').get()

            # Aquí puedes hacer cualquier otra manipulación de los comentarios, como limpiarlos o procesarlos de alguna manera

            # Enviar los comentarios extraídos
            yield {
                'comentario': texto,
            }

        # Si hay más páginas de comentarios, se puede seguir a la página siguiente
        # Implementa lógica para seguir a la página siguiente si es necesario
