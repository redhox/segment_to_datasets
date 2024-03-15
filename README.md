# Python Project with Docker for YOLOv8

This project uses Docker to create an isolated environment for running a Python script that retrieves segmented images from a folder and transforms them into a dataset compatible with YOLOv8.

![alt text](https://git.morgan-coulm.fr/coulm/segment_to_datasets/-/raw/main/image5.png)
## Prerequisites

- Docker installed on your machine.
- A folder containing the segmented images to be used for creating the dataset.

## Installation

1. Clone this repository to your local machine.
2. Place your segmented images in the `image_debase/image` folder at the root of the project.


        .
        ├── image_debase
        │   ├── image
        │   │   ├── objet1 
        │   │   │   ├── segmented_images_of_objet1.jpg
        │   │   │   └── segmented_images_of_objet1.jpg
        │   │   ├── objet2  
        │   │   │   ├── segmented_images_of_objet2.jpg
        │   │   │   ├── segmented_images_of_objet2.jpg
        │   │   │   └── segmented_images_of_objet2.jpg
        │   │   ├── objet3
        │   │   │   ├── segmented_images_of_objet3.jpg

## Building the Docker Image

Run the following command in the project directory to build and execute the Docker image:

    docker-compose up

## Running the Docker Container

To run the Docker container and create the YOLOv8 dataset, use the following command:


This command mounts the `segmented_images` folder containing your segmented images into the container and creates an `output` folder to store the generated YOLOv8 dataset.

## Project Structure
    .
    ├── app.py
    │
    ├── datasets
    │   ├── data.yaml
    │   ├── test
    │   │   ├── images
    │   │   └── labels
    │   ├── train
    │   │   ├── images
    │   │   └── labels
    │   └── val
    │       ├── images
    │       └── labels
    │
    ├── docker-compose.yml
    ├── Dockerfile
    ├── image_debase
    │   ├── image
    │   │   ├── *segmented_images*
    │   └── imagep.jpg
    └── requirements.txt



## License

This project is under the MIT license.
