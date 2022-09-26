import requests
from bs4 import BeautifulSoup as bs


def collect_kqsx():
    # Lay ket qua so xo tu ketqua1.net
    r = requests.get("https://ketqua2.net/")
    soup = bs(r.content, "html.parser")
    info = soup.find("tbody")
    ketqua = info.find_all("tr")
    kqxs = {}
    for index, row in enumerate(ketqua):
        if index == 0 or index == 9:
            pass
        else:
            prize_name = row.find(
                "div", {"class": "row-no-gutters text-center"}
            ).find_all("div")
            if len(prize_name) == 1:
                key = row.find("td", {"class": "hover"}).text
                value = prize_name[0].text
                kqxs[key] = value
            else:
                value = []
                key = row.find("td", {"class": "hover"}).text
                for i in prize_name:
                    value.append(i.text)
                kqxs[key] = value

    return kqxs


def kqxs_lo():
    loto = []
    kqxs = collect_kqsx().values()
    for kq in kqxs:
        if type(kq) == str:
            loto.append(kq[-2:])
        elif type(kq) == list:
            for i in kq:
                loto.append(i[-2:])
    return loto


def main(*args):
    args = input(
        "Nhập số lô cần kiểm tra, Nếu nhập nhiều số thì phải cách ' ', bỏ qua để lấy KQXS:"
    )
    ketqua_2so = kqxs_lo()
    if args == "":
        print(collect_kqsx())
    else:
        trung_lo = {}
        for i in args.split(" "):
            i = i.zfill(2)
            if i in ketqua_2so:
                trung_lo[i] = ketqua_2so.count(i)
        if len(trung_lo) == 0:
            print("Tạch lô rồi!!!")
        else:
            for k, v in trung_lo.items():
                print(f"Lô {k}: Nổ {v} nháy ")


if __name__ == "__main__":
    main()