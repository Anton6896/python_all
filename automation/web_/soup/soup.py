

from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
# uncomment for disable
logging.disable(logging.CRITICAL)


def bs():
    # Web scrapping
    msn_url = "https://www.msn.com/en-xl"
    # for using amazon need to add headers
    amazon_url = "https://www.amazon.com/Merrell-Mens-Moab-Hiking-Walnut/dp/B01HFPP4KI/ref=sr_1_1?dchild=1&keywords=Merrell&qid=1606451904&sr=8-1"
    amazon_url_2 = "https://www.amazon.com/Merrell-Jungle-Slip-Dusty-Olive/dp/B00YBBIO0C/ref=sxin_9_ac_d_rm?ac_md=0-0-bWVycmVsbA%3D%3D-ac_d_rm&cv_ct_cx=Merrell&dchild=1&keywords=Merrell&pd_rd_i=B00YBBIO0C&pd_rd_r=5670c77b-1a94-4956-b564-51b8a98212d2&pd_rd_w=5uMm1&pd_rd_wg=UX5lS&pf_rd_p=b6dc128d-7461-4205-b97b-a956bf7315b7&pf_rd_r=PP42GSY7D083DHA1DQFK&psc=1&qid=1606452636&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081"
    ebay_url = "https://www.ebay.com/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    for _ in range(10):
        page = requests.get(amazon_url, headers=headers)
        page2 = requests.get(amazon_url_2, headers=headers)

        if page.status_code != 200 or page2.status_code != 200:
            # its not allways working ( depends for AI on server and his responce for the price ! )
            logging.debug(
                f" page status: {page.status_code}, trying again ...")
            logging.debug(
                f" page2 status: {page2.status_code}, trying again ...")
            continue

        soup = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(page2.content, "html.parser")

        logging.debug("getting price:")
        # not allways working !! must try couple times in amazon
        price = soup.find(id="priceblock_ourprice",
                          class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text()

        price_2 = soup2.find(id="priceblock_ourprice",
                             class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text()

        print(f"price : {price}")
        print(f"price 2: {price_2}")
        break  # if price break


def get_price():
    # het price from ebay
    ebay_page = "https://www.ebay.com/itm/Tactical-Water-Bottle-Pouch-Bottle-Holder-1L-Camping-Hiking-Climbing-Bag-Molle/223650863828?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3Dcab4065274e0469d93b7c1696de264ba%26pid%3D100675%26rk%3D1%26rkt%3D12%26mehot%3Dnone%26sd%3D383130054461%26itm%3D223650863828%26pmt%3D1%26noa%3D1%26pg%3D2380057%26brand%3DUnbranded%2FGeneric&_trksid=p2380057.c100675.m4236&_trkparms=pageci%3A368b53e4-3066-11eb-ba6d-beb8a831f22a%7Cparentrq%3A07e367b81760a4d3619ba490ffe3d68c%7Ciid%3A1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    page = requests.get(ebay_page, headers=headers)

    # get price
    logging.debug("data price from ebay ")
    price = BeautifulSoup(page.content, "html.parser").find(
        id="prcIsum", itemprop="price").get_text()
    print(price)

    # get img source
    print("get img : src ")
    ul_img = BeautifulSoup(page.content, "html.parser").find(
        id="vi_main_img_fs_slider")
    imgs = ul_img.find_all('img')
    for i in imgs:
        print(i['src'])

    # get image ( download )
    logging.debug("getting image of product ")
    image = requests.get(
        "https://i.ebayimg.com/images/g/MHIAAOSwX7BdcAG-/s-l1600.jpg")
    with open("img.jpg", "wb") as pic:
        pic.write(image.content)


if __name__ == "__main__":
    logging.debug("start soup")
    # bs()
    get_price()
