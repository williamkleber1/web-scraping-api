import pandas as pd

class ExcelExporter:

    def execute(self, data=None, filename='output/output.xlsx'):
        """
        Salva os dados em um arquivo Excel.
        """
        if not data:
            print("Nenhum dado fornecido para exportar.")
            return

        df = pd.DataFrame(data)
        try:
            df.to_excel(filename, index=False)
            print(f"Dados salvos com sucesso em {filename}")
        except Exception as e:
            print(f"Erro ao salvar os dados em Excel: {e}")

