# LSB_decoder.py:  
  * usage: python LSB_decoder.py bmpFileName  
  * output: last bit of every RGB byte (24bits, RGB => 1 byte*3), and convert the binary data to ACSII  


#  Useful Reference:  
  * BMP file format: [Good explanation](http://www.pcschool.com.tw/campus/share/lib/160/)  
  * BMP color depth: [24 bit RGB](http://paulbourke.net/dataformats/bitmaps/)  
  * Python PIL library: [Image module: getpixel() ](https://pillow.readthedocs.io/en/4.1.x/reference/Image.html)  
  * Image Steganography online: [Useful tool](http://incoherency.co.uk/image-steganography/#unhide)  

# Note:  
  * the sequence of RGB color is *BGR* ... 我卡在這裡好久，原本用RGB的順序串binary string，弄半天找不到flag，原因待補  
  * [Someone else](http://mfridman.com/2017/04/14/pico2017-little-schoolbus.html)  
