import scrapy


class CommentSpider(scrapy.Spider):
    name = 'comment_spider'
    start_urls = ['https://www.mercadolibre.com.co/audifonos-jbl-tune-720-bt-headphone-bluetooth-over-ear-color-negro/p/MCO29148660#reviews']  # Reemplaza 'http://www.ejemplo.com' con la URL de tu página web

    def parse(self, response):
        # XPaths para los comentarios
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

        # Extraer comentarios utilizando los XPaths
        for xpath in xpaths:
            comments = response.xpath(xpath).extract()
            for comment in comments:
                yield {
                    'comment': comment
                }