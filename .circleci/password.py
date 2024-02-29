version: 2.1

jobs:
  print_password:
    docker:
      - image: python:3.8
    steps:
      - checkout
      - run:
          name: Print Password
          command: |
            my_password="WFJ1bgp@jax@xna-xny"
            echo "My password is: $my_password"
