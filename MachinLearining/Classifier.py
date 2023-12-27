from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
model =""
models.load_model("baseline_mariya.keras")
import numpy as np



def predict_image(model, path_to_img):
    img = Image.open(path_to_img)
    img.convert("RGB")
    img.resize(32,32)
    data =np.array(img)
    print("before", data[0][0])
    data=data/255
    print("after", data[0][0])
    probs =model.predict(np.array([data])[:1])
    print(probs)
    print(probs.max())
    print(np.argmax(probs))



content =""
img_path="placeholder_image.png"

index = """
<|text-center|
<|{"log.png"}|image|width=25vw|>

<|{content}|file_selector|| extensions=.png|>
select an image from your file system

<|{img_path}|image|>

<|label goes here|indicator|value=0|min=0|max=100|width=25vw|>
>
"""

def on_change(state, var_name, var_val):
    if var_name=="content":
        state.img_path=var_val
        predict_image(model, var_val)
    print(var_name, var_val)


app = Gui(page=index)

if __name__ =="__main__":
    app.run(use_reloader=True)
