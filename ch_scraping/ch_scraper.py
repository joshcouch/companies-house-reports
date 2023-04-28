import requests
import urllib.parse
from bs4 import BeautifulSoup
import re

class ChScraper():
    def __init__(self):
        self.base_url = "https://find-and-update.company-information.service.gov.uk"
        self.search_url = "https://find-and-update.company-information.service.gov.uk/search?"
    
    def search_for_search_term(self, search_term: str) -> requests.Response:
        query = {"q": search_term}
        request_url = self.search_url + urllib.parse.urlencode(query)
        search_response = requests.get(request_url)
        return search_response
    
    def _response_to_soup(self, response: requests.Response) -> BeautifulSoup:
        search_soup = BeautifulSoup(response.text, features="lxml")
        return search_soup
    
    def _clean_result_text(self, result_text: str) -> str:
        return re.sub("  ", "", re.sub("\n", "", result_text))
    
    def _get_company_number(self, href: str) -> str:
        if "/company/" in href:
            company_number = re.sub("/company/", "", href)
        else:
            company_number = "N/A"
        return company_number
    
    def scrape_first_search_result(self) -> dict:
        if len(self.search_soup.select("li.type-company")):
            first_result = self.search_soup.select("li.type-company")[0]
            first_result_header = first_result.select("a.govuk-link")[0]
            href = first_result_header.get("href")
            return {
                "name": self._clean_result_text(first_result_header.text),
                "relative_url": href,
                "company_number": self._get_company_number(href),
                "address": first_result.select("p")[-1].text
            }
        else: raise Exception("No search result found. Please try another search term")
    
    def scrape_search_soup(self, search_term: str):
        search_response = self.search_for_search_term(search_term)
        search_soup = self._response_to_soup(search_response)
        return search_soup
    
    def scrape_overview(self):
        pass
    
    def scrape_filing_history(self):
        pass
    
    def scrape_officers(self):
        officers_url = self.company_page_url + "/officers"
        officers_response = requests.get(officers_url)
        officers_soup = self._response_to_soup(officers_response)
        if officers_soup.select("h2#company-appointments"):
            officers_h2 = officers_soup.select("h2#company-appointments")[0].text
            n_officers = int(re.search("(\d+)(?= officers)", officers_h2).group(0))
            n_resignations = int(re.search("(\d+)(?= resignations)", officers_h2).group(0))
            return {
                "n_officers": n_officers,
                "n_resignations": n_resignations
            }
        else: return {"no officers data"}
        
    def scrape_persons_significant_control(self):
        return {}
    
    def scrape_people(self):
        officers_data = self.scrape_officers()
        person_siginificant_control_data = self.scrape_persons_significant_control()
        return {**officers_data, **person_siginificant_control_data}

    def get_company_data(self, search_term: str) -> dict:
        self.search_soup = self.scrape_search_soup(search_term)
        self.search_result_data = self.scrape_first_search_result()
        self.company_page_url = self.base_url + self.search_result_data["relative_url"]
        self.people_data = self.scrape_people()
        return self.people_data



if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        search_term = sys.argv[1]
    elif len(sys.argv) == 1:
        search_term = "bp plc"
    else:
        raise Exception("""Error: Invalid arguments passed
              
              Usage: `python ch_scraper SEARCH_TERM`
              """)
    
    scraper = ChScraper()
    print(scraper.get_company_data(search_term))
    
