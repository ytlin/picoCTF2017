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
  * 思路: 
   * 方向 1. 一開始毫無頭緒，把LSB瞭解之後可以用線上工具去解看看圖片，夠細心會發現左下角有異樣，然後再針對最後一行處理即可  
   * 方向 2. 也是我的方法，直接把整張圖做 1 bit的decode,把蒐集的binary string轉成ASCII印出來，就可以看到flag  
