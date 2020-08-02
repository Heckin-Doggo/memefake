import os
import datetime


def main():
    print("Welcome to MemeFake 1.1.1")
    image = None  # no image to start
    while not image:  # while no image path exists
        image = input("Image Location? \n>>>")
        if not os.path.isfile(image):  # if no image exist.
            print("File not found, try again.\n")
            image = None  # no image for you

    video = None
    while not video:
        video = input("Video Location? \n>>>")
        if not os.path.isfile(video):
            print("File not found, try again.\n")
            video = None

    save_dir = None
    while not save_dir:
        save_dir = input("Save to which directory? \n>>>")
        if not os.path.isdir(save_dir):
            print("Directory not found, try again.\n")
            save_dir = None

    save_name = input("File name?\n>>>")  # append an mp4

    temp_vid = save_dir + "/" + save_name + "_temp.mp4"  # appended

    mode = input("Absolute mode? [y/n]\n"
                 "(default is relative mode)\n"
                 ">>>")

    flag = "--relative "  # the flag for relative/abs
    if mode.lower().strip() == "y":
        flag = ""  # remove the relative flag.

    save_path = save_dir+"/"+save_name

    # deepfake command
    df = "python demo.py --config config/vox-256.yaml --driving_video {} --source_image {} --checkpoint vox-cpk.pth.tar {}--adapt_scale --result_video {}".format(video, image, flag, temp_vid)
    os.system(df)

    # ffmpeg command
    ff = "ffmpeg -i {} -i {} -c copy -map 0:0 -map 1:1 -shortest {}.mp4".format(temp_vid, video, save_path)
    os.system(ff)

    # remove the temp file.
    os.remove(temp_vid)

    # the below probably isnt necessary anymore.
    print("\n------------")
    print("Image: " + image)
    print("Video: " + video)
    print(save_dir)

    print("\n Done! Saved to {}.mp4".format(os.path.abspath(save_dir+"/"+save_name)))  # print full path.
    print("Finished at {}".format(datetime.datetime.now()))  # for that pizzazz.
    input("Press enter to exit.")
    
    
if __name__ == "__main__":
    main()