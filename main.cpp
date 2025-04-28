#include <iostream>
#include <string>

// This function returns a caption based on the image file name
std::string generateCaption(std::string imageName) {
    if (imageName == "dog.jpg") {
        return "A dog is sitting on the grass.";
    } else if (imageName == "beach.jpg") {
        return "A beautiful view of the beach.";
    } else {
        return "An image of something interesting.";
    }
}

int main() {
    std::string imageName;

    // Asks the user to input the image file name
    std::cout << "Enter image file name: ";
    std::cin >> imageName;

    // Get and print the generated caption
    std::string caption = generateCaption(imageName);
    std::cout << "Generated Caption: " << caption << std::endl;

    return 0;
}