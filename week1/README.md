## 컴퓨터비전 1주차 실습

### 1. Convert colour image into grayscale, then concatenate two horizontally.

1. Read an image
   ```python
   img = cv.imread('path to image')
   
2. Convert colour image into grayscale, and vice versa to match their dimensions 1 -> 3.
    ```python
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    ```

3. Concatenate the images and print.
    ```python
    concat_img = np.hstack((img, gray))
    cv.imshow('concatenated image', concat_img)
    ```

4. Quit the loop if key q is inputted.
     ```python
     key = cv.waitKey(1)
     if key==ord('q'):
      cv.destroyAllWindows()
      cv.imwrite('C:\wona_CV\week1\data/soccer_concatenated.jpg', concat_img)
      break
    ```

<img src="https://github.com/user-attachments/assets/09d15aab-9924-486f-bde1-903297d15627" width="40%">


### 2.  Connect original streaming frames from a webcam with canny edge detection frames horizontally.
1. Connect a webcam
    ```python
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    ```

2. Convert the frames into gray scale - Canny Edge Detection
    ```python
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
    edge = cv.Canny(gray, 50, 200)
    ```

3. Concat the original and canny edge detection image together and print
   ```python
   concat_img = np.hstack((frame, cv.cvtColor(edge, cv.COLOR_GRAY2BGR)))
   cv.imshow('Video display', concat_img)
    ```
<img src="https://github.com/user-attachments/assets/c6025e46-7f69-46fc-a46c-6b7f9527f819" width="40%">

### 3.  Select ROI in an image with mouse drags through cv.setMouseCallback(), and reset or save the ROI based on the input key (r, s)
1. Read an image and print
    ```python
    img = cv.imread('path to image')
    cv.imshow('Drawing', img)
    ```

2. Call the Mouse Event Callback Function
   ```python
   cv.setMouseCallback('Drawing', draw)
   
3. Mouse Callback Function
   1. When the mouse first pressed, change the mouse status as pressed.
      ```python
      if event==cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        cv.rectangle(tmp_img, (x, y), (ix+1, iy+1), (0, 0, 255), 2)
        pressed = True
      ```
   2. If the mouse stauts remain pressed and the mouse is moving, draw a rectangle for every frame.
      ```python
      elif event == cv.EVENT_MOUSEMOVE and pressed==True:
        cv.rectangle(tmp_img, (ix, iy), (x, y), (0, 0, 255), 2)
      ```
      
   3. WHen the mouse pressing stops, change the status and print the rectangle made before as ROI.
      ```python
      elif event==cv.EVENT_LBUTTONUP:
        roi = img[iy:y, ix:x]
        cv.imshow('ROI', roi)
        pressed = False
      ```
      
    4. Print the frame with a rectangle. Noe that the rectangle is printed for every new frame.
       ```python
       cv.imshow('Drawing', tmp_img)
       
4. Reset ROI selection when the key 'r' is typed.
   ```python
   if key==ord('r'):
     roi = None
     cv.imshow('Drawing', img)
   ```
   
5. Save the ROI image when the key 's' is pressed.
   ```python
   elif key==ord('s'):
        if roi is not None:
            cv.imwrite('C:\wona_CV\week1\data/roi.jpg', roi)
            print("ROI saved")
   ```
<img src="https://github.com/user-attachments/assets/9b588bce-588f-4618-930f-ea6abc260f8b" width="20%">

