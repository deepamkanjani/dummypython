#!/usr/bin/python
__author__ = 'deepam'

import Image, stepic

i = Image.open("new.jpg")
i.show()

steg = stepic.encode(i, "This is some random text i am trying to append")

steg.save("steg.jpg", "JPEG")

i2 = Image.open("steg.jpg")
i2.show()