import requests
import matplotlib.pyplot as plt

plt.ion()


def get_latest_log():
    res = requests.get(
        f"https://epics-services-tst:33181/Olog/resources/logs?limit=1",
        verify=False,
    )
    data = res.json()
    return data


def plot_sizes():
    data = get_latest_log()
    data = data[0]["attachments"]
    sizes = [d["fileSize"] for d in data]
    print(f"Number of sizes: {len(sizes)}")

    plt.plot(sizes)
    plt.xlabel(f"File counter (0-{len(data)-1})")
    plt.ylabel("File size [bytes]")
    plt.grid(visible=True)
