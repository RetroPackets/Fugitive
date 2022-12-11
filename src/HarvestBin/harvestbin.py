


cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'


try:
    from googlesearch import search
    import requests
except ImportError:
    print(red +"[ERR] Modules 'requests' and 'google' aren't installed.")
    if input(cyan +"Do you want to install them? (y/n)") == "y":
        import pip

        pip.main(["install", "google"])
        pip.main(["install", "requests"])
        from googlesearch import search
        import requests
    else:
        print(red +"Exiting...")
        exit()


def search_links():
    site = "pastebin.com"
    query = input(Y +"Enter the search query: ")

    query = query + " site:" + site

    results_max = int(
        input(Y +"Enter the maximum number of search results (default 10): ") or "10"
    )

    results = search(query, stop=results_max, pause=2)

    results = [result for result in results if not "/u/" in result]

    for i in range(len(results)):
        results[i] = results[i].replace(".com/", ".com/raw/")

    output_way = input(cyan +"""Enter the output way (file/console): 
    """)
    if output_way == "file":
        print(red +"Warning! File will be overwritten.")
        output_file = input(Y +"Enter the output file name: ")
        output_file = open(output_file, "w")
        separator = input(Y +"Enter what to separate links by (default newline): ") or "\n"
        output_file.write(separator.join(results))
    elif output_way == "console":
        print("\n".join(results))
    else:
        print(red +"Invalid way!")
        exit()


def scrape_from_links(links: list):
    contents = [requests.get(link).text for link in links]
    output_way = input(Y +"Enter the output way (file/console): ")
    if output_way == "file":
        print(red + "Warning! File will be overwritten.")
        output_file = input(Y +"Enter the output file name: ")
        output_file = open(output_file, "w")
        separator = (
            input(Y +"What to separate links by when writing by (default newline): ")
            or "\n"
        )
        separator = "\n" + separator + "\n"
        try:
            output_file.write(separator.join(contents))
            print(green +"Successfully wrote to file")
        except:
            print(red +"[ERR] Couldn't write to file.")
            exit()
    elif output_way == "console":
        print("\n".join(contents))
    else:
        print(red +"Invalid way!")
        exit()


def main():

    print(cyan +"""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_______▒______▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
______▒___________▒▒▒▒▒▒▒▒
_____▒____________▒▒▒▒▒▒▒▒
____▒_______▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
___▒
__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒
█████████████████████████████████████████████████████████████
█─█─██▀▄─██▄─▄▄▀█▄─█─▄█▄─▄▄─█─▄▄▄▄█─▄─▄─███▄─▄─▀█▄─▄█▄─▀█▄─▄█
█─▄─██─▀─███─▄─▄██▄▀▄███─▄█▀█▄▄▄▄─███─██████─▄─▀██─███─█▄▀─██
▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀""")
    print(red +"Welcome to HarvestBin!")
    print(red + "[INF] We scrape from pastebin.com")
    print(red +
        "We aren't responsible for your actions. Tool made for educational purposes only."
    )
    while True:
        print(cyan +"\nMenu:\n\n1 -> Scrape links\n2 -> Scrape links contents")
        choice = input(Y +"Enter your choice: ")
        if choice == "1":
            search_links()
        elif choice == "2":
            links_file = input(Y +"File to import links from: ")
            sep = (
                input(Y +"What to separate links by when reading (default newline): ")
                or "\n"
            )
            with open(links_file, "r") as f:
                links = f.read().split(sep)
                scrape_from_links(links)
        else:
            print(red +"Invalid choice!")


if __name__ == "__main__":
    main()