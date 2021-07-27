import cv2
import glob
import os
import os.path as osp
import shutil

images_dir_list = glob.glob("./xhs_*/*.jpg")
if not osp.exists("./result"):
    os.mkdir("./result")
if not osp.exists("./bad_result"):
    os.mkdir("./bad_result")

for i, image_dir in enumerate(images_dir_list):
    image = cv2.imread(image_dir)
    image_name = os.path.split(image_dir)[1]
    cv2.namedWindow("image", 0)
    cv2.imshow("image", image)

    key = cv2.waitKey()
    if key == ord("s") or key == ord("S"):
        try:
            print("正确判断的图片")
            shutil.move(image_dir, "./result")
            cv2.destroyAllWindows()
        except:
            print(f"{image_dir}文件已经存在")

    elif key == ord("z") or key == ord("Z"):
        try:
            print("错误判断的图片")
            shutil.move(image_dir, "./bad_result")
            cv2.destroyAllWindows()
        except:
            print(f"{image_dir}文件已经存在")

    elif key == ord("q") or key == ord("Q"):
        cv2.destroyAllWindows()
        break

    else:
        cv2.destroyAllWindows()
    
    print(f"还剩{len(images_dir_list) - i - 1}张图片待处理！")
