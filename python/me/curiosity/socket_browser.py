import socket


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as endpoint:
        endpoint.connect(("data.pr4e.org", 80))

        command: str = "GET http://data.pr4e.org/page1.html HTTP/1.0\r\n\r\n"

        endpoint.send(command.encode())

        while True:
            data: bytes = endpoint.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end="")


if __name__ == "__main__":
    main()
