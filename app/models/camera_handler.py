#import cv2 # type: ignore

class CameraHandler:
    def gen_frames():  
        return None
        camera = cv2.VideoCapture(0) 
        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')