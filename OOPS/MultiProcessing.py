import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started downloading {name}!!!")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}.")

if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(50):
        #downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

