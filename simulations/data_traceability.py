# Possivel erro na reastreabilidade dos dados dentro da IA de classificação
# A necessidade de analisar vários dados de uma unica Invoice pode levar a perda de alguma informação importante para a classificação.

import random

data_current = {
    "Invoice 1": {
        "Empresa": "Meta Inc.",
        "Cliente": "Company H",
        "Número da Fatura": "INV014",
        "Data de Emissão": "2023-10-14",
        "Data de Vencimento": "2023-11-14",
        "Moeda": "EUR",
        "Descrição do Produto/Serviço": "1x Health Insurance Premiums",
        "Quantidade": 1,
        "Preço Unitário": "€10000",
        "Total": "€10000",
        "Categoria Macro": "Human Resources",
        "Subcategoria": "Benefits",
        "Categoria de Item": "Health Insurance & Health Care Spending Accounts",
        "Target nivel 1":"Human Resources",
        "Target nivel 2":"Benefits",
        "Target nivel 3":"Health Insurance & Health Care Spending Accounts",
    },
    "Invoice 2": {
        "Empresa": "Meta Inc.",
        "Cliente": "XYZ Corp.",
        "Número da Fatura": "INV002",
        "Data de Emissão": "2023-10-02",
        "Data de Vencimento": "2023-11-02",
        "Moeda": "EUR",
        "Descrição do Produto/Serviço": "5x Software Licenses",
        "Quantidade": 5,
        "Preço Unitário": "€200",
        "Total": "€1000",
        "Categoria Macro": "Technology/Telecom",
        "Subcategoria": "Software & Support",
        "Categoria de Item": "IT Software Applications - Perpetual",
        "Target nivel 1":"Technology/Telecom",
        "Target nivel 2":"Software & Support",
        "Target nivel 3":"IT Software Applications - Perpetual",
    },
    "Invoice 3": {
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
        "Target nivel 1":"Sales, Marketing & Events",
        "Target nivel 2":"Events",
        "Target nivel 3":"Program Sponsorships",
    },
    "Invoice 4": {
        "Empresa": "Meta Inc.",
        "Cliente": "Company Y",
        "Número da Fatura": "INV004",
        "Data de Emissão": "2023-10-04",
        "Data de Vencimento": "2023-11-04",
        "Moeda": "EUR",
        "Descrição do Produto/Serviço": "1x Real Estate Leased",
        "Quantidade": 1,
        "Preço Unitário": "€20000",
        "Total": "€20000",
        "Categoria Macro": "Real Estate & Facilities",
        "Subcategoria": "Facilities Services",
        "Categoria de Item": "Real Estate Leased",
        "Target nivel 1":"Real Estate & Facilities",
        "Target nivel 2":"Facilities Services",
        "Target nivel 3":"Real Estate Leased",
    },
    "Invoice 5": {
        "Empresa": "Meta Inc.",
        "Cliente": "Company X",
        "Número da Fatura": "INV005",
        "Data de Emissão": "2023-10-05",
        "Data de Vencimento": "2023-11-05",
        "Moeda": "USD",
        "Descrição do Produto/Serviço": "100x Office Chairs",
        "Quantidade": 100,
        "Preço Unitário": "$200",
        "Total": "$20000",
        "Categoria Macro": "Real Estate & Facilities",
        "Subcategoria": "Facilities Supplies",
        "Categoria de Item": "Furniture & Fixtures",
        "Target nivel 1":"Real Estate & Facilities",
        "Target nivel 2":"Facilities Supplies",
        "Target nivel 3":"Furniture & Fixtures",
    },
}

data_new = {
    "Invoice 6": {
        "Empresa": "Meta Inc.",
        "Cliente": "Company A",
        "Número da Fatura": "INV006",
        "Data de Emissão": "2023-10-06",
        "Data de Vencimento": "2023-11-06",
        "Moeda": "USD",
        "Descrição do Produto/Serviço": "5x Accounting Services",
        "Quantidade": 5,
        "Preço Unitário": "$1000",
        "Total": "$5000",
        "Categoria Macro": "Professional Services",
        "Subcategoria": "Accounting and Tax Services",
        "Categoria de Item": "Audit & Assurance",
        "Target nivel 1":"Professional Services",
        "Target nivel 2":"Accounting and Tax Services",
        "Target nivel 3":"Audit & Assurance",
    },
    "Invoice 7": {
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
        "Target nivel 1":"Energy & Utilities",
        "Target nivel 2":"Energy Production Fuel",
        "Target nivel 3":"Generators - all",
    },
    "Invoice 8": {
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
        "Target nivel 1":"Energy & Utilities",
        "Target nivel 2":"Energy Production Fuel",
        "Target nivel 3":"Generators - all",
    },
    "Invoice 9": {
        "Empresa": "Meta Inc.",
        "Cliente": "Company D",
        "Número da Fatura": "INV009",
        "Data de Emissão": "2023-10-09",
        "Data de Vencimento": "2023-11-09",
        "Moeda": "EUR",
        "Descrição do Produto/Serviço": "1x Datacenter Cabling",
        "Quantidade": 1,
        "Preço Unitário": "€8000",
        "Total": "€8000",
        "Categoria Macro": "Technology/Telecom",
        "Subcategoria": "Network Hardware",
        "Categoria de Item": "Datacenter Cabling",
        "Target nivel 1":"Technology/Telecom",
        "Target nivel 2":"Network Hardware",
        "Target nivel 3":"Datacenter Cabling",
    },
    "Invoice 10": {
        "Informações da Empresa": "Meta Inc., 123 Street, Global City",
        "Informações do Cliente": "ABC Corporation, 456 Avenue, Local City",
        "Número da Fatura": "INV001",
        "Data de Emissão": "2023-10-25",
        "Data de Vencimento": "2023-11-25",
        "Moeda": "USD",
        "Descrição do Produto/Serviço": "10x Transistor",
        "Quantidade": 10,
        "Preço Unitário": "$5",
        "Total": "$50",
        "Categoria Macro": "Technology/Telecom",
        "Subcategoria": "Network Hardware",
        "Categoria de Item": "Switches",
        "Target nivel 1":"Sales, Marketing & Events",
        "Target nivel 2":"Software & Support",
        "Target nivel 3":"Desktop Computers",
    },
}

def simulate_markov_chain(invoice_data, loss_prob):
    for key, value in invoice_data.items():
        if random.random() < loss_prob:
            invoice_data[key] = None
    return invoice_data

loss_probability_atual = 0.6

# Simulação sistema atual:
print('Iniciando simulação do sistema atual - Com perda de dados')

for invoice_key, invoice_data in data_current.items():
    print(f"Dados originais da {invoice_key}:")
    print(invoice_data)
    print(f"\nDados da {invoice_key} após simulação de perda de dados:")
    simulated_data = simulate_markov_chain(invoice_data, loss_probability_atual)
    print(simulated_data)
    print("\n------------------------------------\n")


# Simulação sistema novo:
print('Iniciando simulação do sistema novo - Sem perda de dados')

for invoice_key, invoice_data in data_new.items():
    print(f"Dados originais da {invoice_key}:")
    print(invoice_data)
    print(f"\nDados da {invoice_key} após simulação de sistema novo:")
    simulated_data = simulate_markov_chain(invoice_data, 0)
    print(simulated_data)
    print("\n------------------------------------\n")
