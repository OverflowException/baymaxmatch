import threading
import time
import socket
import random
import cv2

def tcplink(sock, addr):
    global status;
    print('Accept new connection from %s:%s...' % addr); 
    while True: 
        status = sock.recv(1);
        time.sleep(0.001); 
        if not status or status.decode('utf-8') == 'exit': 
           break; 
    print('Connection from %s:%s closed.' % addr);
    status = 'terminate'
    
def main_game(delay):
    images = [];
    images.append(cv2.imread('./upup.jpg'));
    images.append(cv2.imread('./downdown.jpg'));
    images.append(cv2.imread('./updown.jpg'));
    images.append(cv2.imread('./downup.jpg'));
    image_correct = cv2.imread('./correct.jpg');
    image_incorrect = cv2.imread('./incorrect.jpg');
    
    while True:
        image_index = random.randint(0,3);
        cv2.imshow('Match Gesture', images[image_index]);
        cv2.waitKey(delay);
        print(status)
        if status == 'terminate':
            break;
        
        if status == str(image_index):
            cv2.imshow('Match Gesture', image_correct);
            print 'Gesture Correct!\n'
            cv2.waitKey(500);
        else:
            cv2.imshow('Match Gesture', image_incorrect);
            print 'Gesture Incorrect!\n'
            cv2.waitKey(500);
            #ref_image = cv2.Mat();
            #imshow('Match Gesture', );
        #time.sleep(1);
        #print('main_game',status1,status);

  
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); 
    s.bind(('127.0.0.1', 9090)); 
    s.listen(1);
    print('waiting for connection...'); 
    sock, addr = s.accept();
    print('connected');
    
    t1=threading.Thread( target=tcplink, args=(sock, addr));
    t2=threading.Thread( target=main_game, args=(1500,));
    t1.start();
    t2.start();
