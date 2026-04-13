file = input("File Name:")

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg"):
    print("image/jpg")
elif file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("file/pdf")
elif file.endswith(".zip"):
    print("file/zip")
else:
    print("application/octet-stream")
