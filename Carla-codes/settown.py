import carla

def main():
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    client.load_world("Town10")

if __name__=="__main__":
    main()