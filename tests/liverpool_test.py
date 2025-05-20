from pages.home_page import HomePage
from pages.Playstation.search_results_page import SearchResultsPage
from pages.Playstation.product_list_page import ProductListPage
from pages.Playstation.product_page import ProductPage
from pages.smart_tv_results_page import SmartTVResultsPage
from pages.perfumes_results_page import PerfumesResultsPage

def test_search_playstation(browser):
    home = HomePage(browser)
    home.search_product("playstation")

    search_results = SearchResultsPage(browser)
    assert search_results.verify_consola_section_present(), "No se encontró sección de consola PlayStation"
    assert search_results.verify_juegos_section_present(), "No se encontró sección de juegos PlayStation"

    search_results.select_consola_ps5()

    product_list = ProductListPage(browser)
    product_list.select_first_product()

    product_page = ProductPage(browser)
    title = product_page.get_product_title()
    price = product_page.get_product_price()

    assert "PS5" in title or "PlayStation 5" in title or "PlayStation" in title, f"Título inesperado: {title}"
    assert price != "", "El precio no debería estar vacío"


def test_smart_tv_filters(browser):
    home = HomePage(browser)
    home.search_product("smart tv")
    smart_tv_results = SmartTVResultsPage(browser)
    assert smart_tv_results.verify_size_filter_present(), "Size filter not found"
    assert smart_tv_results.verify_price_filter_present(), "Price filter not found"
    smart_tv_results.select_price_filter()
    smart_tv_results.expand_brands()
    smart_tv_results.select_brand_sony()
    smart_tv_results.select_size_55_inches()
    count = smart_tv_results.get_results_count()
    assert count > 0, f"Expected at least 1 result, but got {count}"


def test_perfumes_dior_filter(browser):
    home = HomePage(browser)
    home.open_categories_menu()
    home.hover_over_belleza_and_select_perfumes_hombre()
    perfumes_results = PerfumesResultsPage(browser)
    perfumes_results.expand_brands()
    perfumes_results.select_dior_brand()






