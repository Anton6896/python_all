import logging
import pytube
import logging
import pathlib
import os

os.chdir(pathlib.Path(
    __file__).parent.absolute())

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    # will put log ner the executed file
    filename="log_file.txt"
)


# download video
def down_video():
    url_youtube: str = "https://www.youtube.com/watch?v=UM6YDJ2aalU&list=WL&index=1&t=7s&ab_channel=NeuralNine"

    logging.debug("createing connection ...")
    video = pytube.YouTube(url_youtube)

    # for stream in video.streams:
    #     if "video" in str(stream) and "mp4" in str(stream):
    #         print(stream)

    # download stream that you need after see the option above
    stream = video.streams.get_by_itag(22)
    logging.debug("start download ...")

    stream.download(filename="test")

# download play list


def down_play_list_youtube(url):
    play_list = pytube.Playlist(url)

    if not os.path.exists('play_list'):
        os.makedirs('play_list')

    os.chdir(
        str(pathlib.Path(__file__).parent.absolute()) + "/play_list"
    )

    for x, url in enumerate(play_list):
        # pytube.YouTube(url).streams.get_by_itag(22).download()

        video = pytube.YouTube(url)
        stream = video.streams.get_by_itag(22)
        logging.debug(f'start download video : {x}')
        stream.download()


if __name__ == "__main__":
    # down_video()

    corey_pl = "https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p"
    test_pl = "https://www.youtube.com/playlist?list=PL7yh-TELLS1EgOLIPo1sVuf_rDPEp33S8"
    # down_play_list_youtube(test_pl)
