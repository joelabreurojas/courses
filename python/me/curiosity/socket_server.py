from socket import socket, AF_INET, SOCK_STREAM


def handle_client(client: socket) -> None:
    """Handles a single client connection."""
    try:
        received: str = client.recv(4096).decode()
        message: str = received.splitlines()[0] if received else ""
        response: str = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body><h1>Hello, World!</h1></body></html>"

        if message:
            print(f"Received: {message}")

        client.sendall(response.encode())

    except Exception as e:
        print(f"Client error: {e}")

    finally:
        client.close()


def create_server(host: str, port: int) -> None:
    """Creates and runs the server."""
    with socket(AF_INET, SOCK_STREAM) as server:
        try:
            server.bind((host, port))
            server.listen(5)

            print(f"Server listening on http://{host}:{port}")

            while True:
                client, address = server.accept()

                print(f"Connection from {address}")

                handle_client(client)

        except KeyboardInterrupt:
            print("\nShutting down...\n")

        except Exception as e:
            print(f"Server error: {e}")


def main() -> None:
    host: str = "localhost"
    port: int = 9000

    create_server(host, port)


if __name__ == "__main__":
    main()
