import csv

class CSVExporter:
    def execute(self, data, filename='output/output.csv'):
        """
        Salva os dados em um arquivo CSV.
        """
        if not data:
            print("Nenhum dado fornecido para exportar.")
            return

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

            print(f"Dados salvos com sucesso em {filename}")
        except Exception as e:
            print(f"Erro ao salvar os dados em CSV: {e}")
