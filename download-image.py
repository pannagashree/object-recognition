import cv2
vidcap = cv2.VideoCapture('VID_20170508_224709.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  cv2.imwrite("./Negative_images/Frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
