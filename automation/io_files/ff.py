import pathlib
import os
import shutil

f_path = pathlib.Path(__file__).parent.absolute()


def os_module_look():
    
    print(f_path)
    print(f"the getcwd : {os.getcwd()}")
    pa = os.path.abspath("check")
    print(f"abcpath : {str(pa)}")
    t = os.path.exists("test")
    print(f"exist : {t}")

    # if not os.path.exists("test"):
    #     os.mkdir("test")
    # os.makedirs("/folde1/folde2/") -> create the full path of folders

    p = os.listdir(os.path.abspath("."))
    print(f"directories on this path {p}")
    size = 0
    # get size of all files in this folder
    for filename in p:
        if not os.path.isfile(os.path.join(os.path.abspath("."), filename)):
            continue
        else:
            size += os.path.getsize(filename)
    print("size is", size)


def working_with_files():
    try:
        # read
        with open(os.path.join(f_path, "test/text.txt")) as f:
            data = f.read()
            print(data)

        # if not os.path.exists("test"):
        #     os.mkdir("test")
        # wright
        with open(os.path.join(f_path, "test/text_3.txt"), "a+") as f:
            f.write("\nnew line =================")
            print(f)

    except FileNotFoundError as e:
        print(e)


def move_file_of_folder():
    mfile = os.path.join(f_path, "test/")
    # file copy
    # shutil.copy(mfile + "text.txt", mfile + "other.txt")

    # folder copy
    # shutil.copytree(mfile, os.path.join(f_path, "test_2"))

    # move file
    # shutil.move(mfile + "/other.txt", mfile+"/jj/")

    # for rename the file just move it with different name !

    # delete or unlink the file
    # os.rmdir for folder (no files in )
    # shutil.rmtree for rm folder not empty
    # if os.path.exists(mfile+"text_2.txt"):
    #     os.unlink(mfile+"text_2.txt")
    # else:
    #     print("file already unlinked")

    if os.path.exists(mfile):
        for folder, sub_folder, file_ in os.walk(mfile):
            print(f"folder : {folder}")
            print(f"sub_folder : {sub_folder}")
            print(f"file : {file_}")
            print("-------------")

            # for f in file_:
            #     # move to root folder 
            #     if f == "text.txt":
            #         shutil.move(folder+"/"+f, mfile)


if __name__ == "__main__":
    pass
