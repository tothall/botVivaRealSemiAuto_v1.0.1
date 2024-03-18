import random
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait


class Config:

    @staticmethod
    def random_httpheader_useragent():
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/121.0.2277.128",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/121.0.2277.128",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.5",
        ]
        return random.choice(user_agents)

    def __init__(self):
        '''system('ipconfig /release')
        system('ipconfig /renew')'''
        my_user_agent = Config.random_httpheader_useragent()
        self.options = uc.ChromeOptions()
        self.options.add_argument(f"--disable-blink-features=AutomationControlled")
        self.options.add_argument(f"--user-agent={my_user_agent}")
        self.options.add_argument("--disable-gpu")  # Elimina processos residuais do chrome
        self.driver = uc.Chrome(options=self.options, version_main=120)
        self.wait = WebDriverWait(self.driver, 10)
        #self.options.add_argument(f"user-agent={my_user_agent}")
        #Randomization.very_long_wait()
        self.driver.get('https://www.google.com/search?q=im%C3%B3veis+viva+real&sca_esv=1a30264c0409ca1f&source=hp&ei=7b_YZf2zM9TP1sQPvt2FuAY&iflsig=ANes7DEAAAAAZdjN_b9xP76vzb-_Z70fsXngMLQi290S&udm=&ved=0ahUKEwi93uu06cGEAxXUp5UCHb5uAWcQ4dUDCA0&uact=5&oq=im%C3%B3veis+viva+real&gs_lp=Egdnd3Mtd2l6IhJpbcOzdmVpcyB2aXZhIHJlYWwyBRAAGIAEMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeSLYdUNgHWP8bcAF4AJABAJgBnQGgAZUTqgEEMC4xN7gBA8gBAPgBAagCCsICEBAAGAMYjwEY5QIY6gIYjAPCAgsQABiABBixAxiDAcICDhAuGIAEGIoFGLEDGIMBwgIOEAAYgAQYigUYsQMYgwHCAg4QLhiABBjHARivARiOBcICCBAAGIAEGLEDwgIIEAAYgAQYkgPCAggQABiABBjJA8ICCxAuGIAEGMcBGK8BwgIIEAAYFhgeGArCAggQABgWGB4YD8ICChAAGBYYHhgPGArCAg4QLhgWGB4YxwEYrwEYCg&sclient=gws-wiz')
        #self.driver.get('https://httpbin.org/headers')
        #self.driver.get('https://nowsecure.nl')

        #  Inicializando o chrome na metade da resolução da tela
        largura_tela, altura_tela = self.driver.execute_script("return [window.screen.width, window.screen.height];")
        largura_janela = largura_tela // 1.5
        altura_janela = altura_tela
        x = largura_tela // 4  # Centraliza horizontalmente
        y = altura_tela // 4  # Centraliza verticalmente
        self.driver.set_window_position(x, y)
        self.driver.set_window_size(largura_janela, altura_janela)

        # Teste extrator

        '''names = []
                years = []

                #  Localizar todos os imóveis da página
                houses_div = driver.find_element(By.XPATH, "//section[@class='results__main']")
                wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='property-card__content']")))
                houses_data = houses_div.find_elements(By.XPATH, "//div[@class='property-card__content']")

                wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tr[@class='team']")))
                table_rows = driver.find_elements(By.XPATH, "//tr[@class='team']")
                sleep(2)
                for i in range(len(table_rows)):
                    try:
                        table_rows = driver.find_elements(By.XPATH, "//tr[@class='team']")
                        soup = BeautifulSoup(driver.page_source, "lxml")

                        if i >= len(table_rows):
                            break  # Todos os imóveis foram clicados/extraídos
                #try:
                soup = BeautifulSoup(driver.page_source, "lxml")

                team_name_elements = soup.find_all("td", class_="losses")
                for element in team_name_elements:
                    names.append(element.get_text())

                team_year_elements = soup.find_all("td", class_="name")
                for element in team_year_elements:
                    years.append(element.get_text())

                #  Página do anúncio
                #pag = []
                #pagina = []
                #pagina = driver.current_url[-1]
                data = list(zip(names, years))
                lent = len(data)
                for i in range(lent):
                    pag.append(pagina)
                    print(pag)
                dataa = list(zip(data, pag))

                try:
                    wb = load_workbook('Data_Extraction_Temp.xlsx')
                    ws = wb.active
                    for row in data:
                        if row == data:
                            pass
                        else:
                            ws.append(row)
                    wb.save('Data_Extraction_Temp.xlsx')

                except FileNotFoundError:
                    wb = Workbook()
                    ws = wb.active
                    # Cabeçalho atributos dos imóveis
                    ws.append(["Endereço do Imóvel", "Área em m2", "Quantidade de Quartos", "Quantidade de Banheiros",
                               "Quantidade de Vagas", "Descrição do Imóvel", "Preço do Imóvel(R$)", "Link Anúncio", "Página do Anúncio"])
                    for row in data:
                        ws.append(row)
                    wb.save('Data_Extraction_Temp.xlsx')
                    loading.clear()
                #ads_quantity += 1

                except (TimeoutException, StaleElementReferenceException):
                    print("Elemento tornou-se stale ou a espera excedeu o limite. Tentando próximo elemento.")'''

        '''                try:
                    loading.clear()
                    wb = load_workbook('Data_Extraction_Temp.xlsx')
                    ws = wb.active
                    for row in houses_data:
                        ws.append(row)
                    wb.save('Data_Extraction_Temp.xlsx')
                except FileNotFoundError:
                    wb = Workbook()
                    ws = wb.active
                    # Cabeçalho atributos dos imóveis
                    ws.append(["Endereço do Imóvel", "Área em m2", "Quantidade de Quartos", "Quantidade de Banheiros",
                               "Quantidade de Vagas", "Descrição do Imóvel", "Preço do Imóvel(R$)", "Link Anúncio",
                               "Página do Anúncio"])
                    for row in houses_data:
                        ws.append(row)
                    wb.save('Data_Extraction_Temp.xlsx')'''
