# Descrição do RNF-02:
# Todas as etapas da cadeia de suprimentos deve ter monitoramento com logs e respostas do sistema.

import logging

logging.basicConfig(filename='supply_chain.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class CadeiaDeSuprimentos:
    def __init__(self):
        self.logger = logging.getLogger('CadeiaDeSuprimentos')

    def recebimento_de_pedido(self, pedido):
        self.logger.info(f"Pedido recebido: {pedido}")

    def processamento_de_pedido(self, pedido):
        self.logger.info(f"Processando pedido: {pedido}")

    def envio_de_pedido(self, pedido):
        self.logger.info(f"Pedido enviado: {pedido}")


if __name__ == '__main__':
    supply_chain = CadeiaDeSuprimentos()

    pedido_1 = {
        "Empresa": "Meta Inc.",
        "Cliente": "Company Z",
        "Número da Fatura": "INV003",
        "Data de Emissão": "2023-10-03",
        "Data de Vencimento": "2023-11-03",
        "Moeda": "USD",
        "Descrição do Produto/Serviço": "2x Event Sponsorships",
        "Quantidade": 2,
        "Preço Unitário": "$5000",
        "Total": "$10000",
        "Categoria Macro": "Sales, Marketing & Events",
        "Subcategoria": "Events",
        "Categoria de Item": "Program Sponsorships",
    }

    pedido_2 = {
        "Empresa": "Meta Inc.",
        "Cliente": "Company B",
        "Número da Fatura": "INV007",
        "Data de Emissão": "2023-10-07",
        "Data de Vencimento": "2023-11-07",
        "Moeda": "EUR",
        "Descrição do Produto/Serviço": "1x Facility Security System",
        "Quantidade": 1,
        "Preço Unitário": "€5000",
        "Total": "€5000",
        "Categoria Macro": "Real Estate & Facilities",
        "Subcategoria": "Security",
        "Categoria de Item": "Physical Security Services & Reception",
    }

    supply_chain.recebimento_de_pedido(pedido_1)

    supply_chain.processamento_de_pedido(pedido_1)

    supply_chain.envio_de_pedido(pedido_1)

    supply_chain.recebimento_de_pedido(pedido_2)

    supply_chain.processamento_de_pedido(pedido_2)

    supply_chain.envio_de_pedido(pedido_2)
