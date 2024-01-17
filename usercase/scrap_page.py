import requests
from bs4 import BeautifulSoup
import asyncio

from usercase.export_excel import ExcelExporter
from usercase.export_csv import CSVExporter
from usercase.generate_plots import JobAnalysisUseCase
from usercase.submit_form import JobSubmitter

class JobScraper:
    BASE_URL = 'https://gruposeb.gupy.io'
    JOB_LIST_SELECTOR = 'ul[data-testid="job-list__list"]'
    JOB_ITEM_SELECTOR = 'li[data-testid="job-list__listitem"]'
    NEXT_PAGE_SELECTOR = 'a[aria-label="Next Page"]'

    def scrap_job(self, job):
        """
        Extrai informações de um único anúncio de emprego.
        """
        title = job.find('div', class_='sc-f5007364-4').text.strip()
        locale = job.find('div', class_='sc-f5007364-5').text.strip()
        job_type = job.find('div', class_='sc-f5007364-6').text.strip()

        return {'title': title, 'locale': locale, 'type': job_type}

    def scrap_page(self, page):
        """
        Raspa uma página específica do site de empregos.
        """
        url = f"{self.BASE_URL}?page={page}"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao acessar a página {url}: {e}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def execute(self):
        """
        Itera pelas páginas do site de empregos e extrai informações de cada anúncio.
        """
        page = 1
        jobs_list = []
        while True:
            soup = self.scrap_page(page)
            if not soup:
                break

            job_list = soup.select_one(self.JOB_LIST_SELECTOR)
            if not job_list:
                break

            for job in job_list.select(self.JOB_ITEM_SELECTOR):
                information = self.scrap_job(job)
                print(information)
                jobs_list.append(information)

            if not soup.select_one(self.NEXT_PAGE_SELECTOR):
                break

            page += 1
        
        # Envia os dados para o formulário.
        JobSubmitter().execute(jobs_list)
        # Exporta os dados para um arquivo Excel.
        ExcelExporter().execute(data=jobs_list)
        # Exporta os dados para um arquivo CSV.
        CSVExporter().execute(data=jobs_list)

        # Cria plotagem de dados.
        JobAnalysisUseCase().execute(jobs_list)

