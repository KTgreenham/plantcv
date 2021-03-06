### Image addition (saturation)
def image_sat_add(img1, img2, device, debug):
  # This is a function used to subtract one image from another image (img1 - img2)
  # The numpy subtraction function '-' is used. This is a modulo operation rather than the cv2.subtract fxn which is a saturation operation
  # img1 = input image
  # img2 = input image used to subtract from img1
  # device = device number. Used to count steps in the pipeline
  # debug = True/False. If True; print output image
  # ddepth = -1 specifies that the dimensions of output image will be the same as the input image
  s_added_img = cv2.add(img1, img2)
  device += 1
  if debug:
    print_image(s_added_img, str(device) + '_s_added' + '.png')
  return device, s_added_img