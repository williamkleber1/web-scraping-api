import pandas as pd
import matplotlib as mpl
#mpl.use('Agg')
import seaborn as sns

class JobAnalysisUseCase:

    def plot_jobs_by_type(self):
        """ Plota a quantidade de vagas por tipo. """
        self.df['type'].value_counts().plot(kind='bar')
        mpl.pyplot.title('Quantidade de Vagas por Tipo')
        mpl.pyplot.xlabel('Tipo de Vaga')
        mpl.pyplot.ylabel('Quantidade')
        mpl.pyplot.savefig('output/jobs_by_type.png')
        #mpl.pyplot.show()

    def plot_jobs_by_title(self):
        """ Plota os 10 títulos de vagas mais comuns. """
        self.df['title'].value_counts().head(10).plot(kind='barh')
        mpl.pyplot.title('Top 10 Títulos de Vagas Mais Comuns')
        mpl.pyplot.xlabel('Quantidade')
        mpl.pyplot.ylabel('Título da Vaga')
        mpl.pyplot.savefig('output/jobs_by_title.png')
        #mpl.pyplot.show()

    def plot_jobs_by_location(self):
        """ Plota a distribuição de vagas por localização. """
        self.df['locale'].value_counts().head(10).plot(kind='pie', autopct='%1.1f%%')
        mpl.pyplot.title('Distribuição de Vagas por Localização')
        mpl.pyplot.ylabel('')
        mpl.pyplot.savefig('output/jobs_by_locale.png')
        #mpl.pyplot.show()

    def plot_jobs_relation(self):
        """ Plota a relação entre tipo de vaga e localização. """
        mpl.pyplot.figure(figsize=(10, 6))
        sns.countplot(y='locale', hue='type', data=self.df, order=self.df['locale'].value_counts().iloc[:10].index)
        mpl.pyplot.title('Relação entre Tipo de Vaga e Localização')
        mpl.pyplot.xlabel('Quantidade')
        mpl.pyplot.ylabel('Localização')
        mpl.pyplot.savefig('output/jobs_relation.png')
        #plt.show() 

    def execute(self, job_list):
        """ Executa os métodos de plotagem. """
        self.df = pd.DataFrame(job_list)

        self.plot_jobs_by_type()
        self.plot_jobs_by_title()
        self.plot_jobs_by_location()
        self.plot_jobs_relation()
        

