def main():
    file = input("File name: ").lower()
    if(file.find("gif") != -1):
        print("image/gif")
    elif(file.find("jpg") != -1):
        print("image/jpeg")
    elif(file.find("jpeg") != -1):
        print("image/jpeg")
    elif(file.find("png") != -1):
        print("image/png")
    elif(file.find("pdf") != -1):
        print("application/pdf")
    elif(file.find("txt") != -1):
        print("text/plain")
    elif(file.find("zip") != -1):
        print("application/zip")
    else:
        print("application/octet-stream")

main()