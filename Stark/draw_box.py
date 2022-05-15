import os
import cv2
'''
显示跟踪训练数据集标注
'''
root_path="/home/ryan"
#img_dir = 'Stark/data/got10k/cir05'
#label_dir='cir/got10k/cir05/groundtruth.txt'
img_dir="Stark/data/got10k/cir21"
label_dir="Stark/test/tracking_results/stark_s/baseline_got10k_only/got10k/cir21.txt"
 
imgs=os.listdir(root_path+"/"+img_dir)
imgs.remove('absence.label')
imgs.remove('cover.label')
imgs.remove('cut_by_image.label')
imgs.remove('groundtruth.txt')
#imgs.remove('cir05.mp4')

imgs.sort(key=lambda x:int(x.split('.')[0]))

for i,img in enumerate(imgs) :
    print(i, img)
    img_name=int(img[:-4])-1	#.jpg
    #img_name=int(img[:-5])#	#.jpeg
    label_f=open(root_path+"/"+label_dir,"r")
    lines=label_f.readlines()[img_name]
    print(lines)
    img_data=cv2.imread(root_path+"/"+img_dir+"/"+img)
    H,W,C=img_data.shape
    #line_list=lines.split(',')
    line_list=lines.split('	')
    print(line_list)
        # class_num=int(line_list[0]) #类别号
        # obj_ID=int(line_list[1])    #目标ID
    x,y,w,h=line_list[:]       #中心坐标，宽高（经过原图宽高归一化后）
    print(x,y,w,h) 
    x=int(x)
    y=int(y)
    w=int(w)
    h=int(h)
    left=int(x)
    bottom=int(y)
    right=left+w
    top=bottom+h
    cv2.circle(img_data,(x,y),1,(0,0,255))
    cv2.rectangle(img_data, (left,top),(right,bottom), (0,255,0), 2)
        #cv2.putText(img_data, str(obj_ID), (left,top), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 1)
#resized_img=cv2.resize(img_data,(800,416))
    #cv2.imshow("label",img_data)
    cv2.waitKey(0)
    cv2.imwrite('/home/ryan/Stark/test/tracking_results/stark_s/baseline_got10k_only/'+img, img_data)
