import requests
import matplotlib.pyplot as plt

plt.ion()


def get_latest_log(bl="tst", port="33181"):
    res = requests.get(
        f"https://epics-services-{bl}:{port}/Olog/resources/logs?limit=1",
        verify=False,
    )
    data = res.json()
    return (data, res.url)


def plot_sizes(*args, **kwargs):
    (data_raw, url) = get_latest_log(*args, **kwargs)
    data = data_raw[0]["attachments"]
    sizes = [d["fileSize"] for d in data]
    print(f"Number of sizes: {len(sizes)}")

    plt.plot(sizes)
    plt.title(f"URL: {url}\nOlog ID: {data_raw[0]['id']}")
    plt.xlabel(f"File counter (0-{len(data)-1})")
    plt.ylabel("File size [bytes]")
    plt.grid(visible=True)
