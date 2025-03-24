🎯 Captioning System Rules<br />

* The system looks at an image and generates a caption describing it.<br />
* It uses a CNN (Convolutional Neural Network) (InceptionV3) to understand the image content.<br />
* It uses an LSTM (Long Short-Term Memory) model to generate a short sentence based on the image.<br />
* This version uses a simplified mock caption to demonstrate how the system works.<br />
___________________________________________________________________________________________________

📌 How it Works? <br />

1️⃣ Install Python and Required Libraries<br />
* Download and install Python 3.x from python.org.<br />
* Open terminal and run: **pip install tensorflow numpy pillow matplotlib**<br />

2️⃣ Download the Script<br />
* Save the **image_captioning.py** file to your computer.<br />

3️⃣ Add an Image<br />
* Place an image in the same folder as the script.<br />
* Rename the image to **example.jpg** (or update the script with your image filename).<br />

4️⃣ Run the Program<br />
* Open a terminal (Command Prompt or Terminal) and navigate to the folder where the file is saved.<br />
* Run the following command: **python image_captioning.py**<br />

5️⃣ View the Result<br />
* The image will be displayed with a generated caption shown above it.<br />
* In this version, the caption is a simple sample output to show how it works.<br />
___________________________________________________________________________________________________

🌟 Code Explanation<br />
<br />
```base_model = InceptionV3(weights='imagenet')```<br />
* Loads a pre-trained CNN model that understands image features.<br />
<br />

```cnn_model = Model(base_model.input, base_model.layers[-2].output)```<br />
* This gives us the feature vector from the image by removing the last classification layer.<br />
<br />

```def preprocess_image(image_path):```<br />
* Resizes and normalizes the image to fit what the CNN expects.<br />
* Adds a batch dimension so it works with the model.<br />
<br />

```def extract_features(image_path):```<br />
* Runs the image through the CNN to get the image's feature representation.<br />
<br />

```word_to_index = {"<start>": 1, "<end>": 2, "dog": 3, "playing": 4, "grass": 5}```<br />
* This is a small vocabulary used to simulate caption generation.<br />
<br />

```embedding = Embedding(...)```<br />
* Turns words (as numbers) into vectors that the LSTM can understand.<br />
<br />

```lstm = LSTM(256, return_sequences=True)(embedding)```<br />
* The LSTM reads the word sequence and learns how to form a sentence.<br />
<br />

```def generate_caption(image_features):```<br />
* Returns a simple example caption: "A dog playing in grass."<br />
* In a real system, this would generate a caption based on LSTM predictions.<br />
<br />

```plt.imshow(img)```<br />
* Displays the image in a pop-up window.<br />
* The caption appears as the title above the image.<br />
