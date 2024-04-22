import scrapy

class ButtonURLSpider(scrapy.Spider):
    name = 'button_url_spider'
    start_urls = ['https://www.mercadolibre.com.co/audifonos-jbl-tune-720-bt-headphone-bluetooth-over-ear-color-negro/p/MCO29148660#reviews']  # Reemplaza 'http://www.ejemplo.com' con la URL de tu página web

    def parse(self, response):
        # Definir los XPath
        xpaths = [
            '//section/div/div/div',
    '//div/section/div/div/div',
    '//div/div/section/div/div/div',
    '//div/div/div/section/div/div/div',
    '//div/div/div/div/section/div/div/div',
    '//div/div/div/div/div/section/div/div/div',
    '//div/div/div/div/div/div/section/div/div/div',
    '//div/div/div/div/div/div/div/section/div/div/div',
    '//div/div/div/div/div/div/div/div/section/div/div/div',
    '//main/div/div/div/div/div/div/div/div/div/section/div/div/div',
    '//body/main/div/div/div/div/div/div/div/div/div/div/section/div/div/div',
    '//div[contains(@class, "ui-review-capability-filter")]',
    '//*[contains(@data-testid, "filter-component")]',
    '//div[contains(@data-testid, "filter-component")]',
    '//*[@data-testid="filter-component"]',
    '//div[@data-testid="filter-component"]',
    '//*[@id="reviews_capability_v3"]/div/section/div/div/div',
    '//*[@id="reviews_capability_v3"]/div/section/div/div/div'
        ]

        for xpath in xpaths:
            buttons = response.xpath(xpath)
            for button in buttons:
                # Obtener la URL a la que apunta el botón
                url = button.xpath('@href').extract_first()  # Cambia '@href' al atributo que contenga la URL en tu HTML
                if url:
                    yield {
                        'url': url
                    }