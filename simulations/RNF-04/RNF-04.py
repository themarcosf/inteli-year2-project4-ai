# Descrição do RNF-04:
# A arquitetura deve garantir o armazenamento dos dados de venda/fornecedores de forma 100% seguro (não apresentar nenhuma falha de segurança).

import json
from cryptography.fernet import Fernet

# Gere uma chave de criptografia
key = Fernet.generate_key()
cipher_suite = Fernet(key)

data_to_store = {
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


data_to_store_str = json.dumps(data_to_store).encode()

encrypted_data = cipher_suite.encrypt(data_to_store_str)

with open('dados_protegidos.txt', 'wb') as file:
    file.write(encrypted_data)

with open('dados_protegidos.txt', 'rb') as file:
    encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)

decrypted_data_str = decrypted_data.decode()
decrypted_data_dict = json.loads(decrypted_data_str)

print("Dados descriptografados com segurança:")
print(decrypted_data_dict)