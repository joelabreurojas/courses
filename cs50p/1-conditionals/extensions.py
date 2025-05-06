# File Extensions


def main():
    """
    Prompts the user for the name of a file and then outputs that file’s media
    type if the file’s name ends, case-insensitively, in any of these suffixes:
    .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
    """
    file_name = input("File name: ").lower().strip()

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.replace("jpeg", "jpg").endswith(".jpg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
