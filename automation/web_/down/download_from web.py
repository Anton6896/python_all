import re
import requests


def ts():

    res = requests.get(
        "https://filesamples.com/samples/document/txt/sample1.txt")
    print(f"download file : {res.status_code} status")
    print(f"file length : {len(res.text)}")
    print(f"text from mess :\n{res.text[:100]}\n")

    # get the bad request exception
    # res = requests.get("https://filesamples.com/samples/document/txt/sample526.txt")
    # print(f"here will throw exception : \n {res.raise_for_status()}")

    # wight to file binary data (python will download the binary from source)
    with open("down_text.txt", "wb") as f:
        # read chunk from file in server and
        # write to the text file by bytes (1000 bite per read)
        for chunk in res.iter_content(1000):
            f.write(chunk)


if __name__ == "__main__":
    ts()
