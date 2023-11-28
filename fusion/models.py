# models.py
from django.db import models
import pandas as pd

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")

    def save_data_from_excel(self):
        try:
            path = str(self.file.path)
            df = pd.read_excel(path)

            # Adicione aqui a lógica para processar os dados do arquivo Excel
            # Exemplo: Salvando os dados processados em um atributo do modelo
            self.processed_data = df.to_dict(orient='records')

        except Exception as e:
            print(f"Erro ao processar dados do Excel: {str(e)}")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.save_data_from_excel()