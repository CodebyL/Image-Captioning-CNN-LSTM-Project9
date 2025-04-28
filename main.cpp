#include <iostream>
#include <fstream>
#include <map>
#include <vector>

int main() {
    std::map<std::string, std::string> captions = {
        {"dog.jpg", "A dog is sitting on the grass."},
        {"beach.jpg", "A beautiful view of the beach."},
        {"car.jpg", "A red car parked on the street."},
        {"mountain.jpg", "Snow-covered mountains under a clear sky."},
        {"city.jpg", "A busy city skyline at night."}
    };

    std::ifstream inputFile("images.txt");
    std::ofstream outputFile("captions.txt");

    std::string imageName;

    while (inputFile >> imageName) {
        if (captions.find(imageName) != captions.end()) {
            outputFile << imageName << ": " << captions[imageName] << std::endl;
        } else {
            outputFile << imageName << ": An image of something interesting." << std::endl;
        }
    }

    std::cout << "Captions generated in captions.txt" << std::endl;

    return 0;
}