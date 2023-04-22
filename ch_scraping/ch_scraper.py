import requests
import urllib.parse
from bs4 import BeautifulSoup
import re

class ChScraper():
    def __init__(self):
        self.base_url = "https://find-and-update.company-information.service.gov.uk"
        self.search_url = "https://find-and-update.company-information.service.gov.uk/search?"
    
    def search_for_company(self, company: str) -> requests.Response:
        query = {"q": company}
        request_url = self.search_url + urllib.parse.urlencode(query)
        search_response = requests.get(request_url)
        return search_response
    
    def _search_results_to_soup(self, search_response: requests.Response) -> BeautifulSoup:
        search_soup = BeautifulSoup(search_response.text, features="lxml")
        return search_soup
    
    def _clean_result_text(self, result_text: str) -> str:
        return re.sub("  ", "", re.sub("\n", "", result_text))
    
    def _get_company_number(self, href: str) -> str:
        if "/company/" in href:
            company_number = re.sub("/company/", "", href)
        else:
            company_number = "N/A"
        return company_number
    
    def get_first_result_data(self, search_soup: BeautifulSoup) -> dict:
        first_result = search_soup.select("li.type-company")[0]
        first_result_header = first_result.select("a.govuk-link")[0]
        href = first_result_header.get("href")
        return {
            "name": self._clean_result_text(first_result_header.text),
            "relative_url": href,
            "company_number": self._get_company_number(href),
            "address": first_result.select("p")[-1].text
        }
    
    def get_company_data(self, company: str) -> dict:
        search_response = self.search_for_company(company)
        search_soup = self._search_results_to_soup(search_response)
        search_data = self.get_first_result_data(search_soup)
        return search_data



if __name__ == "__main__":
    scraper = ChScraper()
    print(scraper.get_company_data("bp plc"))
    
