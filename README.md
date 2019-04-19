# gymTraining

dockerized Version of openai´s gym in combination with an jupyter notebook to access the gym package inside the container.

## Getting Started

These instructions show you how to use this project to set up a openai gym environment. 

### Prerequisites

If you haven´t already installed docker, just download the installer from docs.docker.com
[Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
[Docker for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)
[Docker for Mac OS](https://docs.docker.com/docker-for-mac/install/)

### Installing

Running the environment is fairly simple. Switch to the cloned repository and build the image

```
git clone https://github.com/FelixKleineBoesing/gymTraining.git
cd gymTraining
docker-compose up --build
```

Now you are running a gym environment with a jupyter notebook running on port 8888 on localhost.

###Content

For now there are only a few notebooks included which where created during my Reinforcement Learning Course. But more Content is likely to follow. 

###Usage

If you executed the docker-compose command which is mentioned above the environment will start after building and you´re able to access it via an ordinary jupyter notebook. 
The src directory is mounted into the container, which means for you that everything you do in the work directory is persisted on your host system. If you want to add additional directory just add them in the docker-compose file. 

You are able to install python packages from jupyter notebook, but it would be more consistent to add them to requirements.txt. Don´t forget to add the suffix "--build" to "docker-compose up" if you added something to dockerfile or requirements. Otherwise the already built image would be used (without the local changes).

###Contributions

Feel free to fork and enhance the set of notebooks.