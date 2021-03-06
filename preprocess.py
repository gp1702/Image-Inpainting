
import process_data
import numpy as np
import os
import pickle as pkl


if __name__ == "__main__":

    data_path = "inpainting/preprocess/"

    train_it = process_data.inital_process(batch_size=10000, load_caption=True, isCallFromPreprocess=True)

    no_img = 0
    all_caps = {}

    for i, [xs, ys, cs] in enumerate(train_it):

        print "Doing file no {}...".format(i)

        file_name_x = os.path.join(data_path, "data_train_x_{}.npy".format(i))
        file_name_y = os.path.join(data_path, "data_train_y_{}.npy".format(i))

        np.save(open(file_name_x, 'w'), xs)
        np.save(open(file_name_y, 'w'), ys)

        for img_caps in cs:
            img_caps2 = [" ".join(i) for i in img_caps]
            all_caps[no_img] = img_caps2
            no_img += 1

    print all_caps[0]

    caps_file = os.path.join(data_path, "caps.pkl")
    pkl.dump(all_caps, open(caps_file, 'w'))