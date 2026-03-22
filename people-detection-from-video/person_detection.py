mport cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

video = cv2.VideoCapture("people.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Resize to 9:16 (e.g., 360x640 or 720x1280)
    frame = cv2.resize(frame, (360, 640))

    bbox, label, conf = cv.detect_common_objects(frame)
    person_count = label.count("person")

    output = draw_bbox(frame, bbox, label, conf)

    cv2.putText(output, f"People: {person_count}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("People Counter", output)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
