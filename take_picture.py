from cv2 import VideoCapture
from cv2 import imshow
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyWindow

try:
    
    cam_port = 0
    cam = VideoCapture(cam_port)

    result, image = cam.read()

    if result:
        imshow("MRF", image)
        imwrite("MRF.png", image)
        waitKey(0)
        destroyWindow("MRF")

    else:
        print("No image found")
except Exception as e:
    assert e
